import time
import sys

def fake_bootloader():
    print("Starting up...")
    time.sleep(1)
    print("Loading system files...")
    time.sleep(2)
    print("ERROR: Failed to load critical system files.")
    time.sleep(1)
    print("Attempting to restore system...")
    time.sleep(2)
    print("SYSTEM RESTORE FAILED. PRESS ANY KEY TO CONTINUE.")
    time.sleep(3)
    print("System loaded successfully. Welcome to VOID OS.")
    time.sleep(1)

fake_bootloader()
