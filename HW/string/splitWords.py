########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

inputString = input("Enter a string : ")#FillinMissingCode
inputString = inputString.replace(' ','')
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

#output:
'''
Enter a string : I like to travel in bicycle 
Il ik et ot ra ve li nb ic yc le 
'''