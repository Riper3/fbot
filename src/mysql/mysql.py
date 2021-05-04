import mysql.connector
from env.test import mysqlconfig

connection = mysql.connector.connect(
  host = mysqlconfig['host'],
  user = mysqlconfig['user'],
  password = mysqlconfig['password'],
  database = mysqlconfig['database']
)

def select(select):
    try:
        cursor = connection.cursor(dictionary = True)
        cursor.execute(select)

        records = cursor.fetchall()
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        return records

def insert(insert, data):
    try:
        cursor = connection.cursor()
        cursor.execute(insert, data)

        connection.commit()

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
