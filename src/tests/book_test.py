import unittest
from entities.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("a","b","c","d",2014)

    def test_format(self):
        correct_answer = """@book{a2014,
  author    = "a",
  title     = "b",
  publisher = "c",
  address   = "d",
  year      = 2014
}"""
        self.assertEqual(correct_answer,self.book.format())