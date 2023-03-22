'''Write an algorithm to count the number of unique characters from the input one letter at a time . 
If the letter is ‘Z’ , it means end of input .
'''

#PROGRAM : 

list1 = [ ]
character = 0

print("Enter the characters one by one & z to end : ")

while character != 'z' :

    character = input("enter a character : ")
    list1.append(character)

for x in set(list1) :

    count = 0

    for y in list1 : 

        if x == y :

            count += 1
            
    print(f"{x} - {count}")
    
print("END")