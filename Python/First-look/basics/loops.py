people = [{'name': 'John', 'age': 32}, {'name': 'Paul', 'age': 33},{'name': 'George', 'age': 31},{'name': 'Ringo', 'age': 35}]

def print_person(person):
    print(f"Navn: {person['name']} Alder: {person['age']}")

# for person in people:
#     # print('Navn:', person['name'], 'Alder:', person['age'])
#     # print(f"Navn: {person['name']} Alder: {person['age']}")
#     print_person(person)

# slice
# for person in people[1:3]:
#     print_person(person)

for person in people:
    if person['name'] == 'Paul':
        print(f'{person['name']} - er god på å lage sanger')
        break
    else:
        print_person(person)

# age = 25
# num = 0
# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1

# items = [1, 2, 3, 4, 5]
# for item in items:
#     print(item)
# print()
# #total numbers
# for num in range(5):
#     print(num)
# print()
# #start and end
# for num in range(1,6):
#     print(num)
# print()
#
# #step
# for num in range(1,6,2):
#     print(num)

burgers = ['angus', 'kylling', 'fisk', 'vegetar', 'juicy']

# for num in range(len(burgers)):
#     print(num, burgers[num])

# revers
for num in range(len(burgers) -1, -1, -1):
    print(num, burgers[num])
