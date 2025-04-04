with open('../files/write.txt', 'w') as write_file: # skrive
    write_file.write('Hello, world!')
    write_file.write('\nThis is a new line.')

with open('../files/write.txt', 'a') as write_file: # legg til (ammend) tekst
    write_file.writelines(['\nHello, again!', '\nThis is another new line.'])

quotes = ['"The best thing in life is free!"', '"The rest of the world will not be so good as you."']

with open('../files/write.txt', 'a') as write_file: # legger til
    write_file.write('\n'.join(quotes))

with open('../files/quotes.txt', 'w') as write_file: # lager en ny fil
    write_file.write('\n'.join(quotes))

with open('../files/write.txt') as read_file:
    print(read_file.read())
