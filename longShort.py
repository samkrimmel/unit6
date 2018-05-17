#Sam Krimmel
#5/17/18
#longShort.py - prints longest and shortest word for each letter of the alphabet

file = open('engmix.txt')

for ch in 'abcdefghijklmnopqrstuvwxyz':
    L = []
    for line in file:
        line = line.strip()
        while ch == line[0]:
            L.append(line)
    print(max(L))
    print(min(L))
