import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Boom in this room", 4)
        self.guest = Guest("John Rambo")
        self.song = Song("Toto - Africa")

    def test_room_has_name(self):
        self.assertEqual("Boom in this room", self.room.name)

    def test_occupants_starts_empty(self):
        self.assertEqual(0, self.room.occupants_queue_length())

    def test_guest_can_be_checked_in(self):
        self.room.add_guest_to_room(self.guest)
        self.assertEqual(1, self.room.occupants_queue_length())

    def test_guest_can_be_checked_out(self):
        self.room.add_guest_to_room(self.guest)
        self.room.remove_guest_from_room(self.guest)
        self.assertEqual(0, self.room.occupants_queue_length())

    def test_song_can_be_added_to_room(self):
        self.room.add_song_to_room(self.song)
        self.assertEqual(1, self.room.song_list_length())

    def test_capacity(self):
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.room.add_guest_to_room(self.guest)
        self.assertEqual(4, self.room.occupants_queue_length())


