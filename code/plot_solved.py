import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define constants
T = 243.15  # Setting T as a constant
T_st = 373.15
T_fz = 273.15
eps = 0.622
P = 1000
RH = 100

# Declare the variable for delta_T
delta_T = sp.symbols('delta_T')

# Define e_i_star and e_w_star with T as a constant
e_i_star = (10**(-9.09718*((T_fz/T)-1) - 3.56654*sp.log(T_fz/T, 10) + 0.876793*(1 - T/T_fz))) * 6.1071
e_w_star = (10**(-7.9028*((T_st/T)-1) + 5.02808*sp.log(T_st/T, 10) - 1.3816e-7*(10**(11.344*(1 - T/T_st)) - 1) + 8.1328e-3*(10**(-3.49149*(T/T_st - 1)) - 1))) * 1013.246

# Define w_si and w_sw with T as a constant
w_si = eps * e_i_star / (P - e_i_star)
w_sw_T = eps * e_w_star / (P - e_w_star)
w_sw_T_delta = eps * e_w_star.subs(T, T + delta_T) / (P - e_w_star.subs(T, T + delta_T))

# Define the equation w_sw(T+delta_T) - w_sw(T) = (336*delta_T)/10000 - w_si + RH * w_sw(T)
equation = sp.Eq(w_sw_T_delta - w_sw_T, (336 * delta_T) / 10000 - w_si + RH * w_sw_T)

# Generate values for delta_T
delta_T_values = np.linspace(-10, 10, 400)

# Substitute and evaluate
solutions = [sp.solve(equation.subs(delta_T, val), delta_T) for val in delta_T_values]
solutions = [sol[0] if sol else None for sol in solutions]

# Plotting the curve
plt.plot(delta_T_values, solutions, label='Solution of Delta_T')
plt.xlabel('Delta_T')
plt.ylabel('Solution')
plt.title('Curve of the Equation Solved for Delta_T')
plt.legend()
plt.grid(True)
plt.show()
