#Sam Krimmel
#5/14/18
#homework1.py - ask user for word and tell them whether or not it is in dictionary file

file = open('engmix.txt')

word = input('Enter a word: ')

for line in file:
    if word == line:
        print('Your word is in the dictionary!')
