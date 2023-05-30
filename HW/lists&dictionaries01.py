########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes"

uniqueWords = {'a'}

for word in sentence.split():
    uniqueWords.add(word)
    #FillinMissingCode
countOfWords = len(uniqueWords)   
print(f'number of unique words is {countOfWords}')

#output
#number of unique words is 10

########## Program 2
