import re
import nltk 


files = ['sample1.txt', 'sample2.txt', 'sample3.txt']


class File_processor: 
    def __init__(self):
        self.fileIDs = {}


    def open(self, file, id): 
        """
        IDs each file and returns file in string format so we can manipulate it 
        """


        self.fileIDs[file] = []
        self.fileIDs[file].append(id)
        open_file = open(file, 'r', encoding='utf8')
        string_repr = ""


        for line in open_file:
            string_repr += line 



        return string_repr 

    
    def clean_text(self, text):
        removed_punc = re.sub(r'[^\w\s]', '', text)
        words = (removed_punc.lower()).split()


        stopwords = nltk.corpus.stopwords.words('english')
        cleaned_text = [word for word in words if word not in stopwords]



        return cleaned_text



file_processor = File_processor()
file_ids = 0
for file in files:
    print('******************************************************************')
    file_ids += 1 
    opened = file_processor.open(file, file_ids)
    clean_file = file_processor.clean_text(opened)
    print(clean_file)

print(file_processor.fileIDs)

    
    
