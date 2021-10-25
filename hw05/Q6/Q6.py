
import psycopg2

#Establishing the connection
conn = psycopg2.connect(host="localhost",
                        database="postgres", 
                        user='postgres', 
                        password='riverflows', 
                        port= '5432')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
    id serial, 
    fname varchar(10), 
    lname varchar (10)
)'''

cursor.execute(sql)
print("Table created successfully........")
cursor.close()
conn.commit()

#Closing the connection
conn.close()
