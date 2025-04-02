# def greet(name = "World", time = "morning"):
#     print(f"Good {time}, {name}")
# name = input("What is your name? ")
# time = "afternoon"
# greet(name)
# greet(name, time)

# def area(radius):
#     return 3.14 * radius ** 2

# def volume(area, length):
#     print(area * length)

# radius = int(input("Skriv inn radius: "))
# length = int(input("Skriv inn lengde: "))

# #area_calc = area(radius)
# #volume(area_calc, length)
# volume(area(radius), length)

my_name = "Chris"

def print_name():
    global my_name #endre global til Mario
    my_name = "Mario"
    print('navnet inne i funksjonen er', my_name)

print_name()
print('Navnet utenfor funksjonen er', my_name)