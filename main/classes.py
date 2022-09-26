import re
import nltk 

class File_processor: 
    """
    Class to open, clean and add files so we can easily add them to a inverted index 
    """
    def __init__(self):
        self.texts = {}
        self.filenames = {}
     

    def open(self, file): 
        """
        opens a file and returns it in string format
        tags the string representation of said file with a number so we can identify and access it 
        """       
        self.filenames[len(self.filenames) + 1] = file  

        open_file = open(file, 'r', encoding='utf8')
        string_repr = ""

        for line in open_file:
            string_repr += line 

        open_file.close()
        return string_repr 

    
    def clean_text(self, text):
        """
        Removes punctuation and stopwords and returns as a list 
        """
        removed_punc = re.sub(r'[^\w\s]', '', text)
        words = (removed_punc.lower()).split()

        stopwords = nltk.corpus.stopwords.words('english')
        cleaned_text = [word for word in words if word not in stopwords]
        return cleaned_text
    

    def add_text(self, text):
        """
        Adds file keys with text
        """
        self.texts[len(self.texts) + 1] = text
        return None 


class Inverted_index:
    """
    Data structure to hold words and the docIds they appear in 
    """
    def __init__(self):
        self.index = {}
    
    def add_word(self, word):
        self.index[word] = []
    



    
