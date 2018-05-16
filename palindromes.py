#Sam Krimmel
#5/16/18
#palindromes.py - prints out all palindromes

file = open('engmix.txt')

palindromes = []
for line in file:
    L = []
    L.append(line.strip())
    L2 = L.reverse()
    if L == L2:
        palindromes.append(line.strip())

print(palindromes)
