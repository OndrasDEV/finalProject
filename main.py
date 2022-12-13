import os
import random
from allthefunctions import *
from colorama import Fore





def menu():
    print(Fore.CYAN)
    logo()
    print("""
    [1] Shutdown PC
    [2] Restart PC
    [3] Open CMD (non-Admin)
    [4] Open Edge
    [5] Open Chrome
    [6] CLI Calculator
    [7] Open calc.exe
    [8] Generate A Password
    """)
    choice = int(input(""))
    if choice == 1:
        shutdown()
        menu()
    elif choice == 2:
        restart()
        menu()
    elif choice == 3:
        opencmd()
        menu()
    elif choice == 4:
        openedge()
        menu()
    elif choice == 5:
        openchrome()
        menu()
    elif choice == 6:
        calc()
        menu()
    elif choice == 7:
        opencalc()
        menu()
    elif choice == 8:
        passgen()
        menu()
clear()
menu()
