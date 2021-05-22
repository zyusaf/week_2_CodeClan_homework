import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John Rambo")

    def test_guest_has_name(self):
        self.assertEqual("John Rambo", self.guest.name)