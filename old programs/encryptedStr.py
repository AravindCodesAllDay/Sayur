'''
input is an encrypted  string where there will be chars followed by number. 
The way to decrypt is to repeat the chars, by the number of times. 
Print the decrypted word and its length. If there are any special chars, 
all the chars between the number and special char are ignored.
eg - ac2bd3 means acacbdbdbd. 
ac2acc#cd3 acaccdcdcd
'''

 #PROGRAM :

list1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
list2 = ['0','1','2','3','4','5','6','7','8','9']

message = 'ac2bd#st4'
decrypt = ''
alphabet = ''
result = ''

for x in message:

    if x in list1 :
        alphabet = alphabet + x

    elif x in list2 :
        count = int(x)
        result = result + (alphabet * count)
        alphabet = ''

    else :
        alphabet = ''
        continue

print(result)

        