import dearpygui.dearpygui as dpg 

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Example Window"):
    dpg.add_button(label='search')
    dpg.add_input_text(label='string', default_value='enter text')


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

