import numpy as np
import matplotlib.pyplot as plt

# Constants
T_st = 373.15
T_fz = 273.15
eps = 0.622
P = 1000 # mB = 100000 Pa
RH = 0.6
# Functions
def e_w_star(T): # hPa
    '''https://sciencepolicy.colorado.edu/~voemel/vp.html'''
    return (10**(-7.9028*((T_st/T)-1)+5.02808*np.log10(T_st/T)-1.3816e-7*(10**(11.344*(1-T/T_st))-1)+8.1328e-3*(10**(-3.49149*(T/T_st-1))-1))) * 1013.246

def w_sw(T):
    '''https://pressbooks-dev.oer.hawaii.edu/atmo/chapter/chapter-4-water-vapor/#:~:text=Mixing%20Ratio,-Mixing%20ratio%2C%20r&text=Pressure%20(P)%20should%20be%20in,es%2C%20instead%20of%20e'''
    return eps*e_w_star(T)/(P-e_w_star(T))

def e_i_star(T): # hPa
    '''https://sciencepolicy.colorado.edu/~voemel/vp.html'''
    return (10**(-9.09718*((T_fz/T)-1)-3.56654*np.log10(T_fz/T)+0.876793*(1-T/T_fz))) * 6.1071

def w_si(T):
    '''https://glossary.ametsoc.org/wiki/Mixing_ratio'''
    return eps*e_i_star(T)/(P-e_i_star(T))

# Temperature range
T = np.linspace(0, 30, 100) # Temperature range from 250K to 400K

# Calculate w_sw for each temperature
w_sw_values = [w_sw(213.13+temp) for temp in T]

def calculate_G(p, eta):
    # Constants
    EI_H2O = 1.2232  # Emission index for water (kgH2O/kgfuel)
    cp = 1004        # Specific heat capacity of air (J/kg/K)
    eps = 0.622      # Ratio molar mass of water vapor and air
    Q = 43e6         # Specific combustion heat (J/kg)
    
    # Calculate G using the formula
    G = (EI_H2O * cp * p) / (eps * Q * (1 - eta))
    
    # Output the result
    print(f"\nThe isobaric mixing line (G) value is: {G:.6f}")
    return G

def calculate_T_lm(G):
    import math
    log_G = math.log10(G - 0.053)
    T_lm = -46.6 + 9.43 * log_G + 0.720 * (log_G ** 2)
    return T_lm



def rhs( delta ,T):
    return 336*delta/10000 - w_si(T) + w_sw(T)*(RH+1)

rhs_values = [rhs(temp, 213.13) for temp in T]

# Plotting
plt.plot(T, w_sw_values)
plt.plot(T, rhs_values, 'r')
plt.xlabel('Temperature (K)')
plt.ylabel('w_sw')
plt.title('w_sw vs Temperature')
plt.grid(True)
plt.show()
