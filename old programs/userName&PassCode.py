'''
Check if the username and password is correct. 
Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
name of the company mentioned in the username, followed by any 3 numbers.
eg username : myname@sayur.com. password - mnamesay123 
'''

#PROGRAM:

'''
username = input("Enter ur user name : ")
password = input("Enter ur password")
'''    

username = "aravind@sit.com"
password = "aaindsit123"
passWord = ''
num = ['1','2','3','4','5','6','7','8','9']

if '@' in username and ('.com' in username or '.edu' in username or '.tech' in username or '.org' in username):

    a = username.index('@')

    passWord = username[0] +  username[2] + username[a-3] +  username[a-2] + username[a-1] +username[a+1] +  username[a+2] + username[a+3]
    passWord = passWord + password[-3] + password[-2] + password[-1]

    if password[-1] in num and password[-2] in num and password[-3] in num and password == passWord :

        print("Password is correct....")

    else:

        print("Your password is wrong...")

else:

    print("Enter a valid username...")    