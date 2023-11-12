import os

from geolocator.client import Client
from geolocator.database import Database
from geolocator.user_interface import UserInterface

db_path = os.path.join(os.path.dirname(__file__), "db", "database.db")
database = Database()
database.connect(db_path)

client = Client("7e51999498b98449960c3d517772a9e2")
ui = UserInterface()

# wire everything up below:
latitude = float(ui.get_latitude()) 
longitude = float(ui.get_longitude())

current_db_data = database.search(latitude, longitude)

if current_db_data:
    print("Within a 3% range, the latitude and longitude provided match the following city/cities in our database:")
    for city, country_code in current_db_data:
        print(f"{city}, {country_code}")
    
else: 
    print(f"latitude:{latitude}, longitude:{longitude} was not found in database, perfoming API fetch now.")
    #potential security vulnerability known as SQL injection. Change this to use parameterized queries or prepared
    #statements when interacting with a database. Parameterized queries ensure that user input is treated as data rather
    #than executable SQL code, preventing SQL injection attacks.
    response = client.get(latitude, longitude)
    if response:
        city = response[0]["name"]
        country = response[0]["country"]
        database.write(latitude, longitude, city, country)
        print(f"Your latitude and longitude lands on {city}, {country}.")
    else:
        print(f"Error: Unable to fetch data from API.")
