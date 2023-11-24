import dearpygui.dearpygui as dpg
from utils import util

# Register all Fonts
with dpg.font_registry() as main_font_registry:
    default_font_path = util.resource_path('src/assets/Open_Sans/static/OpenSans-Regular.ttf')
    default_font_bold_path = util.resource_path('src/assets/Open_Sans/static/OpenSans-Bold.ttf')
    default_font = dpg.add_font(default_font_path, size=18)
    default_font_bold = dpg.add_font(default_font_bold_path, size=18)
    header1_font = dpg.add_font(default_font_bold_path, size=32)
