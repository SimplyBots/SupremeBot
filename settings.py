import os.path
import tkinter as tk

def init():
    global userProfilesList
    global userTasksList
    global profileLabelNameList
    global listOfCountries
    global cardTypeList
    global userLabelsList
    global taskLabelData
    global taskLabelList

    userProfilesList = []
    userTasksList = []
    userLabelsList = []
    taskLabelList = []
    cardTypeList = [
        "MASTER",
        "VISA"
    ]
    taskLabelData = [
        ["Item Name: ", 0.25, 0.25, "center"],
        ["Item Category: ", 0.25, 0.40, "center"],
        ["Item Colour: ", 0.25, 0.55, "center"],
        ["Item Size: ", 0.25, 0.70, "center"]
    ]
    profileLabelNameList = [
        ["Full Name: ", 0.25, 0.15, "center"],
        ["Email Address: ", 0.25, 0.20, "center"],
        ["Address 1:", 0.25, 0.25, "center"],
        ["Country: ", 0.25, 0.35, "center"],
        ["Phone Number: ", 0.25, 0.45, "center"],
        ["City: ", 0.25, 0.50, "center"],
        ["Postcode: ", 0.25, 0.55, "center"],
        ["Card Type: ", 0.25, 0.65, "center"],
        ["Card Number: ", 0.25, 0.75, "center"],
        ["Expire Date: ", 0.25, 0.80, "center"],
        ["Card Security Number: ", 0.25, 0.85, "center"],
    ]
    listOfCountries = [
        "AUSTRIA",
        "BELARUS",
        "BELGIUM",
        "BULGARIA",
        "CROATIA",
        "CYPRUS",
        "CZECH REPUBLIC",
        "DENMARK",
        "ESTONIA",
        "FINLAND",
        "FRANCE",
        "GERMANY",
        "GREECE",
        "HUNGARY",
        "ICELAND",
        "IRELAND",
        "ITALY",
        "LATVIA",
        "LITHUANIA",
        "LUXEMBOURG",
        "MALTA",
        "MONACO",
        "NETHERLANDS",
        "NORWAY",
        "POLAND",
        "PORTUGAL",
        "ROMANIA",
        "RUSSIA",
        "SLOVAKIA",
        "SLOVENIA",
        "SPAIN",
        "SWEDEN",
        "SWITZERLAND",
        "TURKEY",
        "UK",
        "UK (N. IRELAND)"
    ]

def setWindowIcon():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    image_url = (dir_path + r'\ui\images\su.ico')

    return image_url


    # THE CODE BELOW WILL BE USED TO FIND USERS PROFILES

    # for entry in settings.userProfilesList:
    #         if entry[0] == "#":
    #             continue

    #         entry_as_dict = eval(entry)

    #         print(entry_as_dict["name"])
    #         print(entry_as_dict["cardnumber"])





    # THE CODE BELOW WILL BE USED TO FIND THE USERS TASKS

    # for entry in settings.userTasksList:
    #         if entry[0] == "#":
    #             continue

    #         entry_as_dict = eval(entry)

    #         print(entry_as_dict["item_name"])
    #         print(entry_as_dict["size"])