import sympy as sp

# Declare the variable for delta_T
delta_T = sp.symbols('delta_T')
RH = 0.6
print("Declared variables: delta_T, RH")

# Define constants
T = 213.15  # Setting T as a constant
T_st = 373.15
T_fz = 273.15
eps = 0.622
P = 200
print(f"Defined constants: T={T}, T_st={T_st}, T_fz={T_fz}, eps={eps}, P={P}")

# Define e_i_star and e_w_star with T as a constant
e_i_star = (10**(-9.09718*((T_fz/T)-1) - 3.56654*sp.log(T_fz/T, 10) + 0.876793*(1 - T/T_fz))) * 6.1071
print(f"e_i_star defined: {e_i_star}")

e_w_star = (10**(-7.9028*((T_st/T)-1) + 5.02808*sp.log(T_st/T, 10) - 1.3816e-7*(10**(11.344*(1 - T/T_st)) - 1) + 8.1328e-3*(10**(-3.49149*(T/T_st - 1)) - 1))) * 1013.246
print(f"e_w_star defined: {e_w_star}")

# Define w_si and w_sw with T as a constant
w_si = eps * e_i_star / (P - e_i_star)
print(f"w_si defined: {w_si}")

w_sw_T = eps * e_w_star / (P - e_w_star)
print(f"w_sw_T defined: {w_sw_T}")

w_sw_T_delta = eps * e_w_star.subs(T, T + delta_T) / (P - e_w_star.subs(T, T + delta_T))
print(f"w_sw_T_delta defined: {w_sw_T_delta}")

# Define the equation w_sw(T+delta_T) - w_sw(T) = (336*delta_T)/10000 - w_si + RH * w_sw(T)
equation = sp.Eq(w_sw_T_delta - w_sw_T, (336 * delta_T) / 10000 - w_si + RH * w_sw_T)
print(f"Equation defined: {equation}")

# Expand and simplify the equation step-by-step
lhs = w_sw_T_delta - w_sw_T
rhs = (336 * delta_T) / 10000 - w_si + RH * w_sw_T
print("Left-hand side (lhs) of the equation expanded:")
print(lhs)

print("Right-hand side (rhs) of the equation expanded:")
print(rhs)

# Combine the terms to form a single equation
combined_equation = lhs - rhs
print("Combined equation:")
print(combined_equation)

# Simplify the equation
simplified_equation = sp.simplify(combined_equation)
print("Simplified equation:")
print(simplified_equation)

# Solve the equation for delta_T
print("Solving the equation for delta_T...")
solution = sp.solve(simplified_equation, delta_T)
print(f"Solution: {solution}")
