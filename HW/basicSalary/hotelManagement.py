'''
Write a program for a simple hotel management (no DB)
 Create a class for a hotel
 Ask the user for input and create instances
 Print which hotel has most rooms and which hotel has ratings
'''
#define your class structure
class hotel:
    def __init__(self, name, rooms, rating):
        self.name = name
        self.rooms = rooms
        self.rating = rating

def mostRoom(hotels):
    maxRooms = 0
    mostRoomHotel = 0
    #complete code
    for eachInstance in hotels:
        if eachInstance.rooms > maxRooms:
            maxRooms = eachInstance.rooms
            mostRoomHotel = eachInstance
    return mostRoomHotel

def mostRating(hotels):
    maxRating = 0.0
    mostRatingHotel = 0
    for hotel in hotels:
        if hotel.rating > maxRating:
            maxRating = hotel.rating
            mostRatingHotel = hotel
    return mostRatingHotel

noOfHotels = int(input("Enter the number of hotels to register: "))#Get user input.
hotels = []#store the instance in a list

for i in range(noOfHotels):

    #get user input for each of your class properties
    name = input("Enter hotel name: ")
    rooms = int(input("Enter number of rooms: "))
    rating = float(input("Enter hotel rating: "))
    
    #create a new instance of your class
    hotel = hotel(name, rooms, rating)

    hotels.append(hotel)

print(f"Hotel with the most rooms: {mostRoom(hotels).name}")

print(f"Hotel with the highest rating:{mostRating(hotels).name}")

