import mysql.connector

cafe = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "1509",
    database = "cafe"
)

mycursor = cafe.cursor()
mycursor.execute("INSERT INTO cafeitems VALUES('coffee', 10, 20, 5, 20, 12, 12)")
mycursor.execute("SELECT * FROM cafeitems" )
myresult = mycursor.fetchall()
print(myresult)
