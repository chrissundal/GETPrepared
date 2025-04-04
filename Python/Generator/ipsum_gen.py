import random

words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]
paragraphs = int(input('Hvor mange paragrafer? '))

def attach(word):
    random_pos = random.randint(0, len(words) - 1)
    return f'{word} {words[random_pos]}'

with open('ipsum.txt') as org_ipsum:
    items = org_ipsum.read().split()

    for n in range(paragraphs):
        my_text = list(map(attach, items))
        with open('my_ipsum.txt', 'a') as my_ipsum:
            my_ipsum.write(' '.join(my_text) + '\n\n')
