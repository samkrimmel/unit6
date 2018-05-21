#Sam Krimmel
#5/21/18
#quiz6.py

file = open('engmix.txt')

"""
#Program 1:
letter = input('Enter a letter: ')

for line in file:
    line = line.strip()
    if line.count(letter) == 4:
        print(line)
"""
"""
#Program 2:
for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break
"""
"""
#Program 3:
letter = input('Enter a letter: ')
num = int(input('Enter a number: '))

for line in file:
    line = line.strip()
    if len(line) == num and line[0] == letter:
        print(line)
"""
"""
#Program 4:
words = []

for line in file:
    line = line.strip()
    if len(line) >= 10:
        words.append(line)

print(words[7999])
"""
