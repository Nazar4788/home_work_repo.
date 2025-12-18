#Імпортувати модулі 

# Функція відкриття папки

# Циклом пройтись по елементам папки

# Якщо файл = прінт, якщо не файл = прінт і відкриваю папку
from colorama import Fore, Style
import sys
from pathlib import Path

def color(path, ind = '  '):
    dir = Path(path)
    for element in dir.iterdir():
        if element.is_dir():
            print(f"{Fore.BLUE}{ind}{element.name}{Style.RESET_ALL}")
            color(element, ind = ind + '  ')
        else:
            print(f"{Fore.RED}{ind}{element.name}{Style.RESET_ALL}")
        

    
    

path = sys.argv[1]
color(path)
