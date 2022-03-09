import os.path
import settings

from ui.core import Core
from bot.main import SupremeBot
from bot.look_for_stock import get_stock
from authentification import getHardwareID
from seleniumMode.entry import openSupreme

def main():
    """
    Main Function That is ran at the start of the project
    :return: None
    """

    # These 3 Lines NEED to happen FIRST
    settings.init()

    loadUserData('data/profile.json')
    loadTaskData('data/tasks.json')

    coreUIPage = Core() 

    Aidan_hwid = "4854C55B-79B8-7D1A-AA1B-D8BBC109D7AC" # Needs to be pulled form first time you load up an exe or install
    Michael_hwid = "032E02B4-0499-0583-5006-180700080009" # Same as comment above
    
    if (getHardwareID() == Aidan_hwid or getHardwareID() == Michael_hwid):
        coreUIPage.mainloop()
        # openSupreme() Commenting This out for now as its breaking my UI stuff

        # get_stock()
    else:
        print('Error')
        coreUIPage.errorMessage()

def loadUserData(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("\nError: preload data file on path '{0}' not found".format(file_path))
        return
    
    if os.stat(file_path).st_size == 0:
        print("\nError: preload data file on path '{0}' is empty".format(file_path))
        return

    data_file = open(file_path, "r")

    entries = data_file.readlines()

    for entry in entries:
        settings.userProfilesList.append(entry)


def loadTaskData(file_path):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print("\nError: preload data file on path '{0}' not found".format(file_path))
        # Disable Other Buttons?
        return

    if os.stat(file_path).st_size == 0:
        print("\nError: preload data file on path '{0}' is empty".format(file_path))
        # Send The User To The Task Window - Disable Other Buttons?
        return

    data_file = open(file_path, "r")

    entries = data_file.readlines()

    for entry in entries:
        settings.userTasksList.append(entry)

if __name__ == "__main__":
    main()
