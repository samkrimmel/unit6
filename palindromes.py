#Sam Krimmel
#5/16/18
#palindromes.py - prints out all palindromes

file = open('engmix.txt')

palindromes = []
for line in file:
    L = []
    L.append(line.strip())
    L2 = L[:]
    if L == L2.reverse():
        palindromes.append(line.strip())

for item in palindromes:
    print(item)
