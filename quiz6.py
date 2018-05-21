#Sam Krimmel
#5/21/18
#quiz6.py

file = open('engmix.txt')

"""
#Program 2:
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break
"""
letter = input('Enter a letter: ')
num = int(input('Enter a number: '))

for line in file:
    line = line.strip()
    if len(line) == num and line[0] == letter:
        print(line)
