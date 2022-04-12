
import unittest
from src.word_wrap import WordWrap 

class WordWrapTests(unittest.TestCase):
  def setUp(self):
    self.wordWrap = WordWrap()
    
  def test_empty_string_return_itself(self):
    self.assertEqual(self.wordWrap.apply('', 2), '')

  def test_ncolumns_matches_with_space_then_replace_it_with_newline(self):
    self.assertEqual(self.wordWrap.apply('a b', 2), 'a\nb')
    self.assertEqual(self.wordWrap.apply('aa b', 3), 'aa\nb')

  def test_some_words_in_each_line(self):
    self.assertEqual(self.wordWrap.apply('aaa b b cc cc', 4), 'aaa\nb b\ncc\ncc')

if __name__ == '__main__':
  unittest.main()
