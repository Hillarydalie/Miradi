import unittest
from models import Location
Location = location.Location


Class LocationTest(unittest.TestCase):
    def setUp(self):
        set.new_location = Location('kenya', 'nairobi', 'construction')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))


if __name__ == '__main__':
    unittest.main
