############## Problem  1 #################### 
#Ask first friend the movies they like. Save it in a list
#Ask another friend the same question. If the movie is in the first friend's list, 
#Print "You both like "name of the color"
#Continue until they is atleast 3 movies they both like

#init variables
movieslist=[]
movieslist2=[]
print("Friend 1")
while (True) :
    movies = input(f"What movie you like? n to exit : " )
    if movies=='n' :
        break
    #convert movies into a List
    movieslist.append(movies)
    #FillinMissingCode
print("Friend 2")
print("Get atleast 3 common movies")
commonMovieCount = 0
while (True) :
    #ask the second friend for one movie at a time
    movie = input("Enter a movie you like : " )#FillinMissingCode
    #Check if this movie is in the movie list
    if movie in movieslist:
        #FillinMissingCode
        #if present, 
        commonMovieCount += 1
        movieslist2.append(movie)
     
    #check if we reached the max
    if(commonMovieCount >= 3):
        break;
    else:
        print (f"common count = {commonMovieCount} ")

print (f'common movies = {movieslist2}') #FillinMissingCode - list all the common movies

#output:
'''
Friend 1
What movie you like? n to exit : josee
What movie you like? n to exit : your name
What movie you like? n to exit : silent voice
What movie you like? n to exit : owl's moving castle
What movie you like? n to exit : sprited away
What movie you like? n to exit : n
Friend 2
Get atleast 3 common movies
Enter a movie you like : sprited away
common count = 1
Enter a movie you like : dororo
common count = 1
Enter a movie you like : silent voice
common count = 2
Enter a movie you like : children of the sea
common count = 2
Enter a movie you like : your name
common movies = ['sprited away', 'silent voice', 'your name']
'''