import sqlite3
import Graphs
# creating file path
dbfile = 'c:/Users/yossa/Downloads/Valid Temp Range Final Project.db'
# Create a SQL connection to our SQLite database
Get_Methods_to_Temp = "SELECT method, Impact_Value FROM 'Impact_Detected' GROUP BY method;"

def get_methods_to_graph(connection):
    with connection:
        return con.exectute(Get_Methods_to_Temp).fetchall()
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute("INSERT INTO 'Impact_Detected'(Impact_Entry,Impact_Value, Impact_Time_Rec)VALUES(13 , 39, '2017-08-07') ")]
con.commit()
table_view = [a for a in cur.execute("SELECT Impact_Entry,Impact_Value,Impact_Time_Rec  FROM 'Impact_Detected'")] 

# here is you table list
#table_view = [a for a in cur.execute("SELECT Impact_Value FROM 'Impact_Detected' WHERE Impact_Entry = 8")]

Graphs.method_temp_range_bar(Get_Methods_to_Temp)
print(table_view[3], type(table_view[3]))
# Be sure to close the connection


con.close()
 