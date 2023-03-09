'''
Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
'''

#PROGRAM :

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']

itemsInShop = ['mango','apple','orange','grapes']
itemSales = [0,0,0,0]

def processCustomerInput(customerInput):

    list1 = list(customerInput.split())
    global quantities 
    quantities = []

    for i in range(len(itemsInShop)):

        if itemsInShop[i] in list1:

            index = (list1.index(itemsInShop[i])) - 1

            for x in range(len(quantityInWords)):

                if quantityInWords[x] in list1[index] or quantityInDigits[x] in list1[index]:

                    quantities.insert(i,int(quantityInDigits[x]))
        else:

            quantities.insert(i,0)   

        itemSales[i] += quantities[i]

print("(Here are the items that we can serve)")

for item in range(len(itemsInShop)) :

        print(f"{item+1}. {itemsInShop[item].upper()}")

customerInput = input("Enter ur order... : ")
processCustomerInput(customerInput.lower())

for i in range(len(itemsInShop)) :

    print(f"{i+1} - {itemSales[i]} - {itemsInShop[i]}")
