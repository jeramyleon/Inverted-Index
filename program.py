from classes import File_processor

files = ['sample3.txt']

file_processor = File_processor()
for file in files:
    opened = file_processor.open(file)
    clean_text = file_processor.clean_text(opened)
    file_processor.add_text(file, clean_text)


data = file_processor.fileIDs # dictionary with filenames: id's and cleaned texts 
for key, value in data.items():
    print(key, value[0], value[1][0])


