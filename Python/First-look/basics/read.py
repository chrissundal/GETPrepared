# ipsum_file = open('../files/ipsum.txt')

# for line in ipsum_file:
#     #print(line)
#     print(line.rstrip())
#
# ipsum_file.seek(0)
#
# lines = ipsum_file.readlines()
# print(lines)
# # print(ipsum_file.read())

# ipsum_file.seek(50) # start på char 50
# file_text = ipsum_file.read(100) # les 100 chars
# print(file_text)

# ipsum_file.close() # må lukkes

def sequence_filter(line):
    return '>' not in line

with open('../files/dna_sequence.txt') as dna_file: # trenger ikke lukkes etterpå
    lines = dna_file.readlines()
    filtered_lines = list(filter(sequence_filter, lines))
    for line in filtered_lines:
        print(line)
