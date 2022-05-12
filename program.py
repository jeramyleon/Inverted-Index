import nltk 
import re

# Functions for cleaning up lines in files 
def remove_stopwords(line):
    words = line.split()
    stopwords = nltk.corpus.stopwords.words('english')
    new_words = [word for word in words if word not in stopwords]
    return new_words 

def remove_punc(line): 
    new_words = re.sub(r'[^\w\s]', '', line)
    return new_words


# Actual program
file_list = ['sample3.txt']
inverted_index = {}


# Prints a list of lists 
for file in file_list:
    words = []
    open_file = open(file, 'r', encoding='utf8')
    
    for line in open_file:
        clean_line = remove_stopwords(remove_punc(line.lower()))
        words.append(clean_line)

    print(words)















    

