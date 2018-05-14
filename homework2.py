#Sam Krimmel
#5/14/18
#homework2.py - print number word entered from the dictionary

file = open('engmix.txt')

fileList = []
for line in file:
    fileList.append(line.strip())

numWord = int(input('Enter a number of a word in the dictionary: '))

while True:
    if numWord > len(fileList):
        numWord = int(input('Enter a number of a word in the dictionary: '))
    else:
        break

print(fileList[numWord-1])

