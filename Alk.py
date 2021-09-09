# Tha Toolkit
# made by SamuR4II & <insert gay name here>

# Modules
from time import sleep
import os, sys
from os import system, name
import glob


# to clear screen
def clear():
    _ = system('clear')

# What's gonna run first
def main():
    pass


# configure Network settings
def Configure_NetSettings(iface):
    
    print('ur netDevice is : ' + iface)

# for testing purposes
def Help():
    print('there is no help')



if True:

    try:

        if sys.argv[1] == "-h":
            Help()

        if sys.argv[1] == "-sns":
            Configure_NetSettings(str(sys.argv[2]))

    except Exception as e:
        clear()
        Help()