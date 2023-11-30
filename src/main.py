import dearpygui.dearpygui as dpg

# Create de DPG context
dpg.create_context()

# Main Imports
from themes import font_registry
from themes import theme_registry
from assets import asset_registry
import polybe as Polybe
import vigenere as Vigenere
import caesar as Caesar
import rot13 as ROT13
from utils import util
import time

# Create DPG Viewport
dpg.create_viewport(title='Chiffrement', width=800, height=600, clear_color=(0, 0, 0, 255))

# Set Theme & Fonts
dpg.bind_font(font_registry.default_font)
dpg.bind_theme(theme_registry.global_theme)


# Callback for encrypt/decrypt buttons
def btn_execute_callback(sender, app_data, user_data):
    # user_data = { input: text_input, output: text_output, action: encrypt/decrypt, encryption: caesar,etc... }
    action = user_data['action']
    encryption = user_data['encryption']
    input = user_data['input']
    output = user_data['output']
    value = dpg.get_value(item=input)
    output_text = ''
    if encryption == 'caesar':
        if action == 'encrypt':
            # Encrypt the entered text
            output_text = Caesar.encrypt(value)
        elif action == 'decrypt':
            # Decrypt the entered text
            output_text = Caesar.decrypt(value)
    if encryption == 'rot13':
        if action == 'encrypt':
            # Encrypt the entered text
            output_text = ROT13.encrypt(value)
        elif action == 'decrypt':
            # Decrypt the entered text
            output_text = ROT13.decrypt(value)
    if encryption == 'vigenere':
        if action == 'encrypt':
            # Encrypt the entered text
            output_text = Vigenere.encrypt(value, dpg.get_value('vigenere_encrypt_key_text_input'))
        elif action == 'decrypt':
            # Decrypt the entered text
            output_text = Vigenere.decrypt(value, dpg.get_value('vigenere_decrypt_key_text_input'))
    if encryption == 'polybe':
        if action == 'encrypt':
            # Encrypt the entered text
            output_text = Polybe.encrypt(value)
        elif action == 'decrypt':
            # Decrypt the entered text
            output_text = Polybe.decrypt(value)
    dpg.set_value(item=output, value=output_text)
    util._print(f'{encryption} Encryption/Decryption\nInput: {input}\nOutput: {output}\nAction: {action}\nValue: {value}\nOuput Text: {output_text}\n-----------')

# Switch between encrypt and decrypt modes
def btn_switch_callback(sender, app_data, user_data):
    encryption = user_data[0]
    window_encrypt_item = f'window_encrypt_{encryption}'
    window_decrypt_item = f'window_decrypt_{encryption}'
    decrypt_text_input = f'decrypt_text_input_{encryption}'
    encrypt_text_input = f'decrypt_text_input_{encryption}'
    encrypt_text_output = f'encrypt_text_output_{encryption}'
    decrypt_text_output = f'decrypt_text_output_{encryption}'
    # user_data = (encryption_method, encrypt/decrypt)
    if (user_data[1] == 'encrypt'):
        dpg.hide_item(item=window_encrypt_item)
        dpg.show_item(item=window_decrypt_item)
        dpg.set_value(item=decrypt_text_input, value=dpg.get_value(encrypt_text_output))
    elif user_data[1] == 'decrypt':
        dpg.show_item(item=window_encrypt_item)
        dpg.hide_item(item=window_decrypt_item)
        dpg.set_value(item=encrypt_text_input, value=dpg.get_value(decrypt_text_output))
    
# Copy to Clipboard the output
def btn_copy_callback(sender, app_data, user_data):
    output = user_data[0]
    popup = user_data[1]
    dpg.show_item(popup)
    util.copy_to_clipboard(dpg.get_value(output))
    time.sleep(2)
    dpg.hide_item(popup)

# Initialize the app
def init():
    # Retrieve last used Language and Window
    lang = util.getSetting('language') or 'fr'
    window = util.getSetting('active_window') or 'caesar'

    # Change the language
    dpg.set_value(f"window_{window}_lang_radio", util.Language[lang]['name'])
    util.changeLanguage(lang)

    # Set the correct window
    util.menu_switch(sender=None, app_data=None, user_data={'active_window': 'window_caesar', 'selected_window': f'window_{window}', 'action': 'encrypt'})

# ROT13 Main Window
with dpg.window(label="Chiffrement ROT13", height=600, width=800, pos=(0,0), tag='window_rot13', show=False, no_close=True, no_move=True, no_resize=True, no_title_bar=True,):
    dpg.bind_item_font(dpg.add_text('Chiffrement ROT13', tag='rot13_encryption_title'), font=font_registry.header1_font)
    dpg.add_text('\n')

    # Encrypt ROT13
    with dpg.child_window(height=360,width=500, label='Chiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=True, tag='window_encrypt_rot13'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_encrypt_rot13'), font_registry.default_font_bold)
        encrypt_text_input = dpg.add_input_text(default_value='...', height=100, width=450, multiline=True, tag='encrypt_text_input_rot13')
        
        # Encrypt & Switch Buttons
        with dpg.group(horizontal=True):
            btn_encrypt_rot13 = dpg.add_button(label="Chiffrer", callback=btn_execute_callback, tag='btn_encrypt_rot13')
            btn_switch_rot13 = dpg.add_button(label='Inverser', callback=btn_switch_callback, user_data=('rot13','encrypt'), tag='btn_switch_encrypt_rot13')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_encrypt_rot13'), font_registry.default_font_bold)
        encrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='encrypt_text_output_rot13')
        dpg.set_item_user_data(item=btn_encrypt_rot13, user_data={'input': encrypt_text_input, 'output': encrypt_text_output, 'action': 'encrypt', 'encryption': 'rot13'})
        
        # Copy to clipboard button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(encrypt_text_output, 'popup_copy_encrypt_rot13'))
        
        # Copy to clipboard popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_encrypt_rot13'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_encrypt_rot13')

    # Decrypt ROT13
    with dpg.child_window(height=360,width=500, label='Déchiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=False, tag='window_decrypt_rot13'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_decrypt_rot13'), font_registry.default_font_bold)
        decrypt_text_input = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, tag='decrypt_text_input_rot13')

        # Decrypt & Switch buttons
        with dpg.group(horizontal=True):
            btn_decrypt_rot13 = dpg.add_button(label="Déchiffer", user_data='text', callback=btn_execute_callback, tag='btn_decrypt_rot13')
            btn_switch_rot13 = dpg.add_button(label='Inverser', callback=btn_switch_callback, user_data=('rot13','decrypt'), tag='btn_switch_decrypt_rot13')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_decrypt_rot13'), font_registry.default_font_bold)
        decrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='decrypt_text_output_rot13')
        dpg.set_item_user_data(item=btn_decrypt_rot13, user_data={'input': decrypt_text_input, 'output': decrypt_text_output, 'action': 'decrypt', 'encryption': 'rot13'})

        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(decrypt_text_output, 'popup_copy_decrypt_rot13'))

        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_decrypt_rot13'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_decrypt_rot13')

        # Styles
        dpg.bind_item_theme(btn_encrypt_rot13, theme_registry.btn1_theme)
        dpg.bind_item_theme(btn_decrypt_rot13, theme_registry.btn1_theme)

    # Menu Bar
    util.menu('window_rot13')

    
# Caesar Main Window
with dpg.window(height=600, width=800, pos=(0,0), no_close=True, no_move=True, no_resize=True, no_title_bar=True, tag='window_caesar'):
    dpg.bind_item_font(dpg.add_text('Chiffrement César', tag='caesar_encryption_title'), font=font_registry.header1_font)
    dpg.add_text('\n')

    # Encrypt Caesar
    with dpg.child_window(height=360,width=500, label='Chiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=True, tag='window_encrypt_caesar'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_encrypt_caesar'), font_registry.default_font_bold)
        encrypt_text_input = dpg.add_input_text(default_value='...', height=100, width=450, multiline=True, tag='encrypt_text_input_caesar')

        # Encrypt & Switch Button
        with dpg.group(horizontal=True):
            btn_encrypt_caesar = dpg.add_button(label="Chiffrer", callback=btn_execute_callback, tag='btn_encrypt_caesar')
            btn_switch_caesar = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('caesar','encrypt'), tag='btn_switch_encrypt_caesar')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_encrypt_caesar'), font_registry.default_font_bold)
        encrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='encrypt_text_output_caesar')
        dpg.set_item_user_data(item=btn_encrypt_caesar, user_data={'input': encrypt_text_input, 'output': encrypt_text_output, 'action': 'encrypt', 'encryption': 'caesar'})

        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(encrypt_text_output, 'popup_copy_encrypt_caesar'))

        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_encrypt_caesar'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_encrypt_caesar')

    # Decrypt Caesar
    with dpg.child_window(height=360,width=500, label='Déchiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=False, tag='window_decrypt_caesar'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_decrypt_caesar'), font_registry.default_font_bold)
        decrypt_text_input = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, tag='decrypt_text_input_caesar')

        # Decrypt & Switch Button
        with dpg.group(horizontal=True):
            btn_decrypt_caesar = dpg.add_button(label="Déchiffer", user_data='text', callback=btn_execute_callback, tag='btn_decrypt_caesar')
            btn_switch_caesar = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('caesar','decrypt'), tag='btn_switch_decrypt_caesar')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_decrypt_caesar'), font_registry.default_font_bold)
        decrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='decrypt_text_output_caesar')
        dpg.set_item_user_data(item=btn_decrypt_caesar, user_data={'input': decrypt_text_input, 'output': decrypt_text_output, 'action': 'decrypt', 'encryption': 'caesar'})
        
        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(decrypt_text_output, 'popup_copy_decrypt_caesar'))
        
        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_decrypt_caesar'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_decrypt_caesar')

        # Styles
        dpg.bind_item_theme(btn_encrypt_caesar, theme_registry.btn1_theme)
        dpg.bind_item_theme(btn_decrypt_caesar, theme_registry.btn1_theme)
    
    # Menu Bar
    util.menu('window_caesar')
    
# Vigenere Main Window
with dpg.window(label="Chiffrement de Vigenere", height=600, width=800, pos=(0,0), tag='window_vigenere', show=False, no_close=True, no_move=True, no_resize=True, no_title_bar=True):
    dpg.bind_item_font(dpg.add_text('Chiffrement de Vigenere', tag='vigenere_encryption_title'), font_registry.header1_font)
    dpg.add_text('\n')

    # Encrypt Vigenere
    with dpg.child_window(height=360,width=500, label='Chiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=True, tag='window_encrypt_vigenere'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_encrypt_vigenere'), font_registry.default_font_bold)
        encrypt_text_input = dpg.add_input_text(default_value='...', height=100, width=450, multiline=True, tag='encrypt_text_input_vigenere')
        
        # Encrypt, Switch Buttons & Encryption Key Input
        with dpg.group(horizontal=True):
            btn_encrypt_vigenere = dpg.add_button(label="Chiffrer", callback=btn_execute_callback, tag='btn_encrypt_vigenere')
            dpg.add_input_text(default_value='Clé de Chiffrement', no_spaces=True, tag='vigenere_encrypt_key_text_input')
            btn_switch_vigenere = dpg.add_button(label='Inverser', callback=btn_switch_callback, user_data=('vigenere','encrypt'), tag='btn_switch_encrypt_vigenere')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_encrypt_vigenere'), font_registry.default_font_bold)
        encrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='encrypt_text_output_vigenere')
        dpg.set_item_user_data(item=btn_encrypt_vigenere, user_data={'input': encrypt_text_input, 'output': encrypt_text_output, 'action': 'encrypt', 'encryption': 'vigenere'})
        
        # Copy to clipboard button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(encrypt_text_output, 'popup_copy_encrypt_vigenere'))
        
        # Copy to clipboard popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_encrypt_vigenere'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_encrypt_vigenere')

    # Decrypt Vigenere
    with dpg.child_window(height=360,width=500, label='Déchiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=False, tag='window_decrypt_vigenere'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_decrypt_vigenere'), font_registry.default_font_bold)
        decrypt_text_input = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, tag='decrypt_text_input_vigenere')

        # Decrypt & Switch buttons
        with dpg.group(horizontal=True):
            btn_decrypt_vigenere = dpg.add_button(label="Déchiffer", user_data='text', callback=btn_execute_callback, tag='btn_decrypt_vigenere')
            dpg.add_input_text(default_value='Clé de Chiffrement...', no_spaces=True, tag='vigenere_decrypt_key_text_input')
            btn_switch_vigenere = dpg.add_button(label='Inverser', callback=btn_switch_callback, user_data=('vigenere','decrypt'), tag='btn_switch_decrypt_vigenere')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_decrypt_vigenere'), font_registry.default_font_bold)
        decrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='decrypt_text_output_vigenere')
        dpg.set_item_user_data(item=btn_decrypt_vigenere, user_data={'input': decrypt_text_input, 'output': decrypt_text_output, 'action': 'decrypt', 'encryption': 'vigenere'})

        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(decrypt_text_output, 'popup_copy_decrypt_vigenere'))

        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_decrypt_vigenere'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_decrypt_vigenere')

        # Styles
        dpg.bind_item_theme(btn_encrypt_vigenere, theme_registry.btn1_theme)
        dpg.bind_item_theme(btn_decrypt_vigenere, theme_registry.btn1_theme)

    # Menu Bar
    util.menu('window_vigenere')

# Polybe Main Window
with dpg.window(height=600, width=800, pos=(0,0), no_close=True, no_move=True, no_resize=True, no_title_bar=True, tag='window_polybe'):
    dpg.bind_item_font(dpg.add_text('Chiffrement Polybe', tag='polybe_encryption_title'), font=font_registry.header1_font)
    dpg.add_text('\n')

    # Encrypt Polybe
    with dpg.child_window(height=360,width=500, label='Chiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=True, tag='window_encrypt_polybe'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_encrypt_polybe'), font_registry.default_font_bold)
        encrypt_text_input = dpg.add_input_text(default_value='...', height=100, width=450, multiline=True, tag='encrypt_text_input_polybe')

        # Encrypt & Switch Button
        with dpg.group(horizontal=True):
            btn_encrypt_polybe = dpg.add_button(label="Chiffrer", callback=btn_execute_callback, tag='btn_encrypt_polybe')
            btn_switch_polybe = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('polybe','encrypt'), tag='btn_switch_encrypt_polybe')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_encrypt_polybe'), font_registry.default_font_bold)
        encrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='encrypt_text_output_polybe')
        dpg.set_item_user_data(item=btn_encrypt_polybe, user_data={'input': encrypt_text_input, 'output': encrypt_text_output, 'action': 'encrypt', 'encryption': 'polybe'})

        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(encrypt_text_output, 'popup_copy_encrypt_polybe'))

        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_encrypt_polybe'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_encrypt_polybe')

    # Decrypt Polybe
    with dpg.child_window(height=360,width=500, label='Déchiffrer', no_scrollbar=True, no_scroll_with_mouse=True, show=False, tag='window_decrypt_polybe'):
        # Input
        dpg.bind_item_font(dpg.add_text('Texte Chiffré', tag='encrypted_text_decrypt_polybe'), font_registry.default_font_bold)
        decrypt_text_input = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, tag='decrypt_text_input_polybe')

        # Decrypt & Switch Button
        with dpg.group(horizontal=True):
            btn_decrypt_polybe = dpg.add_button(label="Déchiffer", user_data='text', callback=btn_execute_callback, tag='btn_decrypt_polybe')
            btn_switch_polybe = dpg.add_button(label='Inversé', callback=btn_switch_callback, user_data=('polybe','decrypt'), tag='btn_switch_decrypt_polybe')
        dpg.add_text('\n')

        # Output
        dpg.bind_item_font(dpg.add_text('Texte au Clair', tag='plaintext_decrypt_polybe'), font_registry.default_font_bold)
        decrypt_text_output = dpg.add_input_text(default_value="...", height=100, width=450, multiline=True, enabled=False, tag='decrypt_text_output_polybe')
        dpg.set_item_user_data(item=btn_decrypt_polybe, user_data={'input': decrypt_text_input, 'output': decrypt_text_output, 'action': 'decrypt', 'encryption': 'polybe'})
        
        # Copy to Clipboard Button
        dpg.add_image_button(texture_tag=asset_registry.copy_clipboard, callback=btn_copy_callback, user_data=(decrypt_text_output, 'popup_copy_decrypt_polybe'))
        
        # Copy to Clipboard Popup
        with dpg.popup(dpg.last_item(), max_size=(-10, -25), tag='popup_copy_decrypt_polybe'):
            dpg.add_text("Copied", color=(0,255,0), tag='text_popup_copy_decrypt_polybe')

        # Styles
        dpg.bind_item_theme(btn_encrypt_polybe, theme_registry.btn1_theme)
        dpg.bind_item_theme(btn_decrypt_polybe, theme_registry.btn1_theme)
    
    # Menu Bar
    util.menu('window_polybe')

with dpg.window(label='Debug', height=200, width=200, show=False, tag='debug_window'):
    dpg.add_text('Console')
    with dpg.child_window(label='Console', autosize_x=True, autosize_y=True):
        dpg.add_text('', tag='debug_console')


# Startup the GUI
dpg.setup_dearpygui()
init()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()