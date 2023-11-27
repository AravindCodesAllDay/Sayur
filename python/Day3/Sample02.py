# Problem #2
# Read a passage from a file. 
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

f = open("D:\python\Day3\string.txt")

givenStr = f.read().lower()

wordList = givenStr.split()

point = False
count = 0

for word in wordList:
    
    if word == 'the' :    

        if point == True:
            count += 1

        point = True

    if word == 'a' :
        point = False

f.close()

print(f"occurence of the's without 'a' in between : {count}")