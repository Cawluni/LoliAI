#!/usr/bin/env python

# Main script for LoliAI #
# When wanting to run LoliAI, run this file #
# To do =>


import time,os,platform
loliMEM_color_settings = False # False means that loli mem cant use color for debug use
gloli_Color_settings = False # General Color ability, if true color portion will be activated. if not it wont be.
clear = lambda: os.system('cls') # Clears Terminal Screen
opsys = platform.system()
def init():
    Frames = ['|','/','-','\\'] # Frams for animation
    msg = "Now loading..."
    loading = True
    current = 1 # The current frame Frames[current]
    mods = ['colors','platform','memory']
    n = 1
    # The actual animation/loading #
    while loading == True:
        print(msg+"".join(Frames[current])) # Should print out Msg +Current frame. Visually looks like: LoliAI is now loading.../
        time.sleep(0.1) # 0.1 allows for a super smooth animation!
        current += 1
        clear()
        if n == 1:
            if (opsys == 'Windows'):
                from termcolor import colored, cprint
                from colorama import init
                init(autoreset=True)
                print(('Colors module') , ("["),((cprint("Loaded","green")),("]")))
                a = cprint("LOADED","green") # Format
                n = 2
                loliMEM_color_settings = True # Now colors for Debug
                gloli_color_settings = True # Colors Enabled for General use
            else:
                print("Cannot use colors")
                n = 2
        if n == 2:
            from loliAI import tempMEM
            loli
        if current >= len(Frames):
            current = 1

        # I need to add the fact that it needs to go through eaah thing




def main():
    init()

if __name__ == '__main__':
    main()
