
import sys

myModules = './modules/'

if not myModules in sys.path:
    sys.path.insert(1, myModules)


import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import axes3d  # leave for 3D plots

import numpy as np
from collections import namedtuple
import pdb

import fdm
import mfgrid
#import mfetc
import mfexceptions as err

def AND(*args):
    L = args[0]
    for arg in args:
        L = np.logical_and(L, arg)
    return L

def OR(*args):
    L = args[0]
    for arg in args:
        L = np.logical_or(L, arg)
    return L

NOT = np.logical_not


INDICES = lambda Lp : np.arange(len(Lp))[Lp]  # Lp is a boolean array

def TRANSFER(it, *args):
    """Transfer the data from previous tme to this time (all in place)"""
    for arg in args:
        arg[:,it] = arg[:,it-1]


print("loading mfpath.py")

def isSink(Q, Qx, Qy, Qz, sinkfrac=0.75, tol=1e-4):
    """Returns boolean array telling which cells are a sink

    A sink is when more than sinkfrac of the water entering the cell is
    extracted from it.

    Parameters
    ----------
    Q, Qx, Qy, Qz : ndarrays obtained from finite difference model
    sinkfrac : float, fraction of extraction relative to inflow
    tol : small value prevents division by zero if Qinto==0

    Returns
    -------
    boolean array that is True for a sink and False otherwise

    @TO 16106
    """
    Qinto = np.zeros(Q.shape)
    Qinto[:, 1:,:] +=  Qx * (Qx>0)
    Qinto[:,:-1,:] += -Qx * (Qx<0)
    Qinto[ 1:,:,:] += -Qy * (Qy<0)
    Qinto[:-1,:,:] +=  Qy * (Qy>0)
    Qinto[:,:, 1:] += -Qz * (Qz<0)
    Qinto[:,:,:-1] +=  Qz * (Qz>0)

    return -Q * (Q<0) /(tol + Qinto) > sinkfrac


def plot_particles(Pcl, axes=None, first_axis='z',
             markers='+o*.xsdph^v<>', ugrid=False, **kwargs):
    """Plots particles on current axis

    Parameters:
    -----------
    Pcl : named tuple with tracked particles as produced by particle_tracker
    ax  : a legal axes or None in which case a 3D plot will me made.
    third_axis: axis perpendicular to plotting plane, so
                'z' if x and y are to be plotted
                'y' if x and z are to be plotted(cross section)
    ugrid : boolean, if True plot particles in normalized grid.

    @ TO 161115
    """
    from mpl_toolkits.mplot3d import Axes3D

    if axes is None:
        fig = plt.figure()
        axes = fig.add_subplot(111, projection='3d')
    if ugrid==False:
        X = Pcl.x
        Y = Pcl.y
        Z = Pcl.z
    else:
        X = Pcl.u
        Y = Pcl.v
        Z = Pcl.w
    if isinstance(axes, Axes3D):
        for ip in range(X.shape[0]):
            L  = Pcl.status[ip,:] > 0.
            NL = NOT(L)
            plt.axes(axes)
            plt.plot(X[ip, :], Y[ip, :], Z[ip, :], 'b.-')
            plt.plot(X[ip, NL], Y[ip, NL], Z[ip, NL], 'r.' )
    elif isinstance(axes, plt.Axes):
        if first_axis=='z':
          xx=X
          yy=Y
        elif first_axis=='y':
          xx=X
          yy=Z
        elif first_axis=='x':
          xx=Y
          yy=Z
        else:
          print("first_axis must be one of ('z', 'y', 'x')")
          raise err.InputError('',"first_axis must be one of ('z', 'y', 'x')")

        Nm = len(markers)
        #pdb.set_trace()
        plt.plot(xx.T, yy.T, 'b')
        for it in range(Pcl.status.shape[1]):
            L = Pcl.status[:,it]>0
            if markers[it % Nm] != ' ':
                plt.plot(xx[L,it], yy[L,it], marker=markers[it % Nm], **kwargs)

        #Mark the end points with status <=0 (captured)
        L  = Pcl.status[:,-1] <= 0.
        plt.plot(xx[L,-1], yy[L, -1], 'r.' )

        #for it, m in enumerate(markers):
        #    plt.plot(xx,yy)

        #print('xx=', xx[ip, :])
        #print('yy=', yy[ip, :])
        #print()
    else:
        print("Axis should be a legal 2d or 3d axes not type {}"
                      .format(axes))


def visualize(gr, Pcl, phi=None, ugrid=False):
    """Visualize particles in the grid (3D view)

    Parameters:
    -----------
    gr : mfgrid.Grid object
    Phi: ndarray shape=(gr.Ny, gr.Nx)
        Heads in the layer that should be shown.
    Pcl : named tuple with particles in fields x, y, z
        as obtained from mfpath.particle_tracker
    ugrid : boolean
        if False the particles are shown in the regular grid
        if True they are shown in the normalized grid
    @TO 161115

    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if ugrid == False:
        gr.plot_grid3d( 'rgb', axes=ax, alpha=0.2)
        if not (phi is None) and np.std(phi) != 0.:
            ax.contour( gr.xm,  gr.ym, phi, 50)
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.set_zlabel('z [m]')
        ax.set_xlim(gr.x[[0,-1]])
        ax.set_ylim(gr.y[[0,-1]])
        ax.set_zlim([np.min(gr.Z), np.max(gr.Z)])
        plot_particles(Pcl, ugrid=ugrid, axes=ax)
    else:
        gr.plot_ugrid('rgb', axes=ax, alpha=0.2)
        ax.set_xlabel('u [-]')
        ax.set_ylabel('v [-]')
        ax.set_xlim([0, gr.Nx])
        ax.set_ylim([gr.Ny, 0])
        ax.set_zlim([gr.Nz, 0])
        plot_particles(Pcl, ugrid=ugrid, axes=ax)
    plt.show()
    return ax


def fdte(v0, a, Us,):
    """Returns time to exit from cell along axis in normal situation.

    Separately deal with normal, linear and stagating situations
    in a vectorized manner

    Parameters:
    -----------
    v0 : ndarray, upfront velocity
    a  : ndarray, "accelleration"
    Us : ndarray, local start location (between 0 and 1)
    trem: ndarray, time unitl end of simulation step

    other locals
    Ue :    ndarray, exit local coordinate (0 or 1. depending sign of v0)
    Llin  : ndarray of bool, cells with constant velocity (a=00)
    Llog  : ndarray of bool, cell with v0 != v1 and not stagnation (normal cells)
    Returns
    -------
    te : ndarray, time to exit (until hitting cell face) for each cell for current axis direction
    vUs  : ndarray, velocity at start postion (determines opposite cell face
    @TO 161027
    """
    # Velocity at starting pint and exit location based on it
    vUs = v0 + a * Us # velocity at starting location
    Ue = np.ones(a.shape);   Ue[vUs<0] = 0  # U at exit face
    vUe = v0 + a * Ue # velocity at exit face

    # Time till hitting that cell face
    te = np.zeros(a.shape)
    te[:] = np.inf # stagnating points get time is inf

    # Cells with constant velocity
    Llin = np.logical_and( a == 0., np.abs(v0) != 0) # cells with constant v
    Llog = AND(vUs * vUe > 0, NOT(Llin)) # cells with changing v without internal water divide

    # times till face
    te[Llin]  = (Ue[Llin] - Us[Llin])/v0[Llin]
    te[Llog]  = np.log( vUe[Llog] / vUs[Llog] )  /  a[Llog]

    return te


def newPos(v0, a, Us, dt):
    """ Compute new position of particle for this axis"""
    EMAX = 1e20
    EMIN = 1e-20

    vUs = v0 + a * Us # velocity at starting location
    Ue = np.ones(a.shape);   Ue[vUs<0] = 0  # U at exit face
    vUe = v0 + a * Ue # velocity at exit face

    # Cells with constant velocity
    Llin = np.logical_and( a == 0., np.abs(v0) != 0) # cells with constant v
    Llog = AND(vUs != 0, vUs != vUe, NOT(Llin)) # cells with changing v without internal water divide

    # Compute the output position after the minimum of te and trem (remaining time)

    e_ = np.fmax( EMIN, np.fmin( EMAX, np.exp(a[Llog] * dt[Llog]))) # exponent

    U = Us.copy() #  for stagated points
    U[Llin] = dt[Llin] * v0[Llin] + Us[Llin]
    U[Llog]= (v0[Llog]/a[Llog] + Us[Llog]) * e_ - v0[Llog]/a[Llog]

    vu = v0 + a * U

    return U, vu


def LOCAL(up, Nx):
    """Return local coordinates u,iy given normalized coordinate up
    """
    iu = np.fmin( np.array(up, dtype=int), Nx - 1)
    u = up - iu
    return u, iu


def particle_tracker(gr, fdm_out, por, T=100., particles=None,
                     markers='+o*.xsdph^v<>', verbose=True,
                     retardation=1.0,
                     sinkfrac=0.75, tol=1e-6,
                     central_point=(0., 0., 0.)):
    """3D particle tracker, returning (XP, YP, ZP) particle coordinates.

    To use this function:
        generate a 3D steady-state model, e.g.call function `fdm3()` in module `fdm` and use its output `fdm_out` (which contains Q, Qx, Qy, Qz) and the array `por` (effective porosity) and the other parameters to track particles. T is an array of times of which the particle positions are to be stored and returned and particles is a 3-tuple with the initial particle coordinates (Xp, Yp, Zp).
        ***Call example:**
        Pcl = particle_tracker(gr, fdm_out, por, T=100.,
                                    particles=(Xp, Yp, Zp))
    ToDo:
    -----
        + If no starting values are used you must click on an existing picture and the flow path will be immedidately drawn with markers at the points reached at the given times in array T. Markers are used in the order as specified (or defaults).
        Repeat this for more lines. Click te right hand button to stop
        + Type fdm3path for selftest and demo.
        + Add random walk.
        + Show use of simultaneous tracking of massive numbers of particles.
        + Implement use in axial symmetric mode.
        @TO 161230

    Parameters:
    -----------
    gr : mfgrid.Grid object
        gr contains the information about the finite difference grid
        For axially symmetric models set axial=True in the call to Grid
            gr = mfgrid.Grid(xGr, yGr, zGr, axial=True)
    fdm_out: named tuple, output of the 3D fintie difference model fdm.fdm3,
        containing the 3D ndarrays Q, Qx, Qy, Qz : [L3/T]
    por : np.ndarray, [- ] effective porsities
    T  : np.ndarray, [T]
        vector of times at which particle positions are desired.
        In interactive mode, a marker is placed on successive times. See markers below.
        A marker at t=0 will always be placed
            Use negative times to backward.
        A single value denotes an end time and 0 is prepended.
        If T is a vector, then T[0] is the startubg tne time of the tracking and the first marker is placed on the starting particle position.
    markers : string, [-]
        a listis of letters or stymbols denoting legal markers in matplotlib.
        These markers will be used in sequence and repeated when used up.
          e.g.   '>+o*.xsdph\^{}v<'
    verbose : bool, if True prints iteration progress
    particles : a 3 tuple of ndarray denoting starting postion of particles.
        An ndarray is also allows. Then the shape must
        be (Np, 3). If shape is (Np, 2) , then [X, Z) is assumed as for a cross section.
    retardation : float. Porosity is multiplied by retardation.
    sinkfrac : float
        criterion when particle are to be removed from sink cells.
        sinkfrac is the extraction as a fraction of the total inflow to the cell.
    tol : float
        determins what is considered to be zero, use 1e-6 for instance
    central_point : is a coordinate 3-tuple (x, y, z).
        It is sometimes useful when working with wells to compute the
        distance to this point. The computed distance is included in the particle output under variable 'r'.

    Returns:
    --------
    (XP, YP, ZP, TP, pStat) : np.ndarray, [L] and [T]
        XP, XP, ZP and TP have size(Np, Nt) where Np the number of particles
        and Nt the number of times with T[0] the starting value and XP[:,0] etc
        the inital coordinates.
        pStat is an ndarray of int showing the status of each particle at each time
            pStat = -1 : particle out of model grid
            pStat = -2 : particle caught in sink
            pStat =  0 : particle reached end time
            pStat > 0  : particle is still moving in the model

    See also:
    ---------
    fdm.fmd3, fdm.fdm3t

    TO 070424 070501 140420

    Copyright 2009-2016 Theo Olsthoorn, TU-Delft and Waternet, without any warranty
    under free software foundation GNU license version 3 or later

    Approach:
    ---------
    All computations and trackings are done in a normalized model grid. That is a grid consisting of cubes with unit sides, using relative coordinates up, vp an wp that run from 0..Nx, 0..Ny and 0..Nz. up=U+iu, where U is 0..1. and iu is integer 0..Nx-1, vp=V+iv, and wp=W+iw with W=0..1. and integer iw=0..Nz-1.
    The velocities are converted to this grid.
    This approach allows to treat all three axes in the same way, so that
    functions for can be written and applied to each axis in sequence that not have to deal with the direction of the axis in the normalized grid. It also prevents duplicating code and is less error prone.
    The code is vectorized as much as possible to allow massive numbers of points to be tracked simultaneously. This should make implementation of random walk of particles simple.
    """

    #import numpy as np
    #from collections import namedtuple
    #import pdb

    # The code is set-up to allow vectorization and thus moving large numbers of particles
    # simultaneously

    # All computations are done with the normalized grid inwhich every cell is a cube
    # of size 1x1x1 and in which ascending indices correspond to ascending axis values
    # The normalize grid has
    #     shape of normalized grid is same as original
    #     Nu=Nx, Nv=Ny, Nw=Nz
    #     x-->u, y-->v z-->w,
    #     0<=0<=Nu+1, 0 <= v <= Nv+1, 0 <= w <= Nw+1
    # conversion between coordinates see: norm2grid and grid2norm
    """Internal parameters
       ------------------
       In the real-world grid, axes direction is x aligned with column number, while y and z run opposite with column and layer numbers. In the normalized grid, u, v and w always increase with increasing column, row and layer numbers, so that coordinates 0<=up<=Nx, 0<=vp<=Ny, and 0<=wp<=Nz for points inside the grid.

       Nu, Nv, Nw = gr.Nx, gr.Ny, gr.Nz
       tNext = T[it], it = current time target index
           Cell based parameters:
           -----------
           vc_u0, vc_u1 : normalized velocities in cell in u-direction
           vc_v0, vc_v1 : in v-direction (y)
           vc_w0, vc_w1 : in w-direction (z)
           au, av, aw : "accelleration (vc_u1-vc_u0) for u-direction etc.
           Ue, Ve, We : exit locations in local coordinates 0<Ue<1, 1.0 if vc0_u1>0 else 0.0, etc.
           dUe, dVe, dWe : local coordinate oupdate when paricle leaves cell  1 v<0 else  0
           diu, div, diw : cell index update when particle leaves in direction -1 if <0 else +1
           NOD : ndarray of int, global cell indices
           Vcell : ndarray, cell volume times effecitve porosity times retardation
           Particle base:
           --------------
           Xp, Yp, Zp   : grid coordinates of particles:
                               gr.x[0]<Xp<gr.x[-1]
                               gr.y[0]>Yp>gr.y[-1]
                               gr.z[0]>Zp>gr.z[-1] # z varies per cell
           up, vp, wp   : normalized grid coordinaes: 0<up<Nu+1, 0<vp<Nv+1, 0<wp<Nw+1
           u_, v_, w_   : up[:,it], vp[:,it], wp[:,it] for convenience
           iup, ivp, iwp: grid cell of particle = np.array(np.floor(up), dtype=int) etc.
           U, V, W      : local grid coordinates U=up-iu, V=vp-iv, V=wp-iw, all 0<=U<=1 etc.
           IC : ndarray with dtype=int, contains cell indices for particles (where they currently are)
           Ic : ndarray of dtype=int, cell indices of only the considered (moving) particles, to select cell info
           Lp : ndarray of dtype=bool, indices of moving particles in the particle array, to select particles not cells
                   lenght of Ic and Lp must alows be the same, as the same particles are targeted.
           Dte : (Np, 4) time until particle exits cell, column 4 = tNext
           dte : minumum time until particle hits any of its current cell faces
           Ie : index Te, axis=1, showing which column (direction) has min time (knnow where paticle goes next)
           Lstag_u : ndarray of bool, tells whether vu is zero within cell, etc. for vv and vw
           Llin_u : ndarray of bool, tells whether vu is constant in cell, etc. for vv and vw
           Llog_u : ndarray of bool, tells whether vu varies and log function is applicable, etc voor vv and vw

    """
    # Constants for particle status
    ACTIVE = 1
    INACTIVE = 0
    CAPTURED = -1
    OUT = -2

    Nv, Nu, Nw = gr.shape

    # For rounding near edges and telling whether v = constant
    digits = int(abs(np.log10(tol)))

    _, Q, Qx, Qy, Qz, *rest = fdm_out

    # Assert correct shapes of input arrays:
    if Q.shape != gr.shape:
        raise err.InputError("","Shape of Q {0} must equal {1}".
                             format(repr(Q.shape), repr((Nv, Nu, Nw)))
                             )
    if Qx.shape != (Nv, Nu-1, Nw):
        raise err.InputError("","Shape of Qx {0} must equal {1}".
                             format(repr(Qz.shape), repr((Nv, Nu-1, Nw)))\
                            )
    if Qy.shape != (Nv-1, Nu, Nw):
        raise err.InputError("","Shape of Qy {0} must equal {1}".
                             format(repr(Qy.shape), repr((Nv-1, Nu, Nw)))
                            )
    if Qz.shape != (Nv, Nu, Nw-1):
        raise err.InputError("","shape of Qz {0} must equals {1}".
                             format(repr(Qz.shape), repr((Nv, Nu, Nw-1)))
                            )
    por = np.array(por)
    if por.shape != (Nv, Nu, Nw):
        raise err.InputError("","shape of por {0} must equal {1}".
                             format(repr(por.shape), repr((Nv, Nu, Nw)))
                            )

    if particles is None:
        raise err.InputError("",
            "Interactive particle input not yet implemented, use array of Npx3 x,y,z points")
    if isinstance(particles, np.ndarray):
        if particles.shape[1] != 2 and particles.shape[1] != 3:
            raise err.InputError("","A particle array must have shape (Np, 2) or (Np, 3),\n\
                    that is: [Xp, Zp] or [Xp, Yp, Zp]")
        if particles.shape[1] == 2:
            # Assume x and z are given, add zeros for y
            Xp = particles[:,0]
            Yp = np.zeros(Xp.shape)
            Zp = particles[:,1]
        else:
            Xp = particles[:,0]
            Yp = particles[:,1]
            Zp = particles[:,2]
            particles = np.hstack((particles[:,0], np.zeros(particles[:,0].shape), particles[:,-1]))
    elif isinstance(particles, (tuple, list)):
        if not (len(particles) == 2 or len(particles) == 3):
            raise err.InputError("","A particles tuple or list must consist of (Xp, Zp) or (Xp, Yp, Zp)")
        if len(particles) == 2:
            Xp = particles[0]
            Yp = np.zeros(Xp.shape)
            Zp = particles[1]
        else:
            Xp = particles[0]
            Yp = particles[1]
            Zp = particles[2]
    else:
        raise err.IntputError("","Particles must be an ndarray, a tuple or a list\n\
            holding [Xp,Zp] or [Xp,Yp,Zp] particle coordinates")
    if len(Xp) != len(Yp) or len(Xp) != len(Zp):
        raise err.InputError("",
                    "length of particle coordinates Xp, Yp, and Zp must be the same.")

    # check for NaNs in intput coordinates
    if any(np.isnan(Xp * Xp * Zp)):
        print("particles coordinates may not contain NaNs, {} NaNs found".
                  format(np.sum(np.isnan(Xp *Yp *Zp))))
        raise ValueError()

    # make sure T has at least two times, add 0. if only onte time is given
    if len(T)<2:
        T = np.array([0., T])

    # Set-up info for cells =========================================

    # cell volume, multiplied by retardation, to tacke linear sorption
    Vcells = gr.Volume * por * retardation

    # initialize velocities at cell faces
    shp = gr.shape
    vc_u0 = np.zeros(shp)
    vc_u1 = np.zeros(shp)
    vc_v0 = np.zeros(shp)
    vc_v1 = np.zeros(shp)
    vc_w0 = np.zeros(shp)
    vc_w1 = np.zeros(shp)
    # ToDo: check that these variables get their own copy, not refs to the same array

    forward = (T[-1]>T[0])
    print('Forward tracking, because T is ascending')

    # Set velocities at cell faces and  ...
    #   take sign of Q into consideration (to align
    #   v with ascending axies in normalized grid
    vc_u0[:, 1:,:] = np.round( Qx * forward / Vcells[:, 1:,:], decimals=digits)
    vc_u1[:,:-1,:] = np.round( Qx * forward / Vcells[:,:-1,:], decimals=digits)
    vc_v0[ 1:,:,:] = np.round(-Qy * forward / Vcells[ 1:,:,:], decimals=digits)
    vc_v1[:-1,:,:] = np.round(-Qy * forward / Vcells[:-1,:,:], decimals=digits)
    vc_w0[:,:, 1:] = np.round(-Qz * forward / Vcells[:,:, 1:], decimals=digits)
    vc_w1[:,:,:-1] = np.round(-Qz * forward / Vcells[:,:,:-1], decimals=digits)

    # Only vectors needed for effecive indexiing
    vc_u0 = vc_u0.ravel()
    vc_u1 = vc_u1.ravel()
    vc_v0 = vc_v0.ravel()
    vc_v1 = vc_v1.ravel()
    vc_w0 = vc_w0.ravel()
    vc_w1 = vc_w1.ravel()

    # "accelerations", round, so that comparison with zero makes sense
    au = np.round(vc_u1 - vc_u0, decimals=digits)
    av = np.round(vc_v1 - vc_v0, decimals=digits)
    aw = np.round(vc_w1 - vc_w0, decimals=digits)

    # Boolean arrays to select the correct time and postion functions
    # Constant velocity in these cells:

    # Set-up information for the particles ===================================

    # Number of particles and number of time steps:
    T = T if len(T)>1 else np.array([0.0, T])
    Nt = len(T)
    Np = len(Xp)

    up, vp, wp  =\
             gr.xyz2uvw(Xp, Yp, Zp)  # relative w coordinates

    SETUP = lambda r: np.hstack(( r.reshape(Np, 1), np.zeros((Np, Nt - 1), r.dtype)))

    # Initialize pparticle output arrays
    Xp, Yp, Zp = SETUP(Xp), SETUP(Yp), SETUP(Zp)
    Up, Vp, Wp = SETUP(up), SETUP(vp), SETUP(wp)
    Tp = SETUP( np.ones((Np, 1)) * T[0])

    # initialize status to inactive
    STAT = SETUP( np.ones(Np, dtype=int) * ACTIVE)

    Lp = gr.inside(Xp[:,0], Yp[:,0], Zp[:,0])
    L_out = NOT(Lp)
    STAT[  gr.inside(Xp[L_out,0], Yp[L_out,0], Zp[L_out,0]), 0] = OUT

    # Get indices of active particle cellss to store them in Ix, Iy, Iz
    _, iu = LOCAL( Up[Lp, 0], gr.Nx)
    _, iv = LOCAL( Vp[Lp, 0], gr.Ny)
    _, iw = LOCAL( Wp[Lp, 0], gr.Nz)

    # Initialize active point cell indices
    intNaNs = mfgrid.intNaN * np.ones(Np, dtype=int)  # intNan if out of grid
    Ix, Iy, Iz = SETUP(intNaNs), SETUP(intNaNs), SETUP(intNaNs) # generate arrays
    Ix[Lp, 0], Iy[Lp, 0], Iz[Lp, 0] = iu, iv, iw # fill in for it==0

    IC = np.zeros(Ix.shape) + mfgrid.intNaN

    # Global cell numbers of active particles
    Ic = gr.ixyz2global_index(Ix[Lp, 0], Iy[Lp, 0], Iz[Lp, 0])
    IC[Lp, 0] = Ic
    # Eliminate particles that are in sink cells.
    Isink = isSink(Q, Qx, Qy, Qz, sinkfrac).ravel() # sink cells array
    STAT[Isink[Ic], 0] = CAPTURED

    # Update active cells
    Lp = (STAT[:,0] == ACTIVE)
    Ic = gr.ixyz2global_index(Ix[Lp, 0], Iy[Lp, 0], Iz[Lp, 0])

    # Coninue with only the active coordinates.
    u, iu = LOCAL( Up[Lp, 0], gr.Nx)
    v, iv = LOCAL( Vp[Lp, 0], gr.Ny)
    w, iw = LOCAL( Wp[Lp, 0], gr.Nz)

    # Global active particle cell number (changes when iu, iv, iw are updated)
    Ic = gr.ixyz2global_index(Ix[Lp, 0], Iy[Lp, 0], Iz[Lp, 0])
    #Ic = iv * Nu * Nw + iu * Nw + iw

    # Compute initial velocities.(Set dt=0 to with initial positions)
    dt = np.zeros(Ic.shape)

    _, vu = newPos(vc_u0[Ic], au[Ic], u, dt)
    _, vv = newPos(vc_v0[Ic], av[Ic], v, dt)
    _, vw = newPos(vc_w0[Ic], aw[Ic], w, dt)

    # Store initiaal velocities
    floatNaNs = np.NaN * np.ones(Np, dtype=float)
    Vu, Vv, Vw = SETUP(floatNaNs), SETUP(floatNaNs), SETUP(floatNaNs)
    Vu[Lp, 0], Vv[Lp, 0], Vw[Lp, 0] = vu, vv, vw
    Vx, Vy, Vz = SETUP(floatNaNs), SETUP(floatNaNs), SETUP(floatNaNs)
    Vx[Lp, 0], Vy[Lp, 0], Vz[Lp, 0] =\
                     vu * gr.DX.ravel()[Ic],\
                     vv * gr.DY.ravel()[Ic],\
                     vw * gr.DZ.ravel()[Ic]

    # Allocate array Npx4 to store cell face hitting times
    Dte    = np.zeros((Np, 4), dtype=float) # time to hit face

    # Are there any points to track ?? If not quit.
    if not np.any(STAT[:, 0] == ACTIVE):
        print("No points to track.\n\
              Remedy:\n\
                  See that there are points inside the grid.")
        raise ValueError()

    # Track all active particles simultaneously on a time step basis.
    for it, tNext in enumerate(T):

        if it==0:
            # Initial values, all set above.
            continue

        #Transfer data from previous time to this one.
        TRANSFER(it,\
            STAT, Tp, Xp, Yp, Zp, Up, Vp, Wp, Ix, Iy, Iz, Vu, Vv, Vw)

        Lp = (STAT[:, it] == ACTIVE)
        Ic = gr.ixyz2global_index(Ix[Lp, it], Iy[Lp, it], Iz[Lp, it])
        Ip = INDICES(Lp)

        tRem = np.ones(len(Ip), dtype=float) * (tNext - T[it - 1])

        """Before any time step: update local info.

        Locals are in lower case.
        Globals are in upper case.
        """
        up, vp, wp = Up[Lp, it], Vp[Lp, it], Wp[Lp, it]

        u, iu = LOCAL(up, gr.Nx)
        v, iv = LOCAL(vp, gr.Ny)
        w, iw = LOCAL(wp, gr.Nz)

        # track till next time ##############################################
        """Inner loop, running one time step iteratively.
        Here we simulate all still active particles during one time step.

        Its ready when all particles arrive or are captured or are stagnant.
        While we remove captured and stagnant particles on our way and
        also remove all partilcles that have arrived at the end of this time
        step. We check whether there are still particles underway, i.e.
        active and not yet reached the end of the current time stp

        We use a for-loop to prevent endless looping and break out when done
        """

        MAXITER = 500
        iter_ = 0
        for iter in range(MAXITER):  # no more references to the past

            iter_ += 1
            # exit times from current cells
            #   dt, vStart =  fdte(v0       , a,      Ustart)
            Dte[Lp, 0] = fdte(vc_u0[Ic], au[Ic], u)
            Dte[Lp, 1] = fdte(vc_v0[Ic], av[Ic], v)
            Dte[Lp, 2] = fdte(vc_w0[Ic], aw[Ic], w)
            Dte[Lp, 3] = tRem

            # The true exit time is the minimum of these 4 times in Dte
            # time along u, v, and w plus trem = 4 times
            dte = np.min(   Dte[Lp], axis=1) # shortest time
            Ie  = np.argmin(Dte[Lp], axis=1) # which side or none

            # Update local coords upon crossing cell face given shortest time
            # vu, vv, vw are velocities at starting locations. We need
            # there signs se to determine at which side the particle could
            # hit cell face. Linear versus varying velocities in cells is
            # handled in function fdte which computes the time till hitting
            # the next cell face in the respective direction.
            u, vu = newPos(vc_u0[Ic], au[Ic], u, dte)
            v, vv = newPos(vc_v0[Ic], av[Ic], v, dte)
            w, vw = newPos(vc_w0[Ic], aw[Ic], w, dte)

            # Updat the current times of the particles
            tRem    -= dte            # until tNext

            # Determine at which side particle leaves cell if at all
            # West, East, North, South, Top, Bottom, depending on
            # which face wat hit, update U and iup
            W_ = AND(Ie == 0, vu < 0) # leaves through west cell face ?
            E_ = AND(Ie == 0, vu > 0) # leaves eastward
            N_ = AND(Ie == 1, vv < 0) # leaves northward
            S_ = AND(Ie == 1, vv > 0) # southward
            T_ = AND(Ie == 2, vw < 0) # leaves upward throug top of cell
            B_ = AND(Ie == 2, vw > 0) # leaves downward through bottom

            # update local coordinate and cell index of particles that
            # hit a cell face and move into adjacent cell
            u[W_] = 1;    iu[W_] -= 1
            u[E_] = 0;    iu[E_] += 1
            v[N_] = 1;    iv[N_] -= 1
            v[S_] = 0;    iv[S_] += 1
            w[T_] = 1;    iw[T_] -= 1
            w[B_] = 0;    iw[B_] += 1

            # Update normalized coordinates

            up = u + iu
            vp = v + iv
            wp = w + iw

            # Update global cell index of particles, because iu, iv and iw changed
            Ic = gr.ixyz2global_index(iu, iv, iw)
            IC[Lp, it] = Ic

            ###################################################################
            """Finish off this iteration by:
                updating the status of
                updating the global postion of the particles
                updating the list of remaining particles

            """
            # First store the current time of the current particles
            Tp[Ip, it] = tNext - tRem

            # Then store location of all current particles
            Up[Ip, it], Vp[Ip, it], Wp[Ip, it] = up, vp, wp
            Xp[Ip, it], Yp[Ip, it], Zp[Ip, it] = gr.uvw2xyz(up, vp, wp)
            Vu[Ip, it], Vv[Ip, it], Vw[Ip, it] = vu, vv, vw
            Vx[Ip, it], Vy[Ip, it], Vz[Ip, it] = vu * gr.DX.ravel()[Ic],\
                                                 vv * gr.DY.ravel()[Ic],\
                                                 vw * gr.DZ.ravel()[Ic]
            Ix[Ip, it], Iy[Ip, it], Iz[Ip, it] = iu, iv,  iw

            # Update status of curreen particles
            # Which of the current particles became captured ?
            gone1 = Isink[Ic]

            # Which of the current particles that are now in stagnation zone ??
            gone2 = AND( vu == 0., vv == 0., vw == 0. )

            STAT[Ip[gone1], it] = CAPTURED
            STAT[Ip[gone2], it] = INACTIVE
            gone = OR(gone1, gone2)

            # See which of the current particles are still moving to reach tNext
            rest = AND (NOT( gone ), tRem > 0. )

            if NOT (np.any( rest )):
                if verbose:
                    """ All particles have been eliminated or arrived at\n\
                    at end of time step'
                    """
                    print("all particles arrived at time step {0}, after {1} iteratons".\
                          format(it, iter_))
                break
            else:
                # Update the set of current particles
                up, vp, wp = up[rest], vp[rest], wp[rest]
                u,   v,  w = u[ rest], v[ rest], w[ rest]
                iu, iv, iw = iu[rest], iv[rest], iw[rest]

                tRem = tRem[rest]

                # update remaining particle indices
                Lp[ Ip[ NOT( rest ) ] ] = False
                Ip = Ip[rest]
                Ic = Ic[rest]


        # after every time step
        # Update global arrays
        # Check if all particles are captured
        pass

    ###########################################################################
    """Round off
    Simulation done, rounding of with summarizing the result to the user.

    """
    Nact   = np.sum(STAT[:, it] == ACTIVE)
    Ncap   = np.sum(STAT[:, it] == CAPTURED)
    Nstag  = np.sum(STAT[:, it] == INACTIVE)

    # average arrival time
    Tavg = np.mean(STAT[:, it] == ACTIVE)

    s =\
    "Job done, {0} particles tracked for time  from t={1} to t={2} in {3}time steps.\n\
    The results are in variable Pcl (a 'named_tuple 'Pcl'.\n\
    whose importnat fields are Status, X, Y, Z, T, up, vp, wp.\n\
    At the and there were:\n\
    {4} particles still active\n\
    {5} particles captured by sinks\n\
    {6} particles stagnant\n\
    The average arrival time of the captured particles is {7}\n\
    \n"
    print(s.format(Np, T[0], T[-1], len(T)-1, \
                   Nact, Ncap, Nstag, Tavg))

    #construct output named tuple
    Pcl= namedtuple('Particles',
            ['status','grid','t',
                 'x', 'y', 'z', 'vx','vy','vz',
                 'u', 'v', 'w', 'vu','vv','vw',
                 'ix', 'iy', 'iz', 'ic', 'r'])
    Pcl.__doc__ = \
        """Output of particle tracker
        t = time, ndarray shape (Np,Nt)
            T is kept at time that status of particle becomes less than zero
        status = ndarray of int, shape (Np,Nt)
            -2: particle outside model (OUTSIDE)
            -1: particle captured by sink (CAPTURED)
             0: particle stagged in stagnation point (INACTIVE)
             1: partbicle moving through model grid (ACTIVE)
        grid : mfgrid.Grid object, holding the original grid
        ix, iy, iz : grid cell id's of particles
        x,   y,  z : ndarray, coordinates shape (Np,Nt)
        vx, by, vz : ndarray, particle velocity (Np,Nt)
        u,   v,  w  : ndarray, normalized coordinates (Np, Nt)
        vu, vv, vw : ndarray, velocities in normalized grid (Np, Nt)
        'r' : dummy, which may be used to store a distance
        """
    x0, y0, z0 = central_point

    r = np.sqrt((Xp-x0)**2 + (Yp-y0)**2 + (Zp-z0)**2) # dummy distance

    pcl = Pcl(STAT, gr, Tp,\
              Xp, Yp, Zp, Vx, Vy, Vz,\
              Up, Vp, Wp, Vu, Vv, Vw,\
              Ix, Iy, Iz, IC, r )  # instantiate

    return pcl
    ###########################################################################

# 1D travel times, for comparison with mfpath results
def normGrid(gr):
    up = np.arange(0., gr.Nx+1)
    vp = np.arange(0., gr.Ny+1)
    wp = np.arange(0., gr.Nz+1)
    return mfgrid.Grid(up, vp, wp)

def travel_time_x(gr, x, phi, k, por, R=1.):
    # T = L1 L eps R / (k dh)
    h0 = np.mean(phi[:, 0,:])
    h1 = np.mean(phi[:,-1,:])
    L  = gr.xm[-1] - gr.xm[0]
    i  = (h0-h1)/L
    if i>0:
        T = por * R * (x[:,-1] - x[:, 0]) / (k * i)
    else:
        T = por * R * (x[:,-1] - x[:, 0]) / (k * i)
    return T

def travel_time_y(gr, y, phi, k, por, R=1.):
    # T = L1 L eps R / (k dh)
    h0 = np.mean(phi[-1,:,:])
    h1 = np.mean(phi[ 0,:,:])
    L  = gr.ym[0] - gr.ym[-1]
    i  = (h0 -h1) / L
    if i>0:
        T =  por * R * (y[:,-1] - y[:,0]) / (k * i)
    else:
        T =  por * R * (y[:,-1] - y[:,0]) / (k * i)
    return T

def travel_time_z(gr, z, phi, k, por, R=1.):
    # T = L1 L eps R / (k dh)
    if gr.full == False:
        h0 = np.mean(phi[:,:,-1])
        h1 = np.mean(phi[:,:, 0])
        L   = gr.zm[0] - gr.zm[-1]
        i   = (h0 - h1) / L
        if i>0:
            T =  por * R * (z[:,-1] - z[:, 0]) / (k * i)
        else:
            T =  por * R * (z[:,-1] - z[:, 0]) / (k * i)
    else:
        return np.zeros(z[:,0].shape) * np.NaN
    return T


def setupAndRunFDM_model(gridpar, k, hbound):

    Lx, wx, Ly, wy, D, d = gridpar
    hW, hE, hN, hS, hT, hB = hbound

    x = np.linspace(-Lx, Lx, int(2 * Lx / wx) + 1)
    y = np.linspace(-Ly, Ly, int(2 * Ly / wy) + 1)
    z = np.linspace(0, -D, int(D /d) + 1)
    gr = mfgrid.Grid(x, y, z)

    K = gr.const(k) # * np.random.rand(gr.Nod).reshape(gr.shape)
    FH = gr.const(0.)
    FQ = gr.const(0.)

    IBOUND = gr.const(1)

    if not (hW is None):
        IBOUND[:, 0, :] = -1
        FH[:, 0, :] = hW
    if not hE is None:
        IBOUND[:, -1, :] = -1
        FH[:, -1, :] = hE
    if not hN is None:
        IBOUND[0, :, :] = -1
        FH[0, :, :] =  hN
    if not hS is None:
        IBOUND[-1, :, :] = -1
        FH[-1, :, :] = hS
    if not hT is None:
        IBOUND[:, :, 0] = -1
        FH[:, :, 0] = hT
    if not hB is None:
        IBOUND[:, :, -1] = -1
        FH[:, :, -1] = hB

    # Solve for the heads:
    Out = fdm.fdm3(gr, (K, K, K), FQ, FH, IBOUND)

    return Out, gr, IBOUND


if __name__ == '__main__':
    """
    Test example:
    ga heen en weer tussen norm points and grid points
    zie lijst in schrift
    checkd dat voor 5 punten het werkt
    van oost naar west
        verblijftijd met de hand of in python uitgerekend ter verificatie
        T = (X - X[0]) / (K * gr.dx/np.mean(Out.Phi[:,-1,:] - Out.Phi[:,0,:]) * eps * R)
    van west naar oost
    van noord naar zuid
    van top naar bottom
    van bottom naar top
    met willekeurige randvoorwaarden
    met willekeurige k-waarden

    zelfde als punten op de grid lijnen liggen
    zelfde als de punten in de cell hoeken liggen
    zelfs als de punten op de rand van de buitenste cellen en in de
    hoeken van het model liggen,
    zelfde wanner de punten in sinks liggen
    zelfde wanneer de punten in stagnatiezones liggen.
    """

    print("I'm Testing the code.")
    print("Setting up the test.")

        # Parameters to set up a grid for the model
    #          Lx    wx     Ly     wy    D     d
    gridpar= (1000., 100., 1000., 100., 100., 10.)

    k = 10.

    #  FH  @   N     S    W   E    T     B
    hbound= (None, None, None, -5., 0., None)

        # run fdm model
    fdm_out, gr, IBOUND = setupAndRunFDM_model(gridpar, k, hbound)

    # The x,y and z of the particles are computed vorm u, v and w norm.coords.
    Np = 25
    up = np.random.rand(Np) * gr.Nx
    vp = np.random.rand(Np) * gr.Ny
    wp = np.random.rand(Np) * gr.Nz
    xp, yp, zp = gr.uvw2xyz(up, vp, wp)

    # Times
    T = np.arange(0., 36000., 360.)

    peff = gr.const(0.35)

    # Track particles
    Pcl = particle_tracker(gr, fdm_out, T, (xp, yp, zp))


    visualize(gr, Pcl, ugrid=False, phi=fdm_out.Phi[:,:,0])
    visualize(gr, Pcl, ugrid=True)

    print('Finished')
    pdb.set_trace()

    # -- plot a 3D network and the partciles in it
