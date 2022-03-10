
import json
import tkinter as tk
from bot.look_for_stock import get_stock
import settings

from tkinter.ttk import Treeview

from multiprocessing.dummy import Pool as ThreadPool

class ShowTasks(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.initialiseView(parent)
        self.setUpHeader()
        self.setUpPage()
    
    def initialiseView(self, parent):
        width = 900
        height = 700

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        xPos = int((screenWidth / 2) - (width / 2))
        yPos = int((screenHeight / 4) - (height / 4))

        self.attributes("-toolwindow", True)  # Remove minimise and maximise decorations
        self.transient(parent)  # Always show on top of main window
        self.resizable(False, False)  # Cannot be resized
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, xPos, yPos))  # Set size and position
        self.lift()  # Bring to front of the main window
        self.focus_force()  # Force dialog to retain any focus
        self.grab_set() # Prevent access to main window

        self.title("SimplyBots (Supreme Bot) - Create Profile")

        image_url = settings.setWindowIcon()
        self.iconbitmap(image_url)

        self.configure(background='white')
    
    def setUpHeader(self):
        main_header = tk.Label(self, text='SimplyBots (Supreme Bot) - Tasks Page', background='#e03533', foreground='white')
        main_header.grid(row=1, sticky="w")
        main_header.place(relx=0.5, rely=0.05, anchor='center')
        main_header.configure(font=("Arial", 16), width=600)

    def setUpPage(self):
        self.createTable()
        self.createStartButton()
    
    def createTable(self):
        tasks = open("data/tasks.json", encoding='utf-8')
        data = json.load(tasks)

        tableFrame = tk.Frame(self)
        tableFrame.pack()
        
        # Scroll Bar

        tableFrame.place(relx=0.5, rely=0.5, anchor='center')

        tasksTable = Treeview(tableFrame)
        tasksTable.pack()

        tasksTable['columns'] = ('Item Name', 'Item Size', 'Item Colour', 'Item Category', 'Item Profile')

        tasksTable.column("#0", width=0, stretch=False)
        tasksTable.heading("#0",text="",anchor='center')

        listNames = ['Item Name', 'Item Size', 'Item Colour', 'Item Category', 'Item Profile']
        windowWidth = self.winfo_width() - (self.winfo_width() * 0.15)

        columnWidth = round(windowWidth / len(listNames))

        print(columnWidth)

        for i in range(0, len(listNames)):
            tasksTable.heading(listNames[i], text=listNames[i], anchor='center')
            tasksTable.column(listNames[i], anchor='center', width=columnWidth)

        iid = 0

        for item in data["tasks"]:
            itemName = item['item_name']
            itemSize = item['size']
            itemColour = item['colour']
            itemCategory = item['item_category']
            itemProfile = item['profile_name']

            tasksTable.insert(parent='', index='end', iid=iid, text='', values=(itemName, itemSize, itemColour, itemCategory, itemProfile))

            iid = iid + 1

        tasksTable.pack()

    def createStartButton(self):
        self.start_tasks_button = tk.Button(self, text='Run Tasks', background='#e03533', foreground='white', command=self.runTasks)
        self.start_tasks_button.grid(columnspan=2, sticky='w')
        self.start_tasks_button.place(relx=0.5, rely=0.95, anchor='center')
        self.start_tasks_button.config(font=("Arial", 12), height=2, width=15)
    
    def runTasks(self):
        self.updateButtonText()
    
    def updateButtonText(self):
        if self.start_tasks_button['text'] == 'Run Tasks':
            self.start_tasks_button['text'] = 'Stop Tasks'
            self.inject_tasks()
        else:
            self.start_tasks_button['text'] = 'Run Tasks'
            print('Stop Running Tasks')
        
    def inject_tasks(self):
        pool1 = ThreadPool(4)

        tasksCreated = []
        tasks = open("data/tasks.json", encoding='utf-8')
        data = json.load(tasks)
        for item in data["tasks"]:
            task = [item["item_category"], item["item_name"], item["colour"], item["size"]]
            tasksCreated.append(task)
        tasks.close()

        pool1.starmap(get_stock, tasksCreated)

        pool1.close()
        pool1.join()