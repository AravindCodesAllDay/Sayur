# Problem #2
# Write a program that reads a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."

f = open("D:\python\Day2\string.txt")

givenStr = f.read()

wordList = givenStr.split()

previousWord = ''
repeatedDict = {}

for word in wordList:
    
    if word == previousWord :

        if(word not in repeatedDict.keys()) :
            repeatedDict[word] = 0
            
        repeatedDict[word] += 1
    
    previousWord = word

f.close()

for x in repeatedDict.keys():
    print(f'{x}:{repeatedDict[x]}')
