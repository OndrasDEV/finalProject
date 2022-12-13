import os
from ondrascalc import *
import random
import string
def shutdown():
    warn = input("Are you sure you want to Shutdown your PC?: ")
    if warn == "y":
        os.system("shutdown /s -t 0")
    else:
        print("Okay")
def restart():
    warn = input("Are you sure you want to Restart your PC?: ")
    if warn == "y":
        os.system("shutdown /r -t 0")
    else:
        print("Okay")
def opencmd():
    os.system("startcmd.bat")
def openedge():
    os.system("startedge.bat")
def openchrome():
    os.system("startchrome.bat")
def calc():
    num1 = int(input("Which number should be first in this Math operation?: "))
    num2 = int(input("Which number should be second in this Math operation?: "))
    symbol = input("[+,-,*,/]Which symbol should be used in this operation?: ")
    if symbol == "+":
        plus(num1,num2)
    elif symbol == "-":
        minus(num1,num2)
    elif symbol == "*":
        krat(num1,num2)
    elif symbol == "/":
        deleno(num1,num2)
def opencalc():
    os.system("startcalc.bat")
def passgen():
    p = "".join(random.choices(string.ascii_letters + string.punctuation + string.digits,k=16))
def clear():
    os.system("cls")
def logo():
    print("""
    
 ▒█████   ███▄    █ ▓█████▄  ██▀███   ▄▄▄        ██████  ▄▄▄▄    ▒█████  ▒██   ██▒
▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▓██ ▒ ██▒▒████▄    ▒██    ▒ ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░
▒██░  ██▒▓██  ▀█ ██▒░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ░ ▓██▄   ▒██▒ ▄██▒██░  ██▒░░  █   ░
▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██   ▒   ██▒▒██░█▀  ▒██   ██░ ░ █ █ ▒ 
░ ████▓▒░▒██░   ▓██░░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒▒██████▒▒░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░
░ ░ ░ ▒     ░   ░ ░  ░ ░  ░   ░░   ░   ░   ▒   ░  ░  ░   ░    ░ ░ ░ ░ ▒   ░    ░  
    ░ ░           ░    ░       ░           ░  ░      ░   ░          ░ ░   ░    ░  
                     ░                                        ░                   

    """)



