word = 'we Attack at dawn'
lettercount = [0]*26
unique = {}

word = [*(word.lower()).replace(' ','')]

for x,letter in enumerate(word) :

    lettercount[x] = word.count(letter)
    unique.update({letter: lettercount[x]})

print(unique.items())
