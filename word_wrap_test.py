
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
    self.assertEqual(self.wordWrap.apply('12 34', 4), '12\n34')
    self.assertEqual(self.wordWrap.apply('aaa b c', 4), 'aaa\nb c')
    self.assertEqual(self.wordWrap.apply('hello world', 7), 'hello\nworld')
    self.assertEqual(self.wordWrap.apply('1 234 56 7890 123 4 567890 1234', 10), '1 234 56\n7890 123\n4 567890\n1234')
    self.assertEqual(self.wordWrap.apply('012345678901234', 6), '012345\n678901\n234')
    # self.assertEqual(self.wordWrap.apply('greedy whenthewordistoolong', 6), 'greedy\nwhenth\newordi\nstoolo\nng')
    # self.assertEqual(self.wordWrap.apply('greedy whenthewordistoolong', 7), 'greedy\nwhenthe\nwordist\noolong')

if __name__ == '__main__':
  unittest.main()
