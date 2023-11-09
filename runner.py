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
ui.hello() 
ui.goodbye()
