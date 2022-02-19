import mysql.connector
<<<<<<< Updated upstream

mydb = mysql.connector.connect(
    host="localhost",
    user="rfidadmin",
    password="rfid_pass"
)

db_cursor = mydb.cursor()
query = "INSERT INTO users (name, id, creation_date) VALUES (%s, %s)"
val = ("Xiaomi ")
=======
import serial
from datetime import datetime

arduino = serial.Serial(port="COM3", baudrate=9600, timeout=.1)

name = input("Inserisci il nome del nuovo utente >> ")

print("Avvicina il dispositivo al lettore...")


def ard_read():
    return arduino.readline()


value = ""
while True:
    value = ard_read()
    if value.decode("utf-8") == "":
        continue
    else:
        break

db_conn = mysql.connector.connect(
    host="localhost",
    user="rfidadmin",
    password="rfid_pass",
    database="rfid"
)

db_cursor = db_conn.cursor()

print(value.decode("utf-8"))

query = "INSERT INTO users (nome, id, data_creazione) VALUES (%s, %s, %s)"
values = (name, value.decode("utf-8"), datetime.now().strftime("%Y-%m-%d"))
db_cursor.execute(query, values)
db_conn.commit()
>>>>>>> Stashed changes
