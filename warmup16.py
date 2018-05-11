#Sam Krimmel
#5/11/18
#warmup16.py - prints out all words that start with initial and end with last initial

file = open('engmix.txt')

for line.strip() in file:
    word = line.split(' ')
    if line[0] == 's' and line[-1] == 'k':
        print(line)
