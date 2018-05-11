#Sam Krimmel
#5/10/18
#reverseFile.py - asks user for a file and prints out reverse version

infile = input('Enter a file: ')

file = open(infile)

lines = []

for line in file:
    lines += line

print(lines)
lines.reverse()

for item in lines:
    print(item)


