
import psycopg2

#establishing the connection
conn = psycopg2.connect(host="localhost",
                        database="postgres", 
                        user='postgres', 
                        password='riverflows', 
                        port= '5432')
#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute("""SELECT * FROM employee LIMIT 10;""")

#Fetching 10 rows from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


