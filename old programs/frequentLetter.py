'''
5.Write a function most frequent letters(s), that takes a string s and ignoring case
(so "A" and "a" are treated the same),returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''

#PROGRAM : 

word = 'we Attack at dawn'
lettercount = [0]*26
finalStr = ''
a = 0

word = word.lower()
word = word.replace(' ','')

unique = set(word)
unique = list(unique)
unique.sort()

for y in unique :

    lettercount[a] = unique.count(f'{y}') 
    a+=1

for z in range(len(unique)) :

    finalStr += str(unique[lettercount.index(max(lettercount))])
    lettercount[lettercount.index(max(lettercount))] = 0

print(finalStr)