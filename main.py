import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="rfidadmin",
    password="rfid_pass"
)

db_cursor = mydb.cursor()
query = "INSERT INTO users (name, id, creation_date) VALUES (%s, %s)"
val = ("Xiaomi ")
