#Sam Krimmel
#5/10/18
#howManyWords.py - how many words there are for each number of letters in the dictionary

file = open('engmix.txt')

numWords = [0]*21

for i in range(1,22):
    for line in file:
        if len(line.strip()) == i:
            numWords[i-1] += 1

for i in range(1,21):
    print('There are',numWords[i-1], i, 'letter words.')

print('There is',numWords[20], '21 letter word')