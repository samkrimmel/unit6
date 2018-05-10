#Sam Krimmel
#5/10/18
#longestDictionary.py - prints the longest word in the dictionary file

file = open('engmix.txt')

longest = ''
for line in file:
    if len(line) > len(longest):
        longest = line
print(longest)
