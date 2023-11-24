import subprocess
import platform
import dearpygui.dearpygui as dpg

def copy_to_clipboard(txt):
    if platform.system() == 'Windows':
        cmd='echo '+txt.strip()+'|clip'
    elif platform.system() == 'Darwin' or 'Linux':
        cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

def enter_debug(sender, app_data, user_data):
    dpg.hide_item('window_caesar')
    dpg.hide_item('window_rot13')

def menu_switch(sender, app_data, user_data):
    active_window: str = user_data['active_window']
    selected_window = user_data['selected_window']
    selected_action = user_data['action']
    encryption = active_window.replace('window_', '')
    window_encrypt_item = f'window_encrypt_{encryption}'
    window_decrypt_item = f'window_decrypt_{encryption}'

    print(f'Menu Switch\nActive Window: {active_window}\nSelected Window: {selected_window}\nSelected Action: {selected_action}\nEncryption: {encryption}\nWindow Encrypt: {window_encrypt_item}\nWindow Decrypt: {window_decrypt_item}')
    dpg.hide_item(active_window)
    dpg.show_item(selected_window)
    if (selected_action == 'decrypt'):
        dpg.hide_item(item=window_encrypt_item)
        dpg.show_item(item=window_decrypt_item)
    elif (selected_action == 'encrypt'):
        dpg.show_item(item=window_encrypt_item)
        dpg.hide_item(item=window_decrypt_item)


    

def menu(active: str):
    with dpg.menu_bar():
        with dpg.menu(label="César"):
            dpg.add_menu_item(label='Chiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_caesar', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_caesar', 'action': 'decrypt'})
        with dpg.menu(label="ROT13"):
            dpg.add_menu_item(label='Chiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_rot13', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_rot13', 'action': 'decrypt'})
        with dpg.menu(label="Vigenere"):
            dpg.add_menu_item(label='Chiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_vigenere', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_vignere', 'action': 'decrypt'})
        with dpg.menu(label="Carré de Polybe"):
            dpg.add_menu_item(label='Chiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_polybe', 'action': 'encrypt'})
            dpg.add_menu_item(label='Déchiffré', callback=menu_switch, user_data={'active_window': active, 'selected_window': 'window_polybe', 'action': 'decrypt'})
        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Debug", check=True, callback=enter_debug)

