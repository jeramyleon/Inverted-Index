from program import display_index, id_filenames
import dearpygui.dearpygui as dpg 

"""
display_index shows each word and the documents they appear in 
id_filenames shows the id numbers that point to the files 
"""

dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Joogle")
    dpg.add_input_text(default_value="search here")
    dpg.add_button(label="search")
dpg.create_viewport(title="Custom Title", width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()







