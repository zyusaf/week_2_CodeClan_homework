import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Africa", "Toto")
        
    def test_song_has_name(self):
        self.assertEqual("Africa", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Toto", self.song.artist)