import mysql.connector as mysql
import os

class DatabaseManage:
    def __init__(self):
        global con
        host = 'localhost'
        user = 'root'
        password = ''
        database = 'user'
        try:
            con = mysql.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            with con.cursor() as cur:
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS Patients (
                        Id INT AUTO_INCREMENT PRIMARY KEY,
                        Name VARCHAR(255),
                        Patient_id VARCHAR(255),
                        Room_No VARCHAR(255),
                        Fees VARCHAR(255)
                    )"""
                )
        except mysql.Error as e:
            print(f"Error connecting to MySQL Platform: {e}")

    def insertData(self, name, pid, room_no, fees):
        try:
            with con.cursor() as cur:
                cur.execute(
                    "INSERT INTO Patients (Name, Patient_id, Room_No, Fees) VALUES (%s, %s, %s, %s)",
                    (name, pid, room_no, fees)
                )
                con.commit()
        except mysql.Error as e:
            print(f"Error: {e}")

    def viewData(self):
        name = []
        try:
            with con.cursor() as cur:
                cur.execute("SELECT * FROM Patients")
                rows = cur.fetchall()
                for row in rows:
                    data = f"{row[0]} - Name : {row[1]}, Patient_id : {row[2]}, Room_No : {row[3]}, Fees : {row[4]}"
                    name.append(data)
            return name
        except mysql.Error as e:
            print(f"Exception in fetching the values: {e}")

    def delData(self, id):
        try:
            with con.cursor() as cur:
                sql = "DELETE FROM Patients WHERE Id = %s"
                cur.execute(sql, (id,))
                con.commit()
        except mysql.Error as e:
            print(f"Error: {e}")

    def fetchData(self, id):
        data = []
        try:
            with con.cursor() as cur:
                sql = "SELECT * FROM Patients WHERE Id = %s"
                cur.execute(sql, (id,))
                rows = cur.fetchall()
                for row in rows:
                    current = [row[1], row[2], row[3], row[4]]
                    data.append(current)
            return data
        except mysql.Error as e:
            print(f"Exception in fetching the values: {e}")

    def updateData(self, id, name, pid, room_no, fees):
        try:
            with con.cursor() as cur:
                sql = "UPDATE Patients SET Name = %s, Patient_id = %s, Room_No = %s, Fees = %s WHERE Id = %s"
                cur.execute(sql, (name, pid, room_no, fees, id))
                con.commit()
        except mysql.Error as e:
            print(f"Error: {e}")