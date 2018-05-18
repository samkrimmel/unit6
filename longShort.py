#Sam Krimmel
#5/17/18
#longShort.py - prints longest and shortest word for each letter of the alphabet

file = open('engmix.txt')

Long = ['']*26
Short = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa']*26

alph = 'abcdefghijklmnopqrstuvwxyz'

for line in file:
    line = line.strip()
    if len(line) > 0 and Long[alph.index((line[0]).lower())] < line:
        Long[alph.index(line[0])] = line
    if len(line) > 0 and line < Short[alph.index((line[0]).lower())]:
        Short[alph.index(line[0])] = line
        
print(Long)
print(Short)