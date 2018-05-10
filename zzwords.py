#Sam Krimmel
#5/10/18
#zzwords.py - prints all words with zz

file = open('engmix.txt')

for line in file:
    if 'zz' in line:
        print(line)
