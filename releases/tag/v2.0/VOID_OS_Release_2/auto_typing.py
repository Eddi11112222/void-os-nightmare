import time
import random

def auto_typing():
    phrases = [
        "SYSTEM ERROR DETECTED...",
        "VIRUS FOUND! DELETE SYSTEM FILES...",
        "Your system has been compromised.",
        "Press 'ESC' to continue... Oh wait, you can't."
    ]
    
    while True:
        phrase = random.choice(phrases)
        for char in phrase:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(0.05, 0.2))
        print("\n")
        time.sleep(3)

auto_typing()
