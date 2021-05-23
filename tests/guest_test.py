import unittest
from classes.room import Room
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room = Room("Boom in this room", 4, 0, 10)
        self.guest = Guest("John Rambo", 30)

    def test_guest_has_name(self):
        self.assertEqual("John Rambo", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(30, self.guest.money)

    def test_reduce_guests_money(self):
        self.guest.reduce_money(self.room.entry_fee)
        self.assertEqual(20, self.guest.money)