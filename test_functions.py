import unittest
import importlib

anagram = importlib.import_module('242')
fPairs = importlib.import_module(name='532')
majority = importlib.import_module('169')
longest = importlib.import_module('720')

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

    def test_majorityElement(self):
        self.assertEqual(majority.Solution().majorityElement([3,2,3]), 3)
        self.assertEqual(majority.Solution().majorityElement([2,2,1,1,1,2,2]), 2)
        self.assertEqual(majority.Solution().majorityElement([6,5,5]), 5)
        self.assertEqual(majority.Solution().majorityElement([]), None)

    def test_longestWord(self):
        self.assertEqual(longest.Solution().longestWord(["w","wo","wor","worl","world"]), 'world')
        self.assertEqual(longest.Solution().longestWord(["a","banana","app","appl","ap","apply","apple"]), 'apple')
        self.assertEqual(longest.Solution().longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]), 'yodn')
