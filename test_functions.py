import unittest
import importlib

anagram = importlib.import_module('242')


class Testes(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.Solution().isAnagram('car', 'sad'), False)
        self.assertEqual(anagram.Solution().isAnagram('anagram', 'nagaram'), True)
        self.assertEqual(anagram.Solution().isAnagram('aaa', 'aa'), False)
        self.assertEqual(anagram.Solution().isAnagram('', ''), True)