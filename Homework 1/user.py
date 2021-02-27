#from user import User
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



connection = create_connection("cis3368-db.c91jggj8tkq9.us-east-2.rds.amazonaws.com", "admin", "!CougarData274894Base?", "cis3368db")


class contacts:
  def __init__(self, contactDetails, creationDate):
    self.contactDetails = contactDetails
    self.creationDate = creationDate
    

class contactList:
  def __init__(self, contact_list=[]):
    self.contact_list = contact_list
  
  def addC(self, contacts):
    dob = datetime.datetime(2000,1,20)
    str_dob = dob.date().isoformat()
    self.contact_list.append(contacts)
    query = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('{}', '{}')".format(input1, input2)
    execute_query(connection, query) 
  
newad = contactList()

input1 = input("contactD")
input2 = input("createD")

new = contacts(input1, input2)

newad.addC(new)