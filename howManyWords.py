#Sam Krimmel
#5/10/18
#howManyWords.py - how many words there are for each number of letters in the dictionary

file = open('engmix.txt')

numWords = [0]*21

for i in range(1,22):
    for line in file.strip():
        if len(line) == i:
            numWords[i-1] += 1

for i in range(1,22):
    print('There are',numWords[i-1], i, 'letter words.')
