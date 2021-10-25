
import numpy as np

# Q1
def transpose_matrix(matrix):
    return np.transpose(matrix)

X = [[10,8], [2,4], [1,7]]

print(transpose_matrix(X))


# Q2
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

new_string = []
def remove_punctations(string):
    # check the type of input
    if(not isinstance(string, str)):
        return("Invalid Input")
    else:
        # for loop in list to create a new string without punctuations
        for i in range(len(string)):
            if string[i] not in punctuations:
                new_string.append(string[i])
    # conbine the list back to a string    
    return ''.join(new_string)

input_string ='Hello in 36-650,& other MSP courses.'

remove_punctations(input_string)


# Q3
def check_trueedits(a,b):
    count,i,j = 0,0,0
    while i < len(a) and j < len(b):
         if a[i] != b[j]:
            if count == 1:
               return 'false'
            if len(a) < len(b):
               j += 1
            elif len(a) > len(b):
               i += 1
            else:
               count,i,j = count+1,i+1,j+1
         else:
            i,j = i+1,j+1
    return 'true'

def check_edits(a,b):
    if(not isinstance(a, str) and not isinstance(b, str)):
        return("Invalid Input")
    # when length difference is larger than 2, edits > 2
    elif(abs(len(a)-len(b))>1):
        return 'false'
    else:
        return check_trueedits(a,b)


check_edits('pale','ple')
check_edits('pales','pale')
check_edits('pale', 'bale')
check_edits('pale', 'bake')

# Q4
def print_triangles(n):
    if (isinstance(n,float)):
        return("Invalid Input")
    elif (n <= 0):
        return("Invalid Input")
    else:
        i,j = 1,2
        for c in range(n):
            for d in range(1, j):
                print(i, end=' ')
                i += 1
            print('')
            j += 1

print_triangles(3.2)
print_triangles(-1)
print_triangles(3)
print_triangles(6)


# Q5
def print_startriangles(n):
    if (isinstance(n,float)):
        return("Invalid Input")
    elif (n <= 0):
        return("Invalid Input")
    else:
        for j in range(1,n+1):
            for i in range(n+1-j):
                print(" ", end='')
            for i in range(j):
                print("*", end=' ')
            print()


print_startriangles(3.4)
print_startriangles(-2)
print_startriangles(5)


# Q6
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
    lname varchar(10)
)'''

cursor.execute(sql)
print("Table created successfully........")
cursor.close()
conn.commit()

#Closing the connection
conn.close()



# Q7
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
print("Table created successfully........")
cursor.close()

# Commit the changes in the database
conn.commit()

# Closing the connection
conn.close()


# Q7
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
print("Table created successfully........")
cursor.close()

# Commit the changes in the database
conn.commit()

# Closing the connection
conn.close()


# Q8
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
sql = """SELECT * FROM employee LIMIT 10;"""

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


# Q9

def palindrome(string):
    if (len(string) < 2):
        return 'true'
    elif(string[0] != string[-1]):
        return 'false'
    else:
        return palindrome(string[1:-1])


palindrome('kayak')
palindrome('hello')