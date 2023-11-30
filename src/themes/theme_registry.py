import dearpygui.dearpygui as dpg

# Register the global theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

# Register the btn1_theme
with dpg.theme() as btn1_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 119, 200, 153), category=dpg.mvThemeCat_Core)

# Register the No padding theme
with dpg.theme() as nopad_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_CellPadding, 4, 0)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)


# Register the Select Theme
with dpg.theme() as sel_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 4)