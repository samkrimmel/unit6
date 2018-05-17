#Sam Krimmel
#5/17/18
#warmup17.py - dununu dununu nu nu nuuu do do doooooo

file = open('engmix.txt')


for line in file:
    letrs = 0
    for letter in 'krimelKRIMEL':
        if letter in line:
            letrs += 1
    if letrs >= 6:
        print(line.strip())
