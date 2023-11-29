Automatically scrolling logger window for Dear PyGui that meets the following requirements. 

- Regularly update
- Scrollable
- Ability to automatically scroll to newest entry
- Ability to show and hide the log with a toggle button
- Text should be selectable
- Automaic scrolling can be turned on and off

[![Automatically scrolling window](https://github.com/DataExplorerUser/dpg_resources/blob/main/autoscroll.gif)](https://github.com/DataExplorerUser/autoscroll/blob/main/autoscroll.py)

*Note*

The code provided in `autoscroll.py` runs perfectly fine by itself. However, if you just process your log file directly with textwrap.fill you will get some very strange line breaking because it doesn't preserve the existing line breaks in the file, so you need to wrap each line individually and then join them with a newline. This is illustrated in the code below.

```Python
    def update_log_display(self):
        FRAME_PADDING = 3
        log_contents = self.read_log_file("latest.log")
        lines = log_contents.splitlines()

        wrapped_lines = [textwrap.fill(line, width=128, replace_whitespace=False) for line in lines]
        wrapped_log = "\n".join(wrapped_lines)

        if wrapped_log:
            dpg.set_item_height(self.log_text, dpg.get_text_size(wrapped_log)[1] + (2 * FRAME_PADDING))
            dpg.set_value(self.log_text, wrapped_log)
        if self.log_autoscroll:
            dpg.configure_item(self.log_text, tracked=True)
        else:
            dpg.configure_item(self.log_text, tracked=False)
```
