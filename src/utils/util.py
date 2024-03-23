import subprocess
import platform
import dearpygui.dearpygui as dpg
import os
import sys
import json
import configparser
from themes import theme_registry
from typing import Union


# [{name, value}]
def saveSettings(settings):
    config = configparser.ConfigParser()
    config.read('SETTINGS.INI')
    for setting in settings:
        config['DEFAULT'][setting['name']] = str(setting['value'])
    with open('SETTINGS.INI', 'w') as configfile:
        config.write(configfile)

def saveSetting(name, value):
    return saveSettings([{'name': name, 'value': value}])

def getSetting(name):
    config = configparser.ConfigParser()
    config.read('SETTINGS.INI')
    try:
        value = config.get('DEFAULT', name)
    except Exception:
        value = None
    return value

def saveDefaultSettings():
    settings = [
        {'name': 'language', 'value': 'fr'},
        {'name': 'active_window', 'value': 'caesar'},
    ]
    saveSettings(settings)

# Copy Text to Clipboard 
def copy_to_clipboard(txt):
    if platform.system() == 'Windows':
        cmd='echo '+txt.strip()+'|clip'
    elif platform.system() == 'Darwin' or 'Linux':
        cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

# Enter debug mode
def enter_debug(sender, app_data, user_data):
    dpg.show_item('debug_window')
    dpg.show_style_editor()
    dpg.show_font_manager()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Retrieve the language data file
def _Language():
    file = open(resource_path('src/assets/language.json'))
    Language = json.load(file)
    file.close()
    return Language
Language = _Language()

# Switch between the different encryption windows
def menu_switch(sender, app_data, user_data):
    active_window: str = user_data['active_window']
    selected_window = user_data['selected_window']
    selected_action = user_data['action']
    encryption = active_window.replace('window_', '')
    window_encrypt_item = f'window_encrypt_{encryption}'
    window_decrypt_item = f'window_decrypt_{encryption}'
    saveSetting('active_window', selected_window.replace('window_', ''))
    _print(f'Menu Switch\nActive Window: {active_window}\nSelected Window: {selected_window}\nSelected Action: {selected_action}\nEncryption: {encryption}\nWindow Encrypt: {window_encrypt_item}\nWindow Decrypt: {window_decrypt_item}')
    dpg.hide_item(active_window)
    dpg.show_item(selected_window)
    dpg.set_primary_window(active_window, False)
    dpg.set_primary_window(selected_window, True)
    if (selected_action == 'decrypt'):
        dpg.hide_item(item=window_encrypt_item)
        dpg.show_item(item=window_decrypt_item)
    elif (selected_action == 'encrypt'):
        dpg.show_item(item=window_encrypt_item)
        dpg.hide_item(item=window_decrypt_item)
    

def setValue(item: Union[str, int], text: str):
    return dpg.set_value(item, text)

def setLabel(item: Union[str, int], text: str):
    return dpg.set_item_label(item, text)

def changeLanguage(lang_code):
    encryptions = ['caesar', 'rot13', 'vigenere', 'polybe']
    _print(f'Changing Language to: {lang_code}')
    lang = Language[lang_code]

    for encryption in encryptions:
        # Change the Language of the Menu Bar Items
        setLabel(f'window_caesar_menubar_title_{encryption}', lang[f'{encryption}_name'])
        setLabel(f'window_rot13_menubar_title_{encryption}', lang[f'{encryption}_name'])
        setLabel(f'window_vigenere_menubar_title_{encryption}', lang[f'{encryption}_name'])
        setLabel(f'window_polybe_menubar_title_{encryption}', lang[f'{encryption}_name'])

        # Change the Language of the Menu Bar Sub-Items
        setLabel(f'window_caesar_menubar_option_encrypt_{encryption}', lang['encrypt_action'])
        setLabel(f'window_caesar_menubar_option_decrypt_{encryption}', lang['decrypt_action'])

        setLabel(f'window_rot13_menubar_option_encrypt_{encryption}', lang['encrypt_action'])
        setLabel(f'window_rot13_menubar_option_decrypt_{encryption}', lang['decrypt_action'])
        
        setLabel(f'window_vigenere_menubar_option_encrypt_{encryption}', lang['encrypt_action'])
        setLabel(f'window_vigenere_menubar_option_decrypt_{encryption}', lang['decrypt_action'])
        
        setLabel(f'window_polybe_menubar_option_encrypt_{encryption}', lang['encrypt_action'])
        setLabel(f'window_polybe_menubar_option_decrypt_{encryption}', lang['decrypt_action'])


        setLabel(f'window_{encryption}_menubar_title_settings_language', lang['language_name'])
        setLabel(f'window_{encryption}_menubar_title_settings', lang['settings_name'])

        # Change the Language of the "Encrypted Text" text
        setValue(f'encrypted_text_encrypt_{encryption}', lang['encrypted_text'])
        setValue(f'encrypted_text_decrypt_{encryption}', lang['encrypted_text'])

        # Change the Language of the "Plain Text" text
        setValue(f'plaintext_encrypt_{encryption}', lang['plaintext'])
        setValue(f'plaintext_decrypt_{encryption}', lang['plaintext'])

        # Change the Language of the different encryption titles
        setValue(f'{encryption}_encryption_title', lang[f'{encryption}_encryption_title'])

        # Change the Language of the different buttons
        setLabel(f'btn_encrypt_{encryption}', lang['encrypt_action'])
        setLabel(f'btn_decrypt_{encryption}', lang['decrypt_action'])
        setLabel(f'btn_switch_encrypt_{encryption}', lang['switch_action'])
        setLabel(f'btn_switch_decrypt_{encryption}', lang['switch_action'])

        # Change the Language of the encryption key input
        setValue('vigenere_encrypt_key_text_input', f'{lang["encryption_key"]}...')
        setValue('vigenere_decrypt_key_text_input', f'{lang["encryption_key"]}...')
        setValue('caesar_encrypt_key_text_input', f'{lang["encryption_key"]}...')
        setValue('caesar_decrypt_key_text_input', f'{lang["encryption_key"]}...')
        

        # Change the Language of the copy popup
        setValue(f'text_popup_copy_encrypt_{encryption}', lang['popup_copied'])
        setValue(f'text_popup_copy_decrypt_{encryption}', lang['popup_copied'])
    saveSetting('language', lang_code)
    
    



# Language Change Callback
def select_lang_callback(sender, app_data, user_data):
    selected_lang = dpg.get_item_label(sender)
    dpg.set_value(sender, False)
    dpg.set_value(f"{user_data}_lang_radio", selected_lang)
    for lang in Language:
        if Language[lang]['name'] == selected_lang:
            lang_code = lang
    changeLanguage(lang_code)

def _print(data):
    current_value = dpg.get_value('debug_console')
    new_value = current_value + '\n\n' + str(data)
    dpg.set_value('debug_console', new_value)
    print(data)
    
# Main Menu Bar
def menu(active: str):
    with dpg.menu_bar(tag=f'{active}_menubar'):
        with dpg.menu(label="César", tag=f'{active}_menubar_title_caesar'):
            dpg.add_menu_item(label='Chiffré', tag=f'{active}_menubar_option_encrypt_caesar', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_caesar', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', tag=f'{active}_menubar_option_decrypt_caesar', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_caesar', 'action': 'decrypt'})
        with dpg.menu(label="ROT13", tag=f'{active}_menubar_title_rot13'):
            dpg.add_menu_item(label='Chiffré', tag=f'{active}_menubar_option_encrypt_rot13', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_rot13', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', tag=f'{active}_menubar_option_decrypt_rot13', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_rot13', 'action': 'decrypt'})
        with dpg.menu(label="Vigenere", tag=f'{active}_menubar_title_vigenere'):
            dpg.add_menu_item(label='Chiffré', tag=f'{active}_menubar_option_encrypt_vigenere', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_vigenere', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', tag=f'{active}_menubar_option_decrypt_vigenere', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_vigenere', 'action': 'decrypt'})
        with dpg.menu(label="Carré de Polybe", tag=f'{active}_menubar_title_polybe'):
            dpg.add_menu_item(label='Chiffré', tag=f'{active}_menubar_option_encrypt_polybe', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_polybe', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', tag=f'{active}_menubar_option_decrypt_polybe', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_polybe', 'action': 'decrypt'})
        with dpg.menu(label="Settings", tag=f'{active}_menubar_title_settings'):
            dpg.add_menu_item(label="Debug", check=True, callback=enter_debug)
            with dpg.menu(label="Language", tag=f'{active}_menubar_title_settings_language'):
                with dpg.table(header_row=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.bind_item_theme(dpg.last_item(), theme_registry.nopad_theme)
                    dpg.add_table_column()
                    dpg.add_table_column(init_width_or_weight=18)
                    with dpg.table_row():
                        with dpg.group(horizontal=True, horizontal_spacing=0):
                            dpg.add_text()
                            with dpg.group():
                                dpg.bind_item_theme(dpg.last_item(), theme_registry.sel_theme)
                                dpg.add_selectable(label=Language['en_US']['name'], span_columns=True, callback=select_lang_callback, disable_popup_close=True, user_data=active, tag=f'{active}_en_US_selectable')
                                dpg.add_selectable(label=Language['en_GB']['name'], span_columns=True, callback=select_lang_callback, disable_popup_close=True, user_data=active, tag=f'{active}_en_GB_selectable')
                                dpg.add_selectable(label=Language['fr']['name'], span_columns=True, callback=select_lang_callback, disable_popup_close=True, user_data=active, tag=f'{active}_fr_selectable')
                        dpg.add_radio_button((Language['en_US']['name'], Language['en_GB']['name'], Language['fr']['name']), tag=f"{active}_lang_radio")