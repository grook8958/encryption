import dearpygui.dearpygui as dpg
from utils import util

# Register all textures assets
with dpg.texture_registry(show=True):
    copy_clipboard_path = util.resource_path('src/assets/copy_clipboard.png')
    width, height, channels, data = dpg.load_image(copy_clipboard_path)
    copy_clipboard = dpg.add_static_texture(width=width, height=height, default_value=data, tag="copy_clipboard")




