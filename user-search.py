from program import display_index, id_filenames
import dearpygui.dearpygui as dpg 

"""
display_index shows each word and the documents they appear in 
id_filenames shows the id numbers that point to the files 
"""

dpg.create_context()

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, World")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="String", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.create_viewport(title="Custom Title", )





