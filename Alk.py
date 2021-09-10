# Tha Toolkit
# made by SamuR4II

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

    space = ' ' * 2
    
    print('chosen interface: ' + iface, '\n')
    
    # set ip address
    os.system("ifconfig | grep 'inet.*broadcast'")      # print out only those interfaces that are configured to have an IP
    print('\n')
    IpAddress = str(input(space + "set ip address:"))

    # set subnetmask
    SubnetMask = str(input(space + "set netmask   :"))

    # set network gateway
    Gateway = str(input(space + "set gateway   :"))

    clear()
    print('\n', space,"setting ip and netmask...")
    sleep(0.5)

    # Set the Ipaddress & Netmask
    os.system("ifconfig " + iface + " " + IpAddress + ' netmask ' + SubnetMask)

    print('\n', space, "setting gateway...")
    sleep(0.5)

    # Set the gateway
    os.system("ifconfig add default gw " + Gateway + ' ' + iface)

    clear()
    print('\n', space, "Done!")
    

    

# for testing purposes
def Help():
    
    space = ' ' * 2

    print(space, 'usage:\n', space*4,
        '-sns <Interface> ', space*2, ' | Set Network Settings\n', space*4,
        '-a'
    )



if True:

    try:

        if sys.argv[1] == "-h":
            Help()

        if sys.argv[1] == "-sns":
            Configure_NetSettings(str(sys.argv[2]))

    except Exception as e:
        
        space = ' ' * 2
        
        print(space, "-h for help")