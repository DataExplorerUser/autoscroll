import textwrap
import dearpygui.dearpygui as dpg
import random

dpg.create_context()
dpg.create_viewport(title="Automatically scrolling text", width=600, height=500)
dpg.setup_dearpygui()

words = ("Dear PyGui ", "Scrolling ", "Automatic ", "Toggle ", "Demo ")
log_text = "".join([ words[random.randint(0, 4)] for i in range(300) ])

with dpg.window(label="Log autoscroll", width=700, height=400) as wnd:

    def on_load_log():
        FRAME_PADDING = 3
        text = textwrap.fill(log_text.replace("\n", " "), width=80)
        dpg.set_value("log_field", text)
        dpg.set_item_height("log_field", dpg.get_text_size(text)[1] + (2 * FRAME_PADDING))

    def toggle_auto_scroll():
        if dpg.get_item_configuration("log_field").get("tracked") == True:
            dpg.configure_item("log_field", tracked=False)
        else:
            dpg.configure_item("log_field", tracked=True)

    dpg.add_button(label="Load", callback=on_load_log)
    dpg.add_checkbox(label="Toggle autoscroll", callback=toggle_auto_scroll)

    with dpg.child_window():
        # autoscroll is turned on by default as tracked = True
        dpg.add_input_text(
            tag="log_field", multiline=True, readonly=True, tracked=True, track_offset=1, width=-1, height=0)

dpg.set_viewport_width(750)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
