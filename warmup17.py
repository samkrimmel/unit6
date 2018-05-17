#Sam Krimmel
#5/17/18
#warmup17.py - dununu dununu nu nu nuuu do do doooooo

file = open('engmix.txt.)

letrs = 0
for line in file:
    for letter in 'krimelKRIMEL':
        if letter in line:
            letrs += 1
    if letrs >= 6:
        print line
