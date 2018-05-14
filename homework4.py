#Sam Krimmel
#5/14/18
#homework4.py

file = open('engmix.txt')

letter = input('Enter a letter: ')

bestNum = ''
for line in file:
    line.strip()
    if bestNum.count(letter) < line.count(letter):
        bestNum = line

print(bestNum, 'has your letter the most times!')
