########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

inputString = input("enter a string : ")#FillinMissingCode
inputString.replace(' ','')
i = 0 #counter to track the chars
newString = ""
if len(inputString)%2 ==1 :
    inputString+=' '
while i < len(inputString):
    newString += inputString[i] + inputString[i+1] #FillinMissingCode (assign the from i, i+1 of inputString)
    newString += " " #add space
    i+=2#check to add the chars at the end
#FillinMissingCode
print (newString)

########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

name = ''
myName = input("Enter ur name : ")#FillinMissingCode
for letter in myName:
    name += letter 
    print(name)

#output:
'''
Enter ur name : aravind
a
ar
ara
arav
aravi
aravin
aravind
'''
        

########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

newSentence = ''
inputSentence = input("enter a sentence : ")#FillinMissingCode
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
     #FillinMissingCode - check if the word has more than one char
    word = word[1:] + firstChar + pigLatinKey
    newSentence += word + ' ' 
print(newSentence)

#output:
'''
enter a sentence : I Love Dosa
Iay oveLay osaDay
'''
        
########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

newSentence = ''
inputSentence = input("Enter a sentence : ")#FillinMissingCode
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']

for word in inputSentence.split(): #gets the word in a sentence
    #take the first chars until a vowel
    first_vowel_index = -1
    #FillinMissingCode - check if the word has more than one char
    for index, char in enumerate(word): #returns both the index and the char in the word
        if char in vowels:
            first_vowel_index = index
            break

    #FillinMissingCode - check if the char is vowel or not    
    word = word[first_vowel_index+1:] + word[:first_vowel_index+1] + pigLatinKey
    newSentence += word + ' '
     
print(newSentence)

#output:
'''
Enter a sentence : I am in Madurai
Iay maay niay duraiMaay
'''