from classes import File_processor, Inverted_index
from pathlib import Path  

# Processing the files
directory = r'C:\Users\jeram\Desktop\software-career\projects\inverted-index\text-files'
files = Path(directory).glob('*.txt')
file_processor = File_processor()

for file in files:
    opened = file_processor.open(file)
    cleaned_text = file_processor.clean_text(opened)
    file_processor.add_text(cleaned_text)

id_texts = file_processor.texts # id number: list of words from text    
id_filenames = file_processor.filenames # id number: filenames 

# Adding words to our inverted index and the documents they appear in 
index = Inverted_index()

for key, value in id_texts.items():
    for word in value: 
        index.add_word(word)

display_index = index.index # displays words and the documents they appear in 

for word in display_index:
    for text in id_texts:
        if word in id_texts[text]: 
            display_index[word].append(text)




































