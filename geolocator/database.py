import os
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self,):
        self.connection = None

    def connect(self, db_path):
        try:
            self.connection = sqlite3.connect(db_path)
            self._create_table()
        except Error as error:
            print(error)

    def search(self, latitude, longitude, range=0.03):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT city, country_code FROM geolocation WHERE latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?", (latitude-range, latitude + range, longitude - range, longitude + range))
            result = cursor.fetchall()
            if result: 
                return result
            else: 
                return None
        except Error as error:
            print (f"Error: {error}")
            return None 

    
    def _create_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS geolocation (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                latitude REAL,
                longitude REAL,
                city TEXT,
                country_code TEXT
            )''')
            self.connection.commit()
        except Error as error:
            print(error)
        

    def write(self, latitude, longitude, city, country):
        try:
            cursor = self.connection.cursor()
            cursor.execute( 
            "INSERT INTO geolocation (latitude, longitude, city, country_code) VALUES (?, ?, ?,?)", 
            (latitude, longitude, city, country))
            self.connection.commit()
            print("Data successfully inserted into database")
        except Error as error:
            print(f"Error: {error}")


