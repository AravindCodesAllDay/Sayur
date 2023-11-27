'''
Problem #1
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row
'''

alphabet =['a','b','c','d','e','f','g']

limit =  int(input("Enter a number 1-26 : "))

if(limit>0  and limit<25):

    x=0
    string=''

    while(x<limit):
        string += alphabet[x]
        string +=  string.rstrip(string[-1])[::-1]
        print(string)
        x += 1

else:
    print("error enter a value between 1-24")