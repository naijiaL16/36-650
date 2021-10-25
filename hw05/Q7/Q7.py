
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

# Preparing SQL queries to INSERT a record into the database.
sql = """INSERT INTO employee (id,fname,lname)
SELECT generate_series(1,500), 
repeat('XY',1+random()::integer), 
repeat('XY',1+(random()*2)::integer);"""


# Executing the SQL command
cursor.execute(sql)
print("VALUES INSERTED successfully........")
cursor.close()

# Commit the changes in the database
conn.commit()

# Closing the connection
conn.close()
