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
    latitude, longitude = current_db_data
    print(f"{latitude}, {longitude} was already found in the database")
else: 
    print("not found in database: perfoming API fetch")

# response = client.get(latitude, longitude)

# if response:
#     city = response[0]["name"]
#     country = response[0]["country"]
#     database.write(latitude, longitude, city, country)
#     print(f"Your latitude and longitude lands on {city}, {country}.")

# else:
#     print(f"Error: Unable to fetch data from API.")
