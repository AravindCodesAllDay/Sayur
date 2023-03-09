'''
Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "* ** * **** "
      Output  - "ILo veIn di aILoveIndi     aILov"
'''
#PROGRAM :

message = 'welcome to madurai'
pattern = '* ** ***'

message = message.replace(' ', '')
final_str = ''

a = 0

for x in message :

    if a >= len(pattern):  

        final_str += ' '
        a = 0
   
    if  pattern[a]== '*':

        final_str += x

    else:

        final_str += ' '

    a += 1

print(final_str)