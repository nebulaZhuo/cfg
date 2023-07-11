import unittest
from isogram import is_isogram

class TestIsIsogram(unittest.TestCase):

    def test_is_isogram_with_isogram_words(self):
        self.assertTrue(is_isogram("ambidextrously"))
        self.assertTrue(is_isogram("uncopyrightable"))
        self.assertTrue(is_isogram("isogram"))

    def test_is_isogram_with_non_isogram_words(self):
        self.assertFalse(is_isogram("hello"))
        self.assertFalse(is_isogram("abca"))
        self.assertFalse(is_isogram("aaaa"))

    def test_is_isogram_with_empty_string(self):
        self.assertTrue(is_isogram(""))

    def test_is_isogram_with_single_letter(self):
        self.assertTrue(is_isogram("a"))
        self.assertTrue(is_isogram("z"))

    def test_is_isogram_with_special_characters(self):
        self.assertFalse(is_isogram("abc!"))
        self.assertFalse(is_isogram("hello!"))
