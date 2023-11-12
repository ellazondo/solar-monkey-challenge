from unittest import TestCase

from geolocator.database import Database


class TestDatabase(TestCase):
    def setUp(self):
        self.database = Database()
        self.database.connect(':memory:')

    def test_can_write_to_geolocation_table(self):
        self.database.write(39.7392364, -104.984862, "Denver", "US")
        result = self.database.search(39.7392364, -104.984862)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Denver")
        self.assertEqual(result[1], "US")

    def test_search_within_range(self):
        self.database.write(39.7392364, -104.984862, "Denver", "US")
        result = self.database.search(39.7392365, -104.984863)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Denver")
        self.assertEqual(result[1], "US")  
        

    def test_search_outside_range(self):
        self.database.write(39.7392364, -104.984862, "Denver", "US")
        result = self.database.search(40, -105)
        self.assertIsNone(result)
        

    #Initiate the tests using the following if you're running the script directly
if __name__ == '__main__':
    import unittest
    unittest.main()       
        
