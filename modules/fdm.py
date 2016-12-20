# -*- coding: utf-8 -*-
"""
3D Finite Difference Models as a function.
Stream line computation (Psi) and a function
Computaion of veclocity vector for plotting with quiver

Created on Fri Sep 30 04:26:57 2016

@author: Theo

"""
import sys

myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules'

if not myModules in sys.path:
    sys.path.insert(0, myModules)

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as la
import scipy.special
from collections import namedtuple
import matplotlib.pylab as plt
import mfexceptions as err
import mfgrid
import pdb

def quivdata(Out, x, y, iz=0):
    """Returns vector data for plotting velocity vectors.

    Takes Qx from fdm3 and returns the tuple X, Y, U, V containing
    the velocity vectors in the xy plane at the center of the cells
    of the chosen layer for plotting them with matplotlib.pyplot's quiver()

    Parameters
    ----------
    `Qx` : ndarray
        field in named tuple returned by fdm3.
    `x` : ndarray
        grid line coordinates.
    `y` : ndarray
        grid line coordinates.
    `iz` : int
        layer number for which vectors are computed (default 0)

    Returns:
        tuple: X, Y, U,V

        X : ndaarray
            2D ndArray of x-coordinates cell centers
        Y : ndarray
            2D ndarray of y-coordinate of cell centers
        U : ndarray
            2D ndarray of x component of cell flow [L3/T]
        V : ndarray
            2D ndarray of y component of cell flow [L3/T]

    """
    Ny = len(y)-1
    Nx = len(x)-1
    xm = 0.5 * (x[:-1] + x[1:])
    ym = 0.5 * (y[:-1] + y[1:])

    X, Y = np.meshgrid(xm, ym) # coordinates of cell centers

    # Flows at cell centers
    U = np.concatenate((Out.Qx[:,0,iz].reshape((Ny,1,1)), \
                        0.5 * (Out.Qx[:,:-1,iz].reshape((Ny,Nx-2,1)) +\
                               Out.Qx[:,1:,iz].reshape((Ny,Nx-2,1))), \
                        Out.Qx[:,-1,iz].reshape((Ny,1,1))), axis=1).reshape((Ny,Nx))
    V = np.concatenate((Out.Qy[0,:,iz].reshape((1,Nx,1)), \
                        0.5 * (Out.Qy[:-1,:,iz].reshape((Ny-2,Nx,1)) +\
                               Out.Qy[1:,:,iz].reshape((Ny-2,Nx,1))), \
                        Out.Qy[-1,:,iz].reshape((1,Nx,1))), axis=0).reshape((Ny,Nx))
    return X, Y, U, V


def psi(Qx, row=0):
    """Returns stream function values in z-x plane for a given grid row.

    The values are at the cell corners in an array of shape [Nz+1, Nx-1].
    The stream function can be vertically contoured using gr.Zp and gr.Xp as
    coordinates, where gr is an instance of the Grid class.

    Arguments:
    Qx --- the flow along the x-axis at the cell faces, excluding the outer
           two plains. Qx is one of the fields in the named tuple returned
           by fdm3.
    row --- The row of the cross section (default 0).

    It is assumed:
       1) that there is no flow perpendicular to that row
       2) that there is no storage within the cross section
       3) and no flow enters the model from below.
    The stream function is computed by integrating the facial flows
    from bottom to the top of the model.
    The outer grid lines, i.e. x[0] and x[-1] are excluded, as they are not in Qx
    The stream function will be zero along the bottom of the cross section.

    """
    Psi = Qx[row,:,:].T # Copy the section for which the stream line is to be computed.
                        # and transpose to get the [z,x] orientation in 2D
    Psi = Psi[::-1,:].cumsum(axis=0)[::-1,:]         # cumsum from the bottom
    Psi = np.vstack((Psi, np.zeros(Psi[0,:].shape))) # add a row of zeros at the bottom
    return Psi


#def fdm3(x, y, z, kx, ky, kz, FQ, HI, IBOUND, axial=False):
def fdm3(gr, K, FQ, HI, IBOUND, axial=False):
    '''Compute a 3D steady state finite diff. model

    Returns a namedtuple with fields Phi, Qx, Qy, Qz and cell flow Q
    Output shapes are
    (Ny,Nx,Nz) (Ny,Nx-1,Nz), (Ny-1,Nx,Nz), (Ny,Nx,Nz-1), (Ny, Nx, Nz)
        --------------------------------------------
    inputs:
    gr  --- Grid instance (see mfgrid.Grid)
    K   --- np.ndarray or a 3-tuple of np.ndarrays containing
        if 3-tuple then the 2 np.ndarrays are kx, ky and kz
            kx  --- array of cell conductivities along x-axis (Ny, Nx, Nz)
            ky  --- same for y direction (if None, then ky=kx )
            kz  --- same for z direction
        else then kx = ky = kz = K

    FQ  --- array of prescrived cell flows (injection positive (Ny, Nx, Nz),
             zero of no inflow/outflow)
    IH  ---  array of initial heads. (Ny,Nx, Nz)
    IBOUND --- the boundary array like in MODFLOW (Ny, Nx, Nz)
               with values denoting:
    * IBOUND>0  the head in the corresponding cells will be computed
    * IBOUND=0  cells are inactive, will be given value NaN
    * IBOUND<0  coresponding cells have prescribed head
    --------------------------------------------

    TO 160905
    '''

    # notice that Our is a class. It is instantiated in the return below
    Out = namedtuple('Out',['Phi', 'Q', 'Qx', 'Qy', 'Qz'])
    Out.__doc__ = """From fdm3: with fields Phi, 'Q', Qx, Qy, Qz and Q."""


    Ny, Nx, Nz = SHP = gr.shape
    Nod = Ny * Nx * Nz
    NOD = np.arange(Nod).reshape(SHP) # generate cell numbers

    if gr.axial==True:
        print("axial==True so that y coordinates and ky are ignored")
        print("            and x stands for r, so that all x coordinates must be >= 0.")
    if isinstance(K, np.ndarray): # only one ndaray was given
        kx = ky = kz = K
    elif isinstance(K, tuple): # 3-tuple of ndarrays was given
        kx, ky, kz = K
    else:
        raise err.InputError("", "K must be an narray of shape (Ny,Nx,Nz) or a 3tuple of ndarrays")

    if kx.shape != SHP:
        raise AssertionError("shape of kx {0} differs from that of model {1}".format(kx.shape, SHP))
    if ky.shape != SHP:
        raise AssertionError("shape of ky {0} differs from that of model {1}".format(ky.shape, SHP))
    if kz.shape != SHP:
        raise AssertionError("shape of kz {0} differs from that of model {1}".format(kz.shape, SHP))

    # from this we have the width of columns, rows and layers
    dx = gr.dx.reshape(1,Nx,1)
    dy = gr.dy.reshape(Ny,1,1)
    dz = gr.dz.reshape(1,1,Nz)

    active = (IBOUND>0 ).reshape(Nod,)  # boolean vector denoting the active cells
    inact  = (IBOUND==0).reshape(Nod,) # boolean vector denoting inacive cells
    fxhd   = (IBOUND<0 ).reshape(Nod,)  # boolean vector denoting fixed-head cells

    if gr.axial==False:
        Rx2 = 0.5 * dx / (dy * dz) / kx
        Rx1 = 0.5 * dx / (dy * dz) / kx
        Ry  = 0.5 * dy / (dz * dx) / ky
        Rz  = 0.5 * dz / (dx * dy) / kz
        #half cell resistances regular grid
    else:
        Rx2 = 1 / (2 * np.pi * kx[:,1: ,:] * dz) * np.log(gr.xm[1:]/gr.x[1:-1]).reshape((1, Nx-1, 1))
        Rx1 = 1 / (2 * np.pi * kx[:,:-1,:] * dz) * np.log(gr.x[1:-1]/gr.xm[:-1]).reshape((1, Nx-1, 1))
        Rx2 = np.hstack((np.Inf * np.ones((Ny,1,Nz)), Rx2))
        Rx1 = np.hstack((Rx1, np.Inf * np.ones((Ny,1,Nz))))
        Ry = np.Inf * np.ones(SHP)
        Rz = 0.5 * dz.reshape((1,1,Nz))  / (np.pi * (gr.x[1:]**2 - gr.x[:-1]**2).reshape((1,Nx,1)) * kz)
        #half cell resistances with grid interpreted as axially symmetric

    # set flow resistance in inactive cells to infinite
    Rx2 = Rx2.reshape(Nod,); Rx2[inact] = np.Inf; Rx2=Rx2.reshape(SHP)
    Rx1 = Rx1.reshape(Nod,); Rx1[inact] = np.Inf; Rx1=Rx1.reshape(SHP)
    Ry  = Ry.reshape( Nod,); Ry[ inact] = np.Inf; Ry=Ry.reshape(SHP)
    Rz  = Rz.reshape( Nod,); Rz[ inact] = np.Inf; Rz=Rz.reshape(SHP)
    #Grid resistances between nodes

    Cx = 1 / (Rx1[:,:-1,:] + Rx2[:,1:,:])
    Cy = 1 / (Ry[ :-1,:,:] + Ry[ 1:,:,:])
    Cz = 1 / (Rz[ :,:,:-1] + Rz[ :,:,1:])
    #conductances between adjacent cells

    IE = NOD[:,1:,:]  # east neighbor cell numbers
    IW = NOD[:,:-1,:] # west neighbor cell numbers
    IN = NOD[:-1,:,:] # north neighbor cell numbers
    IS = NOD[1:,:,:]  # south neighbor cell numbers
    IT = NOD[:,:,:-1] # top neighbor cell numbers
    IB = NOD[:,:,1:]  # bottom neighbor cell numbers
    #cell numbers for neighboors

    R = lambda x : x.ravel()  # shorthand for x.ravel()

    # notice the call  csc_matrix( (data, (rowind, coind) ), (M,N))  tuple within tupple
    # also notice that Cij = negative but that Cii will be postive, namely -sum(Cij)
    A = sp.csc_matrix((
            -np.concatenate(( R(Cx), R(Cx), R(Cy), R(Cy), R(Cz), R(Cz)) ),\
            (np.concatenate(( R(IE), R(IW), R(IN), R(IS), R(IB), R(IT)) ),\
             np.concatenate(( R(IW), R(IE), R(IS), R(IN), R(IT), R(IB)) ),\
                      )),(Nod,Nod))

    # to use the vector of diagonal values in a call of sp.diags() we need to have it aa a
    # standard nondimensional numpy vector.
    # To get this:
    # - first turn the matrix obtained by A.sum(axis=1) into a np.array by np.array( .. )
    # - then take the whole column to loose the array orientation (to get a dimensionless numpy vector)
    adiag = np.array(-A.sum(axis=1))[:,0]

    A += sp.diags(adiag)
    # diagonal matrix, a[i,i]

    RHS = FQ.reshape(Nod,1) - A[:,fxhd].dot(HI.reshape(Nod,1)[fxhd])
    # Right-hand side vector.

    Phi = HI.flatten()
    # Allocate space to store heads.

    Phi[active] = la.spsolve( A[active][:,active] ,RHS[active] )
    # Solve heads at active locations.

    # net cell inflow
    Q  = A.dot(Phi).reshape(gr.shape)

    # reshape Phi to shape of grid
    Phi = Phi.reshape(gr.shape)

    #Flows across cell faces
    Qx =  -np.diff(Phi, axis=1) * Cx
    Qy =  +np.diff(Phi, axis=0) * Cy
    Qz =  +np.diff(Phi, axis=2) * Cz

        # set inactive cells to NaN
    Phi[inact.reshape(gr.shape)] = np.NaN # put NaN at inactive locations

    return Out(Phi=Phi, Q=Q, Qx=Qx, Qy=Qy, Qz=Qz) # this instantiates an Out object

# Examples that take the function of tests
def example_Mazure():
    """1D flow in semi-confined aquifer example
    Mazure was Dutch professor in the 1930s, concerned with leakage from
    polders that were pumped dry. His situation is a cross section perpendicular
    to the dike of a regional aquifer covered by a semi-confining layer with
    a maintained head in it. The head in the regional aquifer at the dike was
    given as well. The head obeys the following analytical expression
    phi(x) - hp = (phi(0)-hp) * exp(-x/lam), lam = sqrt(kDc)
    To compute we use 2 model layers and define the values such that we obtain
    the Mazure result.
    """
    x = np.hstack((0.001, np.linspace(0., 2000., 101))) # column coordinates
    y = np.array([-0.5, 0.5]) # m, model is 1 m thick
    d = 10. # m, thickness of confining top layer
    D = 50. # m, thickness of regional aquifer
    z = np.array([0, -d, -d-D]) # tops and bottoms of layers
    gr = mfgrid.Grid(x, y, z, axial=False)
    c = 250 # d, vertical resistance of semi-confining layer
    k1 = d/c # m/d conductivity of the top layer
    k2 = 10. # m/d conductivity of the regional aquifer
    kD = k2 * D # m2/d, transmissivity of regional aquifer
    lam = np.sqrt(kD * c) # spreading length of semi-confined aquifer
    K = gr.const([k1/2., k2]) # k1 = 0.5 d/c because conductance from layer center
    FQ = gr.const(0) # prescribed flows
    s0 = 2.0 # head in aquifer at x=0
    IH = gr.const(0); IH[:,0,-1] = s0 # prescribed heads
    IBOUND = gr.const(1); IBOUND[:,:,0] = -1; IBOUND[:,0,-1]=-1
    Out = fdm3(gr, K, FQ, IH, IBOUND) # compute heads, run model
    plt.figure()
    plt.setp(plt.gca(), 'xlabel','x [m]', 'ylabel', 'head [m]', 'title', 'Mazure 1D flow')
    plt.plot(gr.xm, Out.Phi[0,:,-1], 'ro-', label='fdm3') # numeric solution
    plt.plot(gr.x, s0 * np.exp(-gr.x / lam),'bx-', label='analytic') # analytic solution
    plt.legend()

def example_De_Glee():
    """Axial symmetric example, well in semi-confined aquifer (De Glee case)
    De Glee was a Dutch engineer/groundwater hydrologist and later the
    first director of the water company of the province of Groningen.
    His PhD (1930) solved the axial symmetric steady state flow to a well
    in a semi confined aquifer using the Besselfunctions of the second kind,
    known as K0 and K1.
    The example computes the heads in the regional aquifer below a semi confining
    layer with a fixed head above. It uses two model layers a confining one in
    which the heads are fixed and a semi-confined aquifer with a prescribed
    extraction at r=r0. If r0>>0, both K0 and K1 Bessel functions are needed.
    The grid is signaled to use inteprete the grid as axially symmetric.
    """
    K0 = lambda x: scipy.special.kn(0, x) # Bessel function second kind, order 0
    K1 = lambda x: scipy.special.kn(1, x) # Bessel function second kind, order 1
    Q  = -1200.0 # m3/d, well extraction
    r0 = 100.  # m, well radius
    R  = 2500. # m, outer radius of model
    d = 10. # m, thickness of confining top layer
    D = 50. # m, thickness of regional aquifer
    c = 250 # d, vertical resistance of confining top layer
    k1 = d/c # m/d conductivity of confining top layer
    k2 = 10.  # m/d conductivity of regional aquifer
    kD = k2 * D # m2/d, transmissivity of regional aquifer
    lam = np.sqrt(kD * c) # spreading length of regional aquifer
    r  = np.hstack((r0+0.001, np.logspace(np.log10(r0), np.log10(R), 41))) # distance to well center
    y = None # dummy, ignored because problem is axially symmetric
    z = np.array([0, -d, -d-D]) # m, elevation of tops and bottoms of model layers
    gr = mfgrid.Grid(r, y, z, axial=True) # generate grid
    FQ = gr.const(0.)
    FQ[0,0,-1] = Q # m3/d fixed flows
    IH = gr.const(0.) # m, initial heads
    IBOUND = gr.const(1)
    IBOUND[:,:,0] = -1 # modflow like boundary array
    K = gr.const([k1/2., k2]) # full 3D array of conductivities
    Out = fdm3(gr, K, FQ, IH, IBOUND) # run model
    plt.figure()
    plt.setp(plt.gca(), 'xlabel', 'r [m]', 'ylabel', 'head [m]',\
             'title', 'De Glee, well extraction, axially symmetric', 'xscale', 'log', 'xlim', [1.0, R])
    plt.plot(gr.xm, Out.Phi[0,:,-1], 'ro-', label='fdm3')
    plt.plot(gr.x, Q/(2 * np.pi * kD) * K0(gr.x / lam) / (r0/ lam * K1(r0/ lam)), 'bx-',label='analytic')
    plt.legend()

if __name__ == "__main__":
    example_Mazure()
    example_De_Glee()
