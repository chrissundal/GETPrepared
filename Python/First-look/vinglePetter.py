import random
from time import sleep
def start_veldig_basic():
    input('Hva skal du ta en beslutning på?: ')
    random_number = random.randint(0, 1)
    for i in range(1, 11):
        print(f'\r{"\u2591" * i} {i * 10}%', end='', flush=True)
        sleep(0.5)
    print()
    print('svar: Ja' if random_number == 0 else 'svar: Nei')
    print()
    input()

# input('Hva skal du ta en beslutning på?: ')
# random_number = random.randint(0, 1)
# print('svar: Ja') if random_number == 0 else print('svar: Nei')

# input('Hva skal du ta en beslutning på?: ')
# random_number = random.randint(0, 1)
# print('__________')
# sleep(1)
# print('##________')
# sleep(1)
# print('####______')
# sleep(1)
# print('######____')
# sleep(1)
# print('########__')
# sleep(1)
# print('##########')
# sleep(1)
# print('svar: Ja') if random_number == 0 else print('svar: Nei')