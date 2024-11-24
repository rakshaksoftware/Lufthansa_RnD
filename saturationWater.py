import math

def calculate_e_water(T):
    # Given constants
    T_st = 372.15  # Steam point temperature in Kelvin

    # Goff-Gratch equation components
    term1 = -7.90298 * ((T_st / T) - 1)
    term2 = 5.02808 * math.log10(T_st / T)
    term3 = -1.3816e-7 * (10**(11.344 * (1 - T / T_st)) - 1)
    term4 = 8.1328e-3 * (10**(-3.49149 * ((T_st / T) - 1)) - 1)

    # Calculate log(e_water)
    log_e_water = term1 + term2 + term3 + term4

    # Convert log(e_water) to e_water
    e_water = 10**log_e_water

    return e_water

# Input temperature T from the user
T = float(input("Enter the temperature T (in Kelvin): "))

# Calculate e_water
e_water = calculate_e_water(T)

# Display the result
print(f"The saturation vapor pressure (e_water) at temperature {T} K is: {e_water} Pa")