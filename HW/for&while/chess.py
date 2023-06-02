######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

for i in range(8):
    a=''
    for j in range(8):
        if (j+i)%2 == 0:
            a+=' b'
            continue
        a+=' \u25A0'
    print(a)

#output:
'''
 b ■ b ■ b ■ b ■
 ■ b ■ b ■ b ■ b
 b ■ b ■ b ■ b ■
 ■ b ■ b ■ b ■ b
 b ■ b ■ b ■ b ■
 ■ b ■ b ■ b ■ b
 b ■ b ■ b ■ b ■
 ■ b ■ b ■ b ■ b
'''