'''
Write a python function that accepts a string and counts the number of upper and lower case letters
'''

#PROGRAM :

def capCounter(string) :

    countUpper = 0
    countLower = 0

    for character in string :

        if character.isupper() :
            countUpper += 1

        elif character.islower() :
            countLower += 1

    return (countUpper, countLower)

def main() :

    string = 'I Love Dosa'  #input("Enter a String : ")
    result = capCounter(string)
    
    print(f'Number of Upper case Letters = {result[0]}')
    print(f'Number of Lower case Letters = {result[1]}')
    
main()
