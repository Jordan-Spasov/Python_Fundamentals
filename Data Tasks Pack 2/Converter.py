# We want to convert miles per gallon (MPG) into litres per 100 kilometers (L/100km)

import math

m_p_g = int(input())

gallon = 4.54 
mile = 1.6 

# Calculate how many kilometers are traveled with one gallon using the formula:
km_per_gallon = m_p_g * mile

# Next, we find how many litres are used per 100 km:
liters_per_100_km = math.floor(100 * gallon / km_per_gallon)

print(f'{liters_per_100_km} litres per 100 km')