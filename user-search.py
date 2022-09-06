from program import display_index, id_filenames
import dearpygui.dearpygui as dpg 

"""
display_index shows each word and the id for the documents they appear in 
id_filenames shows the id numbers that point to the files 
"""

dpg.create_context()

def search_word(): 
    word = dpg.get_value(input_text)
    if word in display_index:
        with dpg.window():
            dpg.add_text('We found this word in the following documents...')
            for document in display_index[word]:
                dpg.add_text(f"   {id_filenames[document]}")
    else:
        with dpg.window():
            dpg.add_text("word not found in any documents")

with dpg.window(tag="Inverted Index Search"):
    input_text = dpg.add_input_text(default_value="Lebron James")
    search = dpg.add_button(label="search")

    dpg.set_item_callback(search, search_word)

dpg.create_viewport(title="Inverted Index Search", width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Inverted Index Search", True)
dpg.start_dearpygui()
dpg.destroy_context()

# user enters search term or terms 
# program takes the search input
# if input is in display index, link doc numbers to id_filenames and print the names 






