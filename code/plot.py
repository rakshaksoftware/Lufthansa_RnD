import numpy as np
from scipy.optimize import fsolve
T_st = 373.15
T_fz = 273.15
eps = 0.622
P = 1000 # mB = 100000 Pa
def e_w_star(T): # hPa
    '''https://sciencepolicy.colorado.edu/~voemel/vp.html'''
    return (10**(-7.9028*((T_st/T)-1)+5.02808*np.log10(T_st/T)-1.3816e-7*(10**(11.344*(1-T/T_st))-1)+8.1328e-3*(10**(-3.49149*(T/T_st-1))-1))) * 1013.246
def e_i_star(T): # hPa
    '''https://sciencepolicy.colorado.edu/~voemel/vp.html'''
    return (10**(-9.09718*((T_fz/T)-1)-3.56654*np.log10(T_fz/T)+0.876793*(1-T/T_fz))) * 6.1071
def w_sw(T):
    '''https://pressbooks-dev.oer.hawaii.edu/atmo/chapter/chapter-4-water-vapor/#:~:text=Mixing%20Ratio,-Mixing%20ratio%2C%20r&text=Pressure%20(P)%20should%20be%20in,es%2C%20instead%20of%20e'''
    return eps*e_w_star(T)/(P-e_w_star(T))
def w_si(T):
    '''https://glossary.ametsoc.org/wiki/Mixing_ratio'''
    return eps*e_i_star(T)/(P-e_i_star(T))
