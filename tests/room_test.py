import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Boom in this room")
        
    def test_room_has_name(self):
        self.assertEqual("Boom in this room", self.room.name)