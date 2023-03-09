'''
Write the function mostFrequentLetters(s), that takes a string s, and ignoring case 
(so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most 
frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''

#PROGRAM :

s = "We Attack at Dawn"

s = s.lower()
s = s.replace(' ','')

unique_letters = sorted(set(s))

letter_counts = [0] * len(unique_letters)

for i , letter in enumerate(unique_letters) :

    letter_counts[i] = s.count(letter)

letter_counts_tuples = list(zip(unique_letters, letter_counts))

sorted_letter_counts = sorted(letter_counts_tuples, key=lambda x: (-x[1], x[0]))

result = ''.join([x[0] for x in sorted_letter_counts])

print(result)