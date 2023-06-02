######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.
print()
for i in range(7,16+1):
    table = ''
    for j in range(1,12+1):
        table += str(i) + '*' + str(j) + '=' + str(i*j) + '\t'
    print(f"{table}")

#output:
'''
7*1=7   7*2=14  7*3=21  7*4=28  7*5=35  7*6=42  7*7=49   7*8=56   7*9=63   7*10=70   7*11=77   7*12=84
8*1=8   8*2=16  8*3=24  8*4=32  8*5=40  8*6=48  8*7=56   8*8=64   8*9=72   8*10=80   8*11=88   8*12=96
9*1=9   9*2=18  9*3=27  9*4=36  9*5=45  9*6=54  9*7=63   9*8=72   9*9=81   9*10=90   9*11=99   9*12=108
10*1=10 10*2=20 10*3=30 10*4=40 10*5=50 10*6=60 10*7=70  10*8=80  10*9=90  10*10=100 10*11=110 10*12=120
11*1=11 11*2=22 11*3=33 11*4=44 11*5=55 11*6=66 11*7=77  11*8=88  11*9=99  11*10=110 11*11=121 11*12=132
12*1=12 12*2=24 12*3=36 12*4=48 12*5=60 12*6=72 12*7=84  12*8=96  12*9=108 12*10=120 12*11=132 12*12=144
13*1=13 13*2=26 13*3=39 13*4=52 13*5=65 13*6=78 13*7=91  13*8=104 13*9=117 13*10=130 13*11=143 13*12=156
14*1=14 14*2=28 14*3=42 14*4=56 14*5=70 14*6=84 14*7=98  14*8=112 14*9=126 14*10=140 14*11=154 14*12=168
15*1=15 15*2=30 15*3=45 15*4=60 15*5=75 15*6=90 15*7=105 15*8=120 15*9=135 15*10=150 15*11=165 15*12=180
16*1=16 16*2=32 16*3=48 16*4=64 16*5=80 16*6=96 16*7=112 16*8=128 16*9=144 16*10=160 16*11=176 16*12=192
'''