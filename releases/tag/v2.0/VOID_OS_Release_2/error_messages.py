import time
import random

def random_error_message():
    messages = [
        "System corrupted. Critical failure detected.",
        "Unresponsive system. Restart required.",
        "Unable to locate files. Missing DLL.",
        "Your personal files are now encrypted."
    ]
    
    while True:
        print(random.choice(messages))
        time.sleep(5)

random_error_message()
