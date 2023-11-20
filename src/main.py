import polybe as Polybe
import vigenere as Vigenere
import caesar as Caesar
import rot13 as Rot13
import dearpygui.dearpygui as dpg

dpg.create_context()

# Set fonts
with dpg.font_registry():
    default_font = dpg.add_font('C:/Users/Eleve/cryptages/src/assets/Open_Sans/static/OpenSans-Regular.ttf', size=18)
    default_font_bold = dpg.add_font('C:/Users/Eleve/cryptages/src/assets/Open_Sans/static/OpenSans-Bold.ttf', size=18)

# Set theme
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
# Set default fonts
dpg.bind_font(font=default_font)

# Callback for encrypt/decrypt buttons
def btn_execute_callback(sender, app_data, user_data):
    # user_data = { input: text_input, output: text_output, action: encrypt/decrypt, encryption: caesar,etc... }
    input = user_data['input']
    output = user_data['output']
    action = user_data['action']
    encryption = user_data['encryption']
    value = dpg.get_value(item=input)
    if encryption == 'caesar':
        if action == 'encrypt':
            # Encrypt the entered text
            output_text = Caesar.encrypt(value)
        elif action == 'decrypt':
            # Decrypt the entered text
            output_text = Caesar.decrypt(value)
    dpg.set_value(item=output, value=output_text)
    print(f'Caesar Encryption/Decryption\nInput: {input}\nOutput: {output}\nAction: {action}\nValue: {value}\nOuput Text: {output_text}\n-----------')

    

# Switch between encrypt and decrypt modes
def btn_switch_callback(sender, app_data, user_data):
    window_encrypt_item = f'window_encrypt_{user_data[0]}'
    window_decrypt_item = f'window_decrypt_{user_data[0]}'
    # user_data = (encryption_method, encrypt/decrypt)
    if (user_data[1] == 'encrypt'):
        dpg.hide_item(item=window_encrypt_item)
        dpg.show_item(item=window_decrypt_item)
        dpg.set_value(item='decrypt_text_input', value=dpg.get_value('encrypt_text_output'))
    elif user_data[1] == 'decrypt':
        dpg.show_item(item=window_encrypt_item)
        dpg.hide_item(item=window_decrypt_item)
        dpg.set_value(item='encrypt_text_input', value=dpg.get_value('decrypt_text_output'))
          

with dpg.window(label="Chiffrement ROT13", width=200, pos=(500,300)):
    dpg.add_text('Work in Progress')

# Encrypt/Decrypt Menu with Caesar Encryption
with dpg.window(label="Chiffrement de César", autosize=True):
    # Encrypt Caesar
    with dpg.child_window(height=340,width=500, label='Chiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=True, tag='window_encrypt_caesar'):
        text = dpg.add_text('Texte au Clair')
        dpg.bind_item_font(text, default_font_bold)
        encrypt_text_input = dpg.add_input_text(default_value='...', height=100, width=450, multiline=True, tag='encrypt_text_input')
        with dpg.group(horizontal=True):
            btn_encrypt_caesar = dpg.add_button(label="Chiffrer", callback=btn_execute_callback)
            btn_switch_caesar = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('caesar','encrypt'))
        dpg.add_text('\n')
        text = dpg.add_text('Texte Chiffré')
        dpg.bind_item_font(text, default_font_bold)
        encrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='encrypt_text_output')
        dpg.set_item_user_data(item=btn_encrypt_caesar, user_data={'input': encrypt_text_input, 'output': encrypt_text_output, 'action': 'encrypt', 'encryption': 'caesar'})
    # Decrypt Caesar
    with dpg.child_window(height=340,width=500, label='Déchiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=False, tag='window_decrypt_caesar'):
        text = dpg.add_text('Texte Chiffré')
        dpg.bind_item_font(text, default_font_bold)
        decrypt_text_input = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, tag='decrypt_text_input')
        with dpg.group(horizontal=True):
            btn_decrypt_caesar = dpg.add_button(label="Déchiffer", user_data='text', callback=btn_execute_callback)
            btn_switch_caesar = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('caesar','decrypt'))
        dpg.add_text('\n')
        text = dpg.add_text('Texte au Clair')
        dpg.bind_item_font(text, default_font_bold)
        decrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='decrypt_text_output')
        dpg.set_item_user_data(item=btn_decrypt_caesar, user_data={'input': decrypt_text_input, 'output': decrypt_text_output, 'action': 'decrypt', 'encryption': 'caesar'})
    # Set local theme
    with dpg.theme() as btn1_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 119, 200, 153), category=dpg.mvThemeCat_Core)
    dpg.bind_item_theme(btn_encrypt_caesar, btn1_theme)
    dpg.bind_item_theme(btn_decrypt_caesar, btn1_theme)


dpg.bind_theme(global_theme)



dpg.show_style_editor()
dpg.show_font_manager()
dpg.create_viewport(title='Chiffrement', width=800, height=600, clear_color=(0, 0, 0, 255), large_icon='', small_icon='')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()