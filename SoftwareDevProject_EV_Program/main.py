import sqlite3

# creating file path
dbfile = 'c:/Users/yossa/Downloads/Valid Temp Range Final Project.db'
# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute("INSERT INTO 'Impact_Detected'(Impact_Entry,Impact_Value, Impact_Time_Rec)VALUES(8 , 55, '2017-08-06') ")]
table_view = [a for a in cur.execute("SELECT Impact_Entry,Impact_Value,Impact_Time_Rec  FROM 'Impact_Detected'")]
# here is you table list
print(table_view)

# Be sure to close the connection
con.close()
 