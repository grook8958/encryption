import dearpygui.dearpygui as dpg

# Register all Fonts
with dpg.font_registry() as main_font_registry:
    default_font = dpg.add_font('C:/Users/Eleve/cryptages/src/assets/Open_Sans/static/OpenSans-Regular.ttf', size=18)
    default_font_bold = dpg.add_font('C:/Users/Eleve/cryptages/src/assets/Open_Sans/static/OpenSans-Bold.ttf', size=18)
    header1_font = dpg.add_font('C:/Users/Eleve/cryptages/src/assets/Open_Sans/static/OpenSans-Bold.ttf', size=32)