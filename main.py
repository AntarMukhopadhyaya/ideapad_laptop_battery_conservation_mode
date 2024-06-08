import subprocess
from colorama import Fore,Back,Style
CHECK_COMMAND = "cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
DISABLE_COMMAND ="echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"
ENABLE_COMMAND = "echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode"


def is_battery_conservation_mode_enabled():
    output = subprocess.check_output(CHECK_COMMAND,shell=True,text=True)
    output = True if int(output) == 1 else False
    return output


def disable_battery_conservation_mode():
    if is_battery_conservation_mode_enabled():
        subprocess.check_output(DISABLE_COMMAND,shell=True,text=True)
        print(Fore.YELLOW+"Battery Conservation mode has been disabled.")
        print("Please disconnect your charger and reconnect it.")
        
    else:

        print(Fore.RED+"Battery conservation mode is already disabled.")
    print(Style.RESET_ALL)



def enable_battery_conservation_mode():
    if is_battery_conservation_mode_enabled():
        print(Fore.RED+"Battery conservation mode is already enabled.")
        
    else:
        subprocess.check_output(ENABLE_COMMAND,shell=True,text=True)
        print(Fore.YELLOW+"Battery conservation mode has been enabled.")
        print("Please disconnect your charger and reconnect it.")
    print(Style.RESET_ALL)



if __name__ == "__main__":
    print(Fore.RED+"Run this script as superuser")
    print(Style.RESET_ALL)
    while True:
        print(" 1-->Enable Battery Conservation Mode\n 2-->Disable Battery Conservation Mode\n 3-->Check Battery Conservation Mode\n 4-->Exit")
        choice = int(input("Enter your choice (1-4):"))
        if choice == 1:
            enable_battery_conservation_mode()
        if choice == 2:
            disable_battery_conservation_mode()
        if choice == 3:
            if is_battery_conservation_mode_enabled():
                print(Fore.YELLOW+"Battery conservation mode is enabled.")
            else:
                print(Fore.RED+"Battery conservation mode is disabled.")
            print(Style.RESET_ALL)
        if choice == 4:
            print(Fore.RED+"Exiting....")
            print(Style.RESET_ALL)
            break
    

    




