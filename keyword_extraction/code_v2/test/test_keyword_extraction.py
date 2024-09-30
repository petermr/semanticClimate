from unittest import TestCase
import unittest
import os
from keyword_extraction import KeywordExtraction
import logging


class TestKeywordExtraction(TestCase):


    def setUp(self):
        self.text_path = "../resources/Chapter05_text.txt"
        self.text_path = "../resources/Chapter05_text.txt"


    def test_keyword_init(self):
         
        # Test for text filepath
        type =  os.path.splitext(self.text_path)

        self.assertEqual(type[1], ".txt")



if __name__ == '__main__':
    unittest.main()