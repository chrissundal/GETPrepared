import math

def planet_mass(gravity,radius):
    mass = (gravity * radius ** 2) / (6.67 * 10 ** -11)
    return mass

def planet_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume