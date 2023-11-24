import dearpygui.dearpygui as dpg

# Register all textures assets
with dpg.texture_registry(show=True):
    width, height, channels, data = dpg.load_image('C:/Users/Eleve/cryptages/src/assets/copy_clipboard.png')
    copy_clipboard = dpg.add_static_texture(width=width, height=height, default_value=data, tag="copy_clipboard")




