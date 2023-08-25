import string
import os
import random
import hashlib
import colorama
from colorama import Fore
colorama.init(autoreset = True)

def clear():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def code():
    clear()
    print(f"{Fore.GREEN}[:] Minotaur 1.1\n")
    print(f"{Fore.MAGENTA}=====================================")
    print(f"{Fore.RED}0 - Exit the program")
    print(f"{Fore.RED}1 - RNG MD5 hash")
    print(f"{Fore.RED}2 - MD5 hash generated from text")
    print(f"{Fore.MAGENTA}=====================================\n")
    user_input = int(input(f"{Fore.CYAN}Choose a thing: {Fore.RESET}"))

    if user_input == 0:
        clear()
        exit()
    
    if user_input == 1:
        gen = hashlib.new("md5", usedforsecurity = True)
        gen_values = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits)
        gen.update(gen_values.encode())
        print(f"{Fore.RED}Output: {Fore.GREEN}{gen.hexdigest()}")
    
    if user_input == 2:
        text = hashlib.new("md5", usedforsecurity = True)
        clear()
        gen_input = input(f"{Fore.CYAN}What's the text you want to put in the hash? {Fore.RESET}")
        if gen_input:
            text.update(gen_input.encode())
            print(f"{Fore.RED}Output: {Fore.GREEN}{text.hexdigest()}")

code()
