'''
In the input, find the first A and last A, print all the letters between these two A. 
If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
Use functions.
'''

#PROGRAM :

def customerInput():
    cusInput = 'We attack at dawn'
    cusInput = cusInput.replace(' ','').lower()
    return   cusInput

def display(cusInput,index1,index2,x) :

    if cusInput.count(x)>1 and (index1!=index2+1):
        print(cusInput[index1+1:index2])
    elif (index1==index2+1):
        print('value is consecutive, nothing to print')
    elif cusInput.count(x) == 1 :
        print('only one value found')
    else :
        print('value not found')

def main():
    cusInput = customerInput()
    cusInputSorted = sorted(set(cusInput))  
    for x in cusInputSorted :

        if cusInput.count(x) > 1 :

            index1 = cusInput.find(x)
            index2 = cusInput.rfind(x)
            display(cusInput,index1,index2,x)
            break
main()


