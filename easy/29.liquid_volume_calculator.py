# Please write a function that calculates liquid volume in a sphere using the following formula. 
# The radius r  is always 10, so consider making it a default parameter.

import math

def liquid_volume(height, radius=10):
    return ((4/3) * math.pi * radius**3) - ((1/3) * math.pi * height**2 * (3 * radius - height))

print(liquid_volume(2))