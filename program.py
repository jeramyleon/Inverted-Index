from classes import File_processor, Inverted_index

files = ['sample1.txt', 'sample2.txt', 'sample3.txt']
file_processor = File_processor()

for file in files:
    opened = file_processor.open(file)
    cleaned_text = file_processor.clean_text(opened)
    file_processor.add_text(cleaned_text)

id_texts = file_processor.texts # key, id number: value, filename  
id_filenames = file_processor.filenames # key, id number: value, cleaned_text 


inverted_index = Inverted_index()

for key, value in id_texts.items():
    for word in value: 
        inverted_index.add_word(word)

index_items = inverted_index.index






































"""
index = Inverted_index()
for key, value in data.items(): # add words in texts to inverted index 
    for word in value[1]:
        index.add_word(word)

data2 = index.index # all the words in the text as keys with empty arrays so we can make our inverted index 

# print(data2)


# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)
"""