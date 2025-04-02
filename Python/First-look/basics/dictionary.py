# burgers = {'Hamburger': 'angus','Cheeseburger': 'ost'}
# print(burgers['Hamburger'])
# print('Cheeseburger' in burgers) # sjekk om den er der
# print(burgers.keys()) # vis keys
# print(burgers.values()) # vis verdien
# burgerlist = list(burgers.keys())
# print(burgerlist)
# burgervalues = list(burgers.values())
# print(burgervalues)
# burgertotal = len(burgers)
# burgercount = burgerlist.count('Cheeseburger')
# print('antall cheeseburgere:', burgercount)
# print('total:', burgertotal)
# burgers['Juicy'] = 'saftig og stor'
# print(burgers)
#
# person = dict(name='Chris', age=37, job='Student')
# print(person)
def burger_count(dictionary):
    hamburgers = list(dictionary.values())
    for burger in set(hamburgers):
        num = hamburgers.count(burger)
        print(f'Det er {num} burger med {burger} i seg')

# def burger(dictionary):
#     for key, value in dictionary.items():
#         print(f'Jeg spiser en {key} og den har {value} i seg')

burgers = {}

while True:
    burger_name = input('Skriv inn navn på burger: ')
    burger_desc = input('Skriv inn beskrivelse av burger: ')
    burgers[burger_name] = burger_desc
    print(burgers)
    more = input('Vil du legge til en annen burger? (j/n): ')
    if more == 'n': break

burger_count(burgers)