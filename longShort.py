#Sam Krimmel
#5/17/18
#longShort.py - prints longest and shortest word for each letter of the alphabet

file = open('engmix.txt')

Long = ['']*26
Short = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']*26

alph = 'abcdefghijklmnopqrstuvwxyz'

for line in file:
    line = line.strip()
    if Long[alph.index((line[0]).lower())] < line and line != '':
        Long[alph.index(line[0])] = line
    if line < Short[alph.index((line[0]).lower())] and line != '':
        Short[alph.index(line[0])] = line
        
print(Long)
print(Short)