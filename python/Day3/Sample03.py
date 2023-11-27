# Problem #3
# From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
# for each word. Write this information at the end of file under the heading "Summary of 4 letter words"


# For problem 2 and 3,
# Make sure your code includes exception handling for reading from a file.
# Reading material for exception handling - https://www.w3schools.com/python/python_try_except.asp
# Video https://youtu.be/83Y2qZvWxdE?si=g2MB45bZHI8-ah5q

try:
    f = open("D:\python\Day3\string.txt")

    givenStr = f.read().lower()

    wordList = givenStr.split()

    repeatedDict = {}

    for word in wordList:
        
        if (len(word) == 4) :

            if(word not in repeatedDict.keys()) :
                repeatedDict[word] = 0
                
            repeatedDict[word] += 1
        
        previousWord = word

    f.close()

    for x in repeatedDict.keys():
        print(f'{x}:{repeatedDict[x]}')
except:
    print("An error occured")
