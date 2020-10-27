#main file for game; contains main game loop and command parsing

#dependencies
from colorama import Fore, Back, Style

def createWorld():
    print("Choose world size (8-64): ")
    user = input(">")
    try:
        user = int(user)
    except:
        print(Fore.RED + "Specify an integer" + Fore.RESET)
        createWorld()
    if user < 64 and user > 8:
        mainloop()
    else:
        print(Fore.YELLOW + "Specify a number between 8 and 64" + Fore.RESET)
        createWorld()

#main game loop
def mainloop():
    while True:
        print(input(">"))


if __name__ == "__main__":
    print(Back.BLUE + "================================" + Back.RESET)
    print(Back.BLUE + "= Weasle's Text Adventure v1.0 =" + Back.RESET)
    print(Back.BLUE + "================================" + Back.RESET)
    createWorld()