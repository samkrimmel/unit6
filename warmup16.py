#Sam Krimmel
#5/11/18
#warmup16.py - prints out all words that start with initial and end with last initial

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if len(line) > 0 and line[0] == 't' and line[-1] == 'l':
        print(line)
