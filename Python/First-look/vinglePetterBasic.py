import random
from time import sleep
def start_basic():
    input('Hva skal du ta en beslutning på?: ')
    random_number = random.randint(0, 1)
    random_times = random.randint(1, 4)
    crash_count = 0

    while crash_count < random_times:
        print('tenker...')
        random_crash = random.randint(1, 9)
        for i in range(1, 11):
            sleep(random.uniform(0.5, 1.5))
            print(f'\r{"\u2591" * i} {i * 10}%', end='', flush=True)
            if i == random_crash:
                crash_count += 1
                print("\nOops! Programmet krasjet...")
                sleep(1)
                break

    print('tenker...')
    for i in range(1, 11):
        sleep(random.uniform(0.5, 1.5))
        print(f'\r{"\u2591" * i} {i * 10}%', end='', flush=True)

    print("\nFerdig! Tar en beslutning...")
    sleep(1)
    print()
    print('Svar: Ja' if random_number == 0 else 'Svar: Nei')
    print()
    input()