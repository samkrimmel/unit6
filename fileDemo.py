#Sam Krimmel
#5/9/18
#fileDemo.py - how to read a file

file = open('engmix.txt')

numWords = 0
for line in file:
    if 'sam' in line:
        print(line.strip())
    numWords+=1

print(numWords)
