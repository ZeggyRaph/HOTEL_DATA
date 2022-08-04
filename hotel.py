# import psycopg2 library
import psycopg2

#connect psycopg2
connection = psycopg2.connect("dbname=postgres user=postgres host=localhost password=famousraph1")


#commit transactions
cursor = connection.cursor()



# drop any existing Hotel_Table table
cursor.execute("DROP TABLE Hotel_Table CASCADE;")

# drop any existing Room_Table table
cursor.execute("DROP TABLE IF EXISTS Room_Table;")

#Queue up work into transactions
cursor.execute("""

CREATE TABLE Hotel_Table (
    Hotel_ID INTEGER PRIMARY KEY,
    Name VARCHAR(300),
    Country VARCHAR(300)
    );

    CREATE TABLE Room_Table (
    Room_No INTEGER PRIMARY KEY,   
    Hotel_ID INTEGER REFERENCES Hotel_Table,
    Type VARCHAR(300),
    Price VARCHAR(300)
    );
""")

#THIS IS ONE WAY OF INSERTING DATA 
#Inserting data into the hotel_table

# cursor.execute("INSERT INTO Hotel_Table(Hotel_ID, Name, Country) VALUES (1, 'Eko Hotel', 'Nigeria');")
# cursor.execute("INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (2, 'Hilltop Hotel', 'Tunisia');")
# cursor.execute("INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (3, 'Golden TulipHotel', 'Kenya');")
# cursor.execute("INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (4, 'ClaimontHotel', 'Egypt');")
# cursor.execute("INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (5, 'DevolHotel', 'Nigeria');")
# cursor.execute("INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (6, 'CityBaseHotel', 'Cameroun');")

#Inserting data into the room_table

# cursor.execute("INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES" +
# "(101, 1, 'Smoking', '150')," + 
# "(412, 5, 'Non-Smoking', '200'),"+
# "(126, 4, 'Non-Smoking', '200')," +
# "(128, 6, 'Smoking', '800'),"+
# "(876,2, 'Non-Smoking', '500'),"+
# "(898, 1, 'Smoking', '200'),"+
# "(345, 3, 'Non-Smoking', '1000'),"+
# "(467, 4, 'Non-Smoking', '500'),"+
# "(100, 5, 'Non-Smoking', '150'),"+
# "(120, 4, 'Non-Smoking', '700'),"+
# "(257, 3, 'Non-Smoking', '500'),"+
# "(221, 1, 'Non-Smoking', '150');")

#THIS IS ANOTHER WAY OF INSERTING DATA 
#Inserting data into the hotel_table

# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);',(1, 'Eko Hotel', 'Nigeria'))
# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);', (2, 'Hilltop Hotel', 'Tunisia'))
# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);',(3, 'Golden TulipHotel', 'Kenya'))
# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);', (4, 'ClaimontHotel', 'Egypt'))
# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);', (5, 'DevolHotel', 'Nigeria'))
# cursor.execute('INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%s, %s, %s);',(6, 'CityBaseHotel', 'Cameroun'))

#Inserting data into the room_table

# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (101, 1, 'Smoking', '150'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (412, 5, 'Non-Smoking', '200'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (126, 4, 'Non-Smoking', '200'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);',(128, 6, 'Smoking', '800'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (876,2, 'Non-Smoking', '500'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (898, 1, 'Smoking', '200')) 
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (345, 3, 'Non-Smoking', '1000')) 
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (467, 4, 'Non-Smoking', '500')) 
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (100, 5, 'Non-Smoking', '150')) 
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (120, 4, 'Non-Smoking', '700'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (257, 3, 'Non-Smoking', '500'))
# cursor.execute('INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%s, %s, %s, %s);', (221, 1, 'Non-Smoking', '150')) 



 
#THIS IS YET ANOTHER WAY OF INSERTING DATA
# #Inserting data into the hotel_table 

SQL1 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'
SQL2 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'
SQL3 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'
SQL4 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'
SQL5 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'
SQL6 = 'INSERT INTO Hotel_Table (Hotel_ID, Name, Country) VALUES (%(Hotel_ID)s, %(Name)s, %(Country)s);'

data1 = {
  'Hotel_ID': 1,
  'Name': 'Eko Hotel',
  'Country': 'Nigeria'
}
data2 = {
  'Hotel_ID': 2,
  'Name': 'Hilltop Hotel',
  'Country': 'Tunisia'
}
data3 = {
  'Hotel_ID': 3,
  'Name': 'Golden Tulip Hotel',
  'Country': 'Kenya'
}
data4 = {
  'Hotel_ID': 4,
  'Name': 'Claimont Hotel',
  'Country': 'Egypt'
}
data5 = {
  'Hotel_ID': 5,
  'Name': 'Devol Hotel',
  'Country': 'Nigeria'
}
data6 = {
  'Hotel_ID': 6,
  'Name': 'CityBase Hotel',
  'Country': 'Cameroun'
}

cursor.execute(SQL1, data1)
cursor.execute(SQL2, data2)
cursor.execute(SQL3, data3)
cursor.execute(SQL4, data4)
cursor.execute(SQL5, data5)
cursor.execute(SQL6, data6)

#Inserting data into the room_table
ROOM1 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'
ROOM2 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'
ROOM3 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'
ROOM4 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'
ROOM5 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'
ROOM6 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);' 
ROOM7 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'  
ROOM8 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);' 
ROOM9 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);' 
ROOM10 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);'  
ROOM11 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);' 
ROOM12 = 'INSERT INTO Room_Table (Room_No, Hotel_ID, Type, Price) VALUES (%(Room_No)s, %(Hotel_ID)s, %(Type)s, %(Price)s);' 


room_data1 = {
  'Room_No': 101,
  'Hotel_ID': 1,
  'Type': 'Non-Smoking',
  'Price': '200'
}
room_data2 = {
  'Room_No': 412,
  'Hotel_ID': 5,
  'Type': 'Smoking',
  'Price': '150'
}
room_data3 = {
  'Room_No': 126,
  'Hotel_ID': 4,
  'Type': 'Non-Smoking',
  'Price': '200'
}
room_data4 = {
  'Room_No': 128,
  'Hotel_ID': 6,
  'Type': 'Smoking',
  'Price': '800'
}
room_data5 = {
  'Room_No': 876,
  'Hotel_ID': 2,
  'Type': 'Non-Smoking',
  'Price': '500'
}
room_data6 = {
  'Room_No': 898,
  'Hotel_ID': 1,
  'Type': 'Smoking',
  'Price': '200'
}
room_data7 = {
  'Room_No': 345,
  'Hotel_ID': 3,
  'Type': 'Non-Smoking',
  'Price': '1000'
}
room_data8 = {
  'Room_No': 467,
  'Hotel_ID': 4,
  'Type': 'Non-Smoking',
  'Price': '500'
}
room_data9 = {
  'Room_No': 100,
  'Hotel_ID': 5,
  'Type': 'Non-Smoking',
  'Price': '150'
}
room_data10 = {
  'Room_No': 120,
  'Hotel_ID': 4,
  'Type': 'Non-Smoking',
  'Price': '700'
}
room_data11 = {
  'Room_No': 257,
  'Hotel_ID': 3,
  'Type': 'Non-Smoking',
  'Price': '500'
}
room_data12 = {
  'Room_No': 221,
  'Hotel_ID': 1,
  'Type': 'Non-Smoking',
  'Price': '150'
}


cursor.execute(ROOM1, room_data1)
cursor.execute(ROOM2, room_data2)
cursor.execute(ROOM3, room_data3)
cursor.execute(ROOM4, room_data4)
cursor.execute(ROOM5, room_data5)
cursor.execute(ROOM6, room_data6)
cursor.execute(ROOM7, room_data7)
cursor.execute(ROOM8, room_data8)
cursor.execute(ROOM9, room_data9)
cursor.execute(ROOM10, room_data10)
cursor.execute(ROOM11, room_data11)
cursor.execute(ROOM12, room_data12)




# commit, so it does the executions on the db and persists in the db
connection.commit()

cursor.close()
connection.close()