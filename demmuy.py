import math
from scipy.optimize import fsolve

# Constants from the table and the problem
E_L = 1232  # Emission index
m_f_dot = 1.0  # Example fuel flow rate
Q = 1004  # Specific heat capacity
eta = 0.4  # Propulsion efficiency
T_st = 372.15  # Steam point temperature in Kelvin
T0 = 273.16  # Ice-point temperature in Kelvin

# Step 1: Calculate G
# Constants (from the table in the image)
EI_H2O = 1.2232  # Emission index for water (kgH2O/kgfuel)
cp = 1004        # Specific heat capacity of air (J/kg/K)
eps = 0.622      # Ratio molar mass of water vapor and air
Q = 43e6         # Specific combustion heat (J/kg)

# Function to calculate G based on pressure and propulsion efficiency
def calculate_G():
    # Get user input for pressure and propulsion efficiency
    p = float(input("Enter the pressure (in hPa): "))  # Pressure in hPa
    eta = float(input("Enter the propulsion efficiency (eta): "))  # Efficiency
    
    # Calculate G using the formula
    G = (EI_H2O * cp * p) / (eps * Q * (1 - eta))
    
    # Output the result
    print(f"\nThe isobaric mixing line (G) value is: {G:.6f}")
    return G


# Step 2: Calculate T_lm
def calculate_T_lm(G):
    log_G = math.log10(G - 0.053)
    T_lm = -46.6 + 9.43 * log_G + 0.720 * (log_G ** 2)
    return T_lm

# Step 3: Goff-Gratch equation for e_water
def log_e_water(T):
    term1 = -7.90298 * (T_st / T - 1)
    term2 = 5.02808 * math.log10(T_st / T)
    term3 = -1.3816e-7 * (10 ** (11.344 * (1 - T / T_st)) - 1)
    term4 = 8.1328e-3 * (10 ** (-3.49149 * (T_st / T - 1)) - 1)
    return term1 + term2 + term3 + term4

# Step 4: Goff-Gratch equation for e_ice
def log_e_ice(T):
    term1 = -9.09718 * (T0 / T - 1)
    term2 = 3.56654 * math.log10(T0 / T)
    term3 = 0.876793 * (1 - T / T0)
    return term1 + term2 + term3

# Step 5: Calculate T_lc (where tangent of e_water intersects with e_ice)
def find_T_lc(T_lm):
    def tangent_line(T):
        # Calculate the slope of the tangent at T_lm
        delta_T = 1e-5
        slope = (log_e_water(T_lm + delta_T) - log_e_water(T_lm)) / delta_T
        intercept = log_e_water(T_lm) - slope * T_lm
        return slope * T + intercept

    def equation(T):
        # Find where the tangent line intersects with e_ice
        return 10 ** tangent_line(T) - 10 ** log_e_ice(T)

    # Initial guess for T_lc (based on typical values)
    T_guess = 220  # Initial guess in Kelvin
    
    # Use fsolve to solve the equation
    T_lc = fsolve(equation, T_guess)
    return T_lc[0]

# Main function to run the calculation
def main():
    # Step 1: Calculate G
    G = calculate_G()
    print(f"G = {G:.4f}")

    # Step 2: Calculate T_lm
    T_lm = calculate_T_lm(G)
    print(f"T_lm = {T_lm:.2f} K")

    # Step 3 and 4: Calculate T_lc (intersection of tangent of e_water and e_ice)
    T_lc = find_T_lc(T_lm)
    print(f"The threshold temperature T_lc is approximately: {T_lc:.2f} K")

# Run the main function
if __name__ == "__main__":
    main()