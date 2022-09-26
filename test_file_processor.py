import unittest 
from main.classes import File_processor


class TestFileProcessor(unittest.TestCase):

    def testOpen(self):
        file_processor = File_processor()
        open_file = file_processor.open('text_files/sample1.txt')
        self.assertIsInstance(open_file, str)
        
    def testCleanText(self):
        pass
    
    def testAddText(self):
        pass 

if __name__ == '__main__':
    unittest.main()
