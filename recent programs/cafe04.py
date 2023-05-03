import mysql.connector

cafe = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "1509",
    database = "cafe"
)

mycursor = cafe.cursor()
mycursor.execute("INSERT INTO ItemInventory VALUES(102,10,20,5,20)")
mycursor.execute("SELECT * FROM ItemInventory" )
myresult = mycursor.fetchall()
print(myresult)
