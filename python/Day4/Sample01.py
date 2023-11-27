# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS

f = open("D:\python\Day4\string.txt")

givenStr = f.read()

wordList = givenStr.split()

sentence = ''

for word in wordList:
    sentence += word[::-1] + ' '

f.close()

print(sentence)