import unittest
import importlib

anagram = importlib.import_module('242')
fPairs = importlib.import_module(name='532')

class Testes(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(anagram.Solution().isAnagram('car', 'sad'), False)
        self.assertEqual(anagram.Solution().isAnagram('anagram', 'nagaram'), True)
        self.assertEqual(anagram.Solution().isAnagram('aaa', 'aa'), False)
        self.assertEqual(anagram.Solution().isAnagram('', ''), True)

    def test_findPairs(self):
        self.assertEqual(fPairs.Solution().findPairs([3,1,4,1,5], 2), 2)
        self.assertEqual(fPairs.Solution().findPairs([1,2,3,4,5], 1), 4)
        self.assertEqual(fPairs.Solution().findPairs([1,3,1,5,4], 0), 1)
        self.assertEqual(fPairs.Solution().findPairs([], 0), 0)
