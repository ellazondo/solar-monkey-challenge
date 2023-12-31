import requests


class Client:
    def __init__(self, api_key):
        self._api_key = api_key

    def get(self, latitude, longitude):
        url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={latitude}&lon={longitude}&appid={self._api_key}"
        try:
            response = requests.get(url)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return None
            
        
