from random import shuffle

prizes = [5,10,50,100,1000]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)

print(dbl_prizes)

dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

nums = [1,2,3,4,5,6,7,8,9,10]

squared_even_nums = []
for num in nums:
    if num % 2 == 0:
        squared_even_nums.append(num**2) #partall lagt til liste ganget med seg selv
print(squared_even_nums)

squared_even_nums = [num**2 for num in nums if num % 2 == 0]
print(squared_even_nums)

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['horse', 'donkey', 'rabbit']
anagrams = []

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

print([jumble(word) for word in words]) # comprehension

# anagrams = list(map(jumble, words))
# print(anagrams)

print(list(map(jumble, words))) #map

# filter(testing_function,data) filtrerings måte

filtered_words = list(filter(lambda word: word.startswith('d'), words))
print(filtered_words)

def remove_word(word):
    return word != 'donkey'

print(list(filter(remove_word, words)))
print(list(filter(lambda word: word != 'rabbit', words)))

filtered_words = []

for word in words:
    if word != 'rabbit':
        filtered_words.append(word)

print(filtered_words)

print([word for word in words if word != 'rabbit'])

print(list(filter(lambda num: num != 3, nums)))

def square(num):
    return num**2

print(list(map(square, nums)))

print(list(map(lambda num: num**2, nums)))