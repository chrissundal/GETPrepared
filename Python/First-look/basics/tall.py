# radius = input('Skriv inn radiusen til en sirkel (m): ')
# area = 3.142 * int(radius)**2
# print('Arealet til sirkelen er:', area)

# formattering

# num1 = 3.1415926535
# num2 = 10.2903948

# print('num 1 er: {0} og num 2 er: {1}'.format(num1, num2))
# print(f'num 1 er: {num1:.3} og num 2 er: {num2:.3f}')

try:
    age = int(input('Hvor gammel er du? '))
    # if age < 10:
    #     print('Du var ikke gammel!')
    # elif age < 30:
    #     print('Du er ikke så gammel!')
    # elif age < 50:
    #     print('Gammel')
    # else:
    #     print('Like før det er over!')

    # match age:
    #     case age if age < 10:
    #         print('Du var ikke gammel!')
    #     case age if age < 30:
    #         print('Du er ikke så gammel!')
    #     case age if age < 50:
    #         print('Gammel krok')
    #     case _:
    #         print('Like før det er over!')

    print(
        'Du var ikke gammel!' if age < 10 else
        'Du er ikke så gammel!' if age < 30 else
        'Gammel' if age < 50 else
        'Like før det er over!'
    )

    # print('Du var ikke gammel!') if age < 10 else print('Du er gammel!')

except ValueError:
    print('Vennnligst skriv inn ett tall!')