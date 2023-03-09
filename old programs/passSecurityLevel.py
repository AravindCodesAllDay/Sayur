'''
Print the level of the password security and if the password is acceptable
Weak - only alphabets or only numbers or only special chars
Ok - at least one alphabet, one number and one special char
strong - at least three alphabets, two numbers and one special char
Very strong - same as strong, but at least 16 count
All passwords must be at least 8 chars long. You can use RegEx if you want.
'''

#password validation

list1_count = 0
list2_count = 0
list3_count = 0
lists = []

list1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
list2 = ['0','1','2','3','4','5','6','7','8','9']
list3 = ['!','?','@','#','$','%','^','&','*','_','-','+']

password = input("Enter your password with minimum of 8 characters: ")
length = len(password)

for x in password:
    lists.append(x)

if length >= 8:

    for y in range(length) :

        if lists[y] in list1 :
            list1_count += 1
        elif lists[y] in list2 :
            list2_count += 1
        elif lists[y] in list3 : 
            list3_count += 1

    if list1_count == length or list2_count == length or list3_count == length:
        print("password is weak")
    
    elif list1_count >= 3 and list3_count >= 2 and list3_count >= 1 :

        if length >= 16:
            print("password is Very strong")
        else:
            print("password is strong")

    elif  list1_count >= 1 and list3_count >= 1 and list3_count >= 1 :
        print("password is ok")

    else :
        print("password is normal")

else :
    print("Enter a password atleast with 8 letters")

print("END")