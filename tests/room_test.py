import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Boom in this room", 4, 0, 10)
        self.guest = Guest("John Rambo", 30)
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

    def test_increase_money_in_till(self):
        self.room.increase_till_money(self.room.entry_fee)
        self.assertEqual(10, self.room.till)

    def test_can_take_entry_fee_from_guest(self):
        room = Room("Boom in this room", 4, 0, 10)
        guest = Guest("John Rambo", 30)
        self.room.take_entry_from_guest_and_add_to_till(room, guest)
        self.assertEqual(20, guest.money)
        self.assertEqual(10, self.room.till)
