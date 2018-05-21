#Sam Krimmel
#5/21/18
#quiz6.py

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if len(line) >= 9:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break

