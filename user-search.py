import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport(title='Joogle', width=600, height=300)

def button_callback(): 
    dpg.add_text('Term appears in files...')

with dpg.window(tag="Primary Window"):
    dpg.add_input_text(default_value='enter text')
    dpg.add_button(label='search', callback=button_callback)

    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

