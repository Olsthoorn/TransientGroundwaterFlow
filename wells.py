import pdb
import numpy as np

from scipy.special import expi
def W(u): return  -expi(-u)  # Theis

def wh(u, rho):
    """Returns Hantush's well function values

    Note: works only for scalar values of u and rho

    Parameters:
    -----------
    u : scalar  (u= r^2 * S / (4 * kD * t))
    rho : sclaar (rho =r / lambda, lambda = sqrt(kD * c))
    Returns:
    --------
    Wh(u, rho) : Hantush well function value for (u, rho)
    """
    try:
        u =float(u)
        rho =float(rho)
    except:
        print("u and rho must be scalars.")
        raise ValueError()

    LOGINF = 2
    y = np.logspace(np.log10(u), LOGINF, 1000)
    ym = 0.5 * (y[:-1]+  y[1:])
    dy = np.diff(y)
    w = np.sum(np.exp(-ym - (rho / 2)**2 / ym ) * dy / ym)
    return w


def Wh(U,Rho):
    """Returns multiple values of Hantush's well function.

    Parameters:
    -----------
    U : ndarray with values of u
    Rho : ndarray with values of rho

    Returns:
    --------
    well function values for all combinations of U and Rho in an ndarray of shape (Nrho, Nu)
    """
    U   = np.array(U,   dtype=float).ravel()  # converts U to shape ([)1, Nu)
    Rho = np.array(Rho, dtype=float).ravel()  # convers V to shape (Nr, 1)
    w = np.zeros((len(Rho), len(U))) *  np.NaN     # initialize array w of shape [Nr, Nu]
    for iu, u in enumerate(list(U)):
        for ir, rho in enumerate(Rho):
            w[ir, iu] = wh(u, rho)
    return w
