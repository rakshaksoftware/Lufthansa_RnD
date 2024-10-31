import numpy as np
T_st = 373.15
T_C = 40
eps = 0.622
P = 1000
delta_T = 40
def e_star(T): # hPa
    return 10**(-7.9028*((T_st/T)-1)+5.02808*np.log10(T_st/T)-1.3816e-7*(10**(11.344*(1-T/T_st))-1)+8.1328e-3*(10**(-3.49149*(T/T_st-1))-1)) * 1013.246
def w(T):
    return eps*e_star(T)/(P-e_star(T))
for T_C in (40,50,60,70,80):
    T = 272.15 - T_C
    # print(w(T))
    # print(w(T+delta_T))
    for delta_T in (5,40):
        print(f"Increase in mixing ratio for P = {P} and T = -{T_C} and delta_T = {delta_T} is:",end="")
        print(1000*(w(T+delta_T) - w(T))/delta_T) # 1000 for g/kg to g/g