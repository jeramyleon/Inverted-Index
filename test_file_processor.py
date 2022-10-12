import unittest 
import re
import nltk 
import string
 
from main.classes import File_processor

class TestFileProcessor(unittest.TestCase):

    def test_0_open(self):
        file_processor = File_processor()
        open_file = file_processor.open('text_files/sample1.txt')
        self.assertIsInstance(open_file, str)
        
    def test_1_cleanText(self):
        file_processor = File_processor()
        string_example = "my name is jeramy leon and i am 22 years old"
        cleaned_text = file_processor.clean_text(string_example)

        for character in string_example: 
            self.assertNotIn(character, string.punctuation)


    def test_2_addText(self):
        file_processor = File_processor()
        texts = ["jeramy", "leon", "23"]
        text_amount = 0

        for text in texts: 
            file_processor.add_text(text)
            text_amount += 1 
            self.assertEqual(len(file_processor.texts), text_amount)


if __name__ == '__main__':
    unittest.main()
