#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for mfgrid

Created on Mon Nov  7 10:25:48 2016

@author: Theo
"""

import sys

myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules/'

if not myModules in sys.path:
    sys.path.insert(0, myModules)

import numpy as np
import pdb
import unittest
import mfgrid

#import matplotlib.pylab as plt

def AND(*args):
    L = args[0]
    for arg in args:
        L = np.logical_and(L, arg)
    return L

NOT = np.logical_not

class MfgridTests(unittest.TestCase):




    def setUp(self):
        global gr, grn, tol, xTest, yTest,\
            xp, yp, zp, xpm, ypm, zpm,\
            up, vp, wp, upm, vpm, wpm,\
            U, iu, V, iv, W, iw, mustSkip


        mustSkip = False
        tol = 1e-5
        digits = int(abs(np.log10(tol)))

        x = np.array([0, 6, 3.000001, -2, -1e-6, 3e-6, 4.00001, 7, 8, 11, -3, -4])
        y = x[:]

        xTest = np.unique(np.round(x, digits))
        yTest = xTest[::-1]

        Nx = len(np.unique(np.round(np.array(x), digits))) - 1
        Ny = len(np.unique(np.round(np.array(y), digits))) - 1


        # Generate a full fledged Z array with different Z in ever iy,ix
        # combination
        z = np.arange(5) * -10
        Z = np.ones((Ny, Nx, 1)) * z.reshape((1, 1, len(z)))
        Z = Z * (np.random.rand(len(z)) + 0.5).reshape((1, 1, len(z)))

        min_dz = 0.1
        gr = mfgrid.Grid(x, y, Z, min_dz=min_dz, tol=tol)

        Nz = gr.Nz

        grn = gr.norm_grid()

        Lam = lambda a,b : np.hstack((np.array(a), np.array(b)))

        """
        # Generate trial points that include all special cases like
        # points outside the model, points at grid lines and points
        # at the boundary edges of the model, next to ordinary
        # points falling within model cells.
        """

        # outside and inside the model
        up = np.array([]); vp = np.array([]); wp = np.array([])

        up = Lam(up, -0.5 + np.array([0., 1., 0., 0., 1., 1., 0., 1.]))
        vp = Lam(vp, -0.5 + np.array([0., 0., 1., 0., 1., 0., 1., 1.]))
        wp = Lam(wp, -0.5 + np.array([0., 0., 0., 1., 0., 1., 1., 1.]))

        up = Lam(up, Nx - 0.5 + np.array([0., 1., 0., 0., 1., 1., 0., 1.]))
        vp = Lam(vp, Ny - 0.5 + np.array([0., 0., 1., 0., 1., 0., 1., 1.]))
        wp = Lam(wp, Nz - 0.5 + np.array([0., 0., 0., 1., 0., 1., 1., 1.]))

        # points on grid lines, including all corner cases
        up = Lam(up, [0., 1., 0., 0., 1., 1., 0., 1.])
        vp = Lam(vp, [0., 0., 1., 0., 1., 0., 1., 1.])
        wp = Lam(wp, [0., 0., 0., 1., 0., 1., 1., 1.])

        up = Lam(up, Nx - np.array([0., 1., 0., 0., 1., 1., 0., 1.]))
        vp = Lam(vp, Ny - np.array([0., 0., 1., 0., 1., 0., 1., 1.]))
        wp = Lam(wp, Nz - np.array([0., 0., 0., 1., 0., 1., 1., 1.]))

        # not at grid lines, i.e. ordinary points
        up = Lam(up, np.pi/10. * Nx + np.array([0., 1., 0., 0., 1., 1., 0., 1.]))
        vp = Lam(vp, np.pi/10. * Ny + np.array([0., 0., 1., 0., 1., 0., 1., 1.]))
        wp = Lam(wp, np.pi/10. * Nz + np.array([0., 0., 0., 1., 0., 1., 1., 1.]))

        # convert these ponts to grid coordinates
        xp, yp, zp = gr.uvw2xyz(up, vp, wp)
        # verify by showing the location of these points in the two grids

        U, iu = gr.U(xp)
        V, iv = gr.V(yp)
        W, iw = gr.W(xp, yp, zp)
        up = gr.up(xp)
        vp = gr.vp(yp)
        wp = gr.wp(xp, yp, zp)

    def test_x_tol(self):
        self.assertTrue(np.all(xTest == gr.x))
    def test_y_tol(self):
        self.assertTrue(np.all(yTest == gr.y))
    def test_xdir(self):
        self.assertTrue(gr.x[-1]>gr.x[0])
    def test_ydir(self):
        self.assertTrue(gr.y[-1]<gr.y[0])
    def test_zdir(self):
        self.assertTrue(np.all(gr.Z[:,:,-1]<gr.Z[:,:,0]))
    def test_full(self):
        self.assertTrue(gr.full == np.all(gr._Z.shape == (gr.Ny, gr.Nx, gr.Nz+1)))
    def test_shape(self):
        self.assertTrue(np.all(gr.shape == (gr.Ny, gr.Nx, gr.Nz)))
    def test_dx_tol(self):
        self.assertTrue(np.all(gr.dx>=tol))
    def test_dy_tol(self):
        self.assertTrue(np.all(gr.dy>=tol))
    def test_Dx_tol(self):
        self.assertTrue(np.all(gr.Dx>=tol) and
                        np.all(gr.Dx.shape == (gr.Ny, gr.Nx)))
    def test_Dy_tol(self):
        self.assertTrue(np.all(gr.Dy>=tol) and
                        np.all(gr.Dy.shape == (gr.Ny, gr.Nx)))
    def test_DX_tol(self):
        self.assertTrue(np.all(gr.DX>=tol) and
                        np.all(gr.DX.shape == gr.shape))
    def test_DY_tol(self):
        self.assertTrue(np.all(gr.DY>=tol) and
                        np.all(gr.DY.shape == gr.shape))
    def test_dz_min(self):
        self.assertTrue(np.all(gr.DZ>=gr.min_dz) and
                        np.all(gr.DZ.shape == gr.shape))
    def test_Area(self):
        self.assertTrue((np.round(np.sum(gr.Area), gr._digits) ==\
                        np.round(gr.area, gr._digits)) and
                        np.all(gr.Area.shape == (gr.Ny, gr.Nx)))
    def test_area(self):
        self.assertTrue(np.round(gr.area, gr._digits) == \
               np.round((gr.x[-1] - gr.x[0]) * (gr.y[0] - gr.y[-1]), gr._digits))
    def test_Volume(self):
        self.assertTrue(np.round(gr.volume, gr._digits) ==
                        np.round(np.sum(gr.DX * gr.DY * gr.DZ), gr._digits))
    def test_volume(self):
        self.assertTrue(np.round(gr.volume, gr._digits) ==
                        np.round(np.sum(gr.Volume), gr._digits))
    def test_Xm(self):
        self.assertTrue(np.all(gr.Xm == gr.xm.reshape((1, gr.Nx)) *
                        np.ones((gr.Ny, gr.Nx))))
    def test_Ym(self):
        self.assertTrue(np.all(gr.Ym == gr.ym.reshape((gr.Ny, 1)) *
                        np.ones((gr.Ny, gr.Nx))))
    def test_XM(self):
        self.assertTrue(np.all(gr.XM == gr.xm.reshape((1, gr.Nx, 1)) *
                        np.ones(gr.shape)))
    def test_YM(self):
        self.assertTrue(np.all(gr.YM == gr.ym.reshape((gr.Ny, 1, 1)) *
                        np.ones(gr.shape)))
    def test_ZM(self):
        self.assertTrue(np.all(gr.ZM == 0.5*(gr.Z[:,:,:-1] + gr.Z[:,:,1:])))
    def test_ZT(self):
        self.assertTrue(np.all(gr.ZT - gr.ZB == gr.DZ))
    def test_ix_first(self):
        self.assertTrue(gr.ix(gr.x[0]) == 0)
    def test_ix_last(self):
        self.assertTrue(gr.ix(gr.x[-1]) == gr.Nx - 1)
    def test_ixm_first(self):
        self.assertTrue(gr.ix(gr.xm[0]) == 0)
    def test_ixm_last(self):
        self.assertTrue(gr.ix(gr.xm[-1]) == gr.Nx - 1)
    def test_ix_gridline(self):
        "The point gr.x[-1] falls in cell Nx-1"
        self.assertTrue(np.all(gr.ix(gr.x) ==\
                    np.hstack((np.arange(gr.Nx), gr.Nx-1))))
    def test_ix_no_gridline(self):
        self.assertTrue(np.all(gr.ix(gr.xm) == np.arange(gr.Nx)))
    def test_iy_first(self):
        self.assertTrue(gr.iy(gr.y[0]) == 0)
    def test_iy_last(self):
        self.assertTrue(gr.iy(gr.y[-1]) == gr.Ny - 1)
    def test_iym_first(self):
        self.assertTrue(gr.iy(gr.ym[0]) == 0)
    def test_iym_last(self):
        self.assertTrue(gr.iy(gr.ym[-1]) == gr.Ny - 1)
    def test_iy_on_gridline(self):
        self.assertTrue(np.all( gr.iy(gr.y) == \
                        np.hstack((np.arange(gr.Ny), gr.Ny-1))))
    def test_iy_not_on_gridline(self):
        self.assertTrue(np.all(gr.iy(gr.ym) == np.arange(gr.Ny)))
    def test_xc_first(self):
        self.assertTrue(gr.xc[0] == gr.x[0])
    def test_xc_last(self):
        self.assertTrue(gr.xc[-1] == gr.x[-1])
    def test_yc_first(self):
        self.assertTrue(gr.yc[0] == gr.y[0])
    def test_yc_last(self):
        self.assertTrue(gr.yc[-1] == gr.y[-1])
    def test_xp_first(self):
        self.assertTrue(gr.xp[0] == gr.x[1])
    def test_xp_last(self):
        self.assertTrue(gr.xp[-1] == gr.x[-2])
    def test_ixyz_first_top(self):
        self.assertTrue(np.all(gr.ixyz(gr.x[0], gr.y[0],
                gr.Z[0, 0, 0]) == (0, 0, 0)))
    def test_ixyz_last_top(self):
        self.assertTrue(np.all(gr.ixyz(gr.x[-1], gr.y[-1],
                gr.Z[-1, -1, 0]) == (gr.Nx-1, gr.Ny-1, 0)))
    def test_ixyz_last_bot(self):
        self.assertTrue(np.all(gr.ixyz(gr.x[-1], gr.y[-1],
                gr.Z[-1, -1, -1]) == (gr.Nx - 1, gr.Ny - 1, gr.Nz - 1)))
    def test_grn_shape(self):
        self.assertTrue(np.all(grn.shape == gr.shape))
    def test_grn_x(self):
        self.assertTrue(np.all(grn.x == np.arange(gr.Nx+1, dtype=float)))
    def test_grn_y(self):
        self.assertTrue(np.all(grn.y == np.arange(gr.Ny,-1,-1, dtype=float)))
    def test_grn_z(self):
        self.assertTrue(np.all(grn.z == np.arange(gr.Nz,-1,-1, dtype=float)))
    def test_grn_Z(self):
        self.assertTrue(np.all(grn.Z == np.arange(gr.Nz,-1,-1, dtype=float).\
                reshape((1, 1, gr.Nz+1)) * np.ones((grn.Ny, grn.Nx, grn.Nz+1))))
    def test_grn_full(self):
        self.assertTrue(grn.full == False and gr.full == True)
    def test_gr_z(self):
        self.assertTrue(np.all(gr.z == np.mean(np.mean(gr.Z, axis=0), axis=0)))
    def test_up(self):
        U, iu = gr.U(gr.xm)
        up = gr.up(gr.xm)
        self.assertTrue(
            np.all(np.round(up, gr._digits) == np.round(U + iu, gr._digits)))
    def test_vp(self):
        V, iv = gr.V(gr.ym)
        vp = gr.vp(gr.ym)
        self.assertTrue(\
             np.all(np.round(vp, gr._digits) == np.round(V + iv, gr._digits)))
    def test_gr_up(self):
        self.assertTrue(np.all(grn.x == gr.up(gr.x)))
    def test_gr_vp(self):
        self.assertTrue(np.all(grn.y[::-1] == gr.vp(gr.y)))
    def test_grn_upm(self):
        self.assertTrue(np.all(grn.xm == gr.up(gr.xm)))
    def test_grn_vpm(self):
        self.assertTrue(np.all(grn.ym[::-1] == gr.vp(gr.ym)))
    def test_iu(self):
        _, iu = gr.U(gr.x)
        self.assertTrue(np.all(iu < gr.Nx))
    def test_iv(self):
        _, iv = gr.V(gr.y)
        self.assertTrue(np.all(iv < gr.Ny))
    def test_iw(self):
        _, iw = gr.W(xp, yp, zp)
        self.assertTrue(np.all(iw < gr.Nz))
    def test_uvw2xyz(self):
        xe, ye, ze = gr.uvw2xyz(up, vp, wp)
        ue, ve, we = gr.xyz2uvw(xe, ye, ze)
        tol = 1e-5
        crit = np.abs(up - ue) + np.abs(vp - ve) + np.abs(wp - we)
        self.assertTrue( np.all( crit[ NOT( np.isnan(crit)) ] < tol) )
    def test_ix_out_left(self):
        ix = gr.ix(gr.x - 0.5 * gr.dx[0])
        self.assertTrue(  np.sum(ix<0) == 1)
    def test_ix_out_right(self):
        ix = gr.ix(gr.x + 0.5 * gr.dx[-1])
        self.assertTrue(  np.sum(ix<0) == 1)
    def test_iy_out_left(self):
        iy = gr.iy(gr.y[0] + 0.5 * gr.dy[0])
        self.assertTrue(  np.sum(iy<0) == 1)
    def test_iy_out_right(self):
        iy = gr.iy(gr.y[-1] - 0.5 * gr.dy[-1])
        self.assertTrue(  np.sum(iy<0) == 1)
    def test_iz_out_top(self):
        ix = 2
        iy = 2
        zp = gr.Z[iy, ix, :] + 0.5 * gr.DZ[iy, ix, 0]
        xp = gr.xm[ix] * np.ones(zp.shape)
        yp = gr.ym[iy] * np.ones(zp.shape)
        _,_,iz = gr.ixyz(xp, yp, zp)
        self.assertTrue(  np.sum(iz<0) == 1)
    def test_iz_out_bot(self):
        ix = 2
        iy = 2
        zp = gr.Z[iy, ix, :] - 0.5 * gr.DZ[iy, ix, -1]
        xp = gr.xm[ix] * np.ones(zp.shape)
        yp = gr.ym[iy] * np.ones(zp.shape)
        _,_,iz = gr.ixyz(xp, yp, zp)
        self.assertTrue(  np.sum(iz<0) == 1)
    def test_ixyz2global_index(self):
        ix, iy, iz = gr.ixyz(xp, yp, zp)
        L = AND(ix>=0, iy>=0, iz>=0)
        Ic  = iy[L] * gr.Ny * gr.Nz + ix[L] * gr.Nz + iz[L]
        Iglob = gr.ixyz2global_index( ix[L], iy[L], iz[L])
        self.assertTrue(np.all(Ic == Iglob))
    def test_xyz2global_index(self):
        ix, iy, iz = gr.ixyz(xp, yp, zp)
        L = AND( ix>=0, iy>=0, iz>=0)
        Ic  = iy[L] * gr.Ny * gr.Nz + ix[L] * gr.Nz + iz[L]
        Iglob =  gr.xyz2global_index(xp, yp, zp)

        self.assertTrue(np.all(Ic == Iglob[L]))
    def test_inside(self):
        """ Test whether these points are inside the grid."""

        id = np.array( [
                    [0, 0, 0],
                    [-1, 0, 0],
                    [0, -1, 0],
                    [0, 0, -1],
                    [-1, -1, 0],
                    [-1, 0, -1],
                    [0, -1, -1],
                    [-1, -1, -1],

                    [2, 0, 0],
                    [2, -1,0],
                    [2, 0, -1],
                    [2, -1, -1],
                    [0, 2, 0],
                    [-1, 0,0],
                    [0, 2, -1],
                    [-1, 2, -1],
                    [0, 0, 2],
                    [-1, 0, 2],
                    [0, -1, 2],
                    [-1, -1, 2]], dtype = int)

        xM = np.mean(gr.x)
        yM = np.mean(gr.y)
        zM = np.mean(gr.Z.ravel())

        xp0 = gr.x[id[:,0]]
        yp0 = gr.y[id[:,1]]
        zp0 = gr.Z[id[:,1], id[:,0], id[:,2]]

        xp1 = xM + 1.01 * (xp0 - xM)
        yp1 = yM + 1.01 * (yp0 - yM)
        zp1 = zM + 1.01 * (zp0 - zM)

        xp2 = xM + 0.99 * (xp0 - xM)
        yp2 = yM + 0.90 * (yp0 - yM)
        zp2 = zM + 0.99 * (zp0 - zM)

        xxp = np.hstack((xp0, xp1, xp2))
        xyp = np.hstack((yp0, yp1, yp2))
        xzp = np.hstack((zp0, zp1, zp2))

        I = gr.inside(xxp, xyp, xzp)
        J = np.hstack(( np.ones(20, dtype=int),
                        np.zeros(20, dtype=int),
                        np.ones(20, dtype=int))) == 1

        self.assertTrue(np.all(I == J))

if __name__ == "__main__":
    unittest.main()
