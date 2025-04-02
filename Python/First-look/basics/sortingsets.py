from importlib.resources.readers import remove_duplicates

nums = [1,5,10,2,5,9,5,10,15,20,3,7,4,6]
sorted_nums = sorted(nums)
print('sortert:',sorted_nums)
nums_set = set(nums)
print('tatt bort duplikater:',nums_set)

names = ['Chris','Frank','Tore','Lisa','Aksel', 'amanda','Amanda', 'Sonja', 'Harald', 'Haakon'] # store bokstaver kommer først

names.sort()
print('vanlig:',names)

sorted_names = sorted(names)
print('vanlig:',sorted_names)

names.sort(reverse=True)
print('baklengs:',names)

names.sort(key=len)
print('lengde på string:',names)

lower_names = sorted(names, key=str.lower)
print('vanlig men inkluder lower:',lower_names)

lowercase_names = [name.lower() for name in names if isinstance(name,str)]
lowercase_names.sort()
print('konvertert til lower og sortert:',lowercase_names)

names_set = set(lowercase_names)
sorted_names_set = sorted(names_set)
print('konvertert, til lower og tatt bort duplikater:',sorted_names_set)

people = {'Chris': 37,'Frank': 29,'Aksel': 22,'amanda': 28,'Amanda': 24}
print(people)
sorted_people = sorted(people.items(), key=lambda x: (x[1], x[0].lower()))
print('Sortert etter alder:', sorted_people)
lower_sorted_people = {person.lower(): age for person, age in sorted_people}.items()
sorted_people_no_duplicates = sorted(lower_sorted_people, key=lambda x: x[1])
print('Sortert etter alder, til lower og tatt bort duplikater:', sorted_people_no_duplicates)

lower_sorted_people = {person.lower(): age for person, age in people.items()}
upper_first = [person.capitalize() for person in lower_sorted_people]
print('Uten duplikater i lower:', lower_sorted_people)
print('Stor forbokstav uten duplikater:', upper_first)
