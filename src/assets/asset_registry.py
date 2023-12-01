import dearpygui.dearpygui as dpg
from utils import util

# Register all textures assets
with dpg.texture_registry():
    # Add the copy clipboard texture
    copy_clipboard_path = util.resource_path('src/assets/copy_clipboard.png')
    copy_clipboard_width, copy_clipboard_height, copy_clipboard_channels, copy_clipboard_data = dpg.load_image(copy_clipboard_path)
    copy_clipboard = dpg.add_static_texture(width=copy_clipboard_width, height=copy_clipboard_height, default_value=copy_clipboard_data, tag="copy_clipboard")


    