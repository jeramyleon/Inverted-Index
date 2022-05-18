import re
import nltk 


class File_processor: 
    """
    Class to open, clean and add files so we can easily add them to a inverted index 
    """
    def __init__(self):
        self.fileIDs = {}


    def open(self, file): 
        """
        IDs each file and returns file in string format so we can manipulate it 
        """       
        self.fileIDs[file] = []
        self.fileIDs[file].append(len(self.fileIDs))
        open_file = open(file, 'r', encoding='utf8')
        string_repr = ""

        for line in open_file:
            string_repr += line 

        return string_repr 

    
    def clean_text(self, text):
        """
        Removes punctuation and stopwords
        """
        removed_punc = re.sub(r'[^\w\s]', '', text)
        words = (removed_punc.lower()).split()

        stopwords = nltk.corpus.stopwords.words('english')
        cleaned_text = [word for word in words if word not in stopwords]

        return cleaned_text
    

    def add_text(self, file, text):
        """
        Update file keys with text
        """
        self.fileIDs[file].append(text)
        return None 

class Inverted_index:
    def __init__(self):
        self.index = {}
    
    def update_index(self, word, docId_frequency):
        self.index[word] = []
        self.index[word].append(docId_frequency)
    
    