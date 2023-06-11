########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

def uniqueWords(sentence):
    words = sentence.split()
    wordCounts = {}

    for word in words:

        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
            
    return wordCounts

sentence = "This is a cat and it has a tail and two eyes"
print(f'{uniqueWords(sentence)}')


#output:
'''
{'This': 1, 'is': 1, 'a': 2, 'cat': 1, 'and': 2, 'it': 1, 'has': 1, 'tail': 1, 'two': 1, 'eyes': 1}
'''


