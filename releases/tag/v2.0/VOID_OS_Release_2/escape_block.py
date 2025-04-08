import ctypes
import sys

def block_escape():
    print("Escape functions disabled. Attempting to press 'Alt+F4'...")

    # Disable Ctrl+Alt+Del (Windows only)
    ctypes.windll.user32.RegisterHotKey(None, 1, 0x0000, 0x11)
    
    while True:
        pass

block_escape()
