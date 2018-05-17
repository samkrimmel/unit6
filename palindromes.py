#Sam Krimmel
#5/16/18
#palindromes.py - prints out all palindromes

file = open('engmix.txt')

palindromes = []
for line in file:
    back = ''
    for ch in line:
        back = ch + back
    if line == back:
        palindromes.append(line.strip())

for item in palindromes:
    print(item)
