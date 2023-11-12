from unittest import TestCase

import responses

from geolocator.client import Client


class TestClient(TestCase):
    def setUp(self):
        self.client = Client("TEST_API_KEY")

    def test_gets_the_geolocation_information(self):
        response = self.client.get(39.7392364, -104.984862)
         
