# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 04:26:57 2016

Various useful functions for working with models

@author: Theo
"""


import numpy as np

#%matplotlib notebook

import matplotlib.pylab as plt
import mfexceptions as err


def stat(A):
    """Returns statistics of ndarray as dict"""
    B = A.ravel()
    Out = {}
    Out['shape'] = A.shape
    Out['min'] = np.min(B)
    Out['mean'] = np.mean(B)
    Out['med'] = np.median(B)
    Out['max'] = np.max(B)
    Out['std'] = np.std(B)
    return Out


def unique(x, tol=0.0001):
    """Return sorted unique values of x within tolerance,

    Ascending or descending direction is maintained

    """
    if x[0]>x[-1]:  # vector is reversed
        x = np.sort(x)[::-1]  # sort and reverse
        return x[np.hstack((np.diff(x) < -tol, True))]
    else:
        x = np.sort(x)
        return x[np.hstack((np.diff(x) > +tol, True))]


def display(*args, fmt='10.3g'):
    """Show a series if equal length vectors next to each other

    a bit like display() in Matlab, but without the headers:

    Example:
    show(z, y, z)
    """
    A = args if len(args)>1 else args[0]
    prarr(np.vstack(A).T, N=len(A), fmt=fmt)


def prarr(A, N=8, fmt='10.4g'):
    """matlab like 1D, 2D and 3D array Printer

    (Wraps around `prarr2`)

    examples:
        prarr(A)
        prarr(A, N=10)
        prarr(A, N=7, fmt='10.2f')

    Numeric format `fmt` must be fortran like format string:
        '8.4g', '10d', '12.4f', '15.3e'

    TO 160926
    """
    A = np.asarray(A)

    if len(A.shape)<2:  # make sure array is at least 2D
        A = A.reshape((1,len(A)))

    if len(A.shape)>2: # when 3D, print 2D layers repeatedly with 1 base layer prefix
        for iL in range(A.shape[2]):
            prefix = "Layer iz={0}, ".format(iL)
            prarr2(A[:,:,iL], N, fmt, prefix)
    else:
        prarr2(A, N, fmt, "") # regular 2D print


def prarr2(A, ncol=8, fmt='10.4g', prefix='', decimals=7):
    """Matlab like 2D array Printer.

    (Is called by wrapper `prarr`, see docstring of `prarr`)

    TO 160926
    """
    if A.dtype==complex:
        try:
            w,f = fmt.split('.')
            if int(w)<15:
                fmt='16.4f'
        except:
            pass
    ft = "{{0:{0}}}".format(fmt)     # construct format

    A = np.asarray(A)

    if len(A.shape)==1:
        A.reshape((1,len(A))) # make sure A is at least 2D

    SHP =A.shape
    Nrows, Ncols = SHP[:2] # number of rows and columns to print
    Nblocks = int(np.ceil(Ncols/ncol))# number of column blocks to print

    cols=np.array([0, ncol]) # first block of columns
    for iBlock in range(Nblocks): # print each block of columns
        print("\n{} for columns {} to {}".\
              format(prefix, cols[0], min(cols[1],Ncols)-1))
        for iRow in range(Nrows):  # print all rows
            a = np.round(A[iRow], decimals) # current data row
            for j in range(cols[0], min(cols[1],Ncols)):
                print(ft.format(a[j]), end="")  # print one row
            print()
        cols += ncol # next block of columns to be printed
        print # blank line


def XS(A, row=0):
    """returns cross section of 3D array along/at given row examples:
        XS(A)
        XS(A, row=2)
    see also: YS()

    TO 160926
    """
    return A[row,:,:].T


def YS(A, col=0):
    """returns cross seciton of 3D array along/at given column
    examples:
        YS(A)
        YS(A, col=3)
    see also: XS()

       TO 160926
    """
    return A[:,col,:].T


def spy(A, linespec='b.', tol=1e-4, Xm=None, Ym=None, ax=None):
    """Return figure showing which elements in array are non-zero"""
    #import pdb
    A = np.asarray(A)

    ax = ax if not ax==None else plt.gca()

    if len(A.shape) != 2:
        raise err.InputError("","Iinput array must be 2D")

    Ny, Nx = A.shape

    if Xm == None:
        Xm =  (np.arange(0, A.shape[1]) + 0.5).reshape(1,Nx) * np.ones((Ny,1))
    else:
      if not np.all(A.shape == Xm.shape):
          raise err.InputError("","shape of input array must match shape of Xm")
    if Ym == None:
        Ym =  (np.arange(0, Ny) + 0.5)[::-1].reshape(Ny,1) * np.ones((1,Nx))
    else:
      if not np.all(A.shape == Ym.shape):
          raise err.InputError("","shape of input aray must match shape of Ym")
    #pdb.set_trace()
    I = np.logical_not( np.logical_and( A > -tol, A < tol) )

    plt.setp(ax, 'xlim',(Xm[0,0],Xm[0,-1]), 'ylim', (Ym[-1,0], Ym[0,0]))

    plt.plot(Xm[I], Ym[I], linespec)
