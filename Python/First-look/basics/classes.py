from space.Planet import Planet
from space.calc import planet_mass, planet_volume

hoth = Planet('Hoth','200000',5.5,'Hoth System')
planetX = Planet('X-1','100000',1,'X-1 System')

hoth_mass = planet_mass(hoth.gravity, hoth.radius)
hoth_volume = planet_volume(hoth.radius)
planetX_mass = planet_mass(planetX.gravity, planetX.radius)
planetX_volume = planet_volume(planetX.radius)

print(f'Hoth: {hoth_mass:,.2f} kg, {hoth_volume:,.2f} m3')
print(f'PlanetX: {planetX_mass:,.2f} kg, {planetX_volume:,.2f} m3')

print(f'{hoth.info()} {hoth.orbit()}')
print(f'{planetX.info()} {planetX.orbit()}')
print()
print(Planet.commons())
print(Planet.spin('i veldig høy fart'))
print(Planet.spin())
# class Planet:
#     shape = 'runde'
#
#     def __init__(self,name,radius,gravity,system):
#         self.name = name
#         self.radius = radius
#         self.gravity = gravity
#         self.system = system
#
#     def orbit(self):
#         return f'og sirkler i {self.system}'
#
#     def info(self):
#         return f'{self.name} er en planet med radius {self.radius} og gravitasjon på {self.gravity}'
#
#     @classmethod
#     def commons(cls):
#         return f'Alle planeter er {cls.shape} pga gravitasjonen'
#
#     @staticmethod
#     def spin(speed = '10000 kilometer i timen'):
#         return f'Planeten spinner {speed}'

# hoth = Planet('Hoth','200000',5.5,'Hoth System')
# # print(f'Navn: {hoth.name}')
# # print(f'Radius: {hoth.radius}')
# # print(f'Gravitasjon: {hoth.gravity}')
# # print(hoth.orbit())
# print(f'{hoth.info()} {hoth.orbit()}')
#
# planetX = Planet('X-1','100000',1,'X-1 System')
# print(f'{planetX.info()} {planetX.orbit()}')
# print(Planet.commons())
# print(Planet.spin('i veldig høy fart'))
# print(Planet.spin())