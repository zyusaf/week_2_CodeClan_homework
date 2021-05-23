import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Toto - Africa")
        
    def test_song_has_details(self):
        self.assertEqual("Toto - Africa", self.song.details)