#Sam Krimmel
#5/17/18
#longShort.py - prints longest and shortest word for each letter of the alphabet

file = open('engmix.txt')

Long = ['']*26
Short = ['']*26

alph = 'abcdefghijklmnopqrstuvwxyz'

for line in file:
    line = line.strip()
    if alph.index(line[0])