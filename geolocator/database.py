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
        finally:
            if self.connection:
                self.connection.close()
    
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
        pass

