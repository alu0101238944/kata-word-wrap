
import unittest
from src.word_wrap import WordWrap 

class WordWrapTests(unittest.TestCase):
  def setUp(self):
    self.wordWrap = WordWrap()
    
  def test_empty_string_return_itself(self):
    self.assertEqual(self.wordWrap.apply(''), '')

if __name__ == '__main__':
  unittest.main()
