#Sam Krimmel
#5/14/18
#homework3.py - add ! to the end of each line in input.txt

file = open('homework1.py')

for line in file:
    if len(line) > 0:
        print(line.strip('\n') + '!')
    else:
        print(line.strip('\n'))