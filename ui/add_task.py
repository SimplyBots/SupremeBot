import tkinter as tk
import tkinter.messagebox as mb
import settings
import json

class AddTask(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.initialiseView(parent)
        self.setUpVariables()
        self.setUpHeader()
        self.setUpPage()
    
    def initialiseView(self, parent):
        width = 600
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

    def setUpVariables(self):
        self.taskItem_name = tk.StringVar()
        self.taskItem_category = tk.StringVar()
        self.taskItem_colour = tk.StringVar()
        self.taskItem_size = tk.StringVar()

        self.taskItem_name_input = tk.Entry(self, textvariable=self.taskItem_name)
        self.taskItem_category_input = tk.Entry(self, textvariable=self.taskItem_category)
        self.taskItem_colour_input = tk.Entry(self, textvariable=self.taskItem_colour)
        self.taskItem_size_input = tk.Entry(self, textvariable=self.taskItem_size)
    
    def setUpHeader(self):
        main_header = tk.Label(self, text='SimplyBots (Supreme Bot) - Add Task Page', background='#e03533', foreground='white')
        main_header.grid(row=1, sticky="w")
        main_header.place(relx=0.5, rely=0.05, anchor='center')
        main_header.configure(font=("Arial", 16), width=600)

    def setUpPage(self):
        self.createLabels()
        self.positionInGrid()
        self.configureInputs()
        self.placeInputs()
        self.setUpButtons()
    
    def createLabels(self):
        for i in range(0, len(settings.taskLabelData)):
            labelText = settings.taskLabelData[i][0]
            labelXPos = settings.taskLabelData[i][1]
            labelYPos = settings.taskLabelData[i][2]
            labelAnchor = settings.taskLabelData[i][3]

            label = tk.Label(self, text=labelText)
            label.grid(row=1, column=0, sticky='w')
            label.configure(font=('Arial', 12), background='white', foreground='#272822')
            label.place(relx=labelXPos, rely=labelYPos, anchor=labelAnchor)

            settings.taskLabelList.append(label)

    def setUpButtons(self):
        self.add_new_task_button = tk.Button(self, text='Add New Task', background='#e03533', foreground='white', command=self.createNewTask)
        self.add_new_task_button.grid(columnspan=2, sticky='w')
        self.add_new_task_button.place(relx=0.25, rely=0.85, anchor='center')
        self.add_new_task_button.config(font=("Arial", 12), height=2, width=15)

        self.cancel_add_task_button = tk.Button(self, text='Cancel', background='#e03533', foreground='white', command=self.destroy)
        self.cancel_add_task_button.grid(columnspan=2, sticky='w')
        self.cancel_add_task_button.place(relx=0.75, rely=0.85, anchor='center')
        self.cancel_add_task_button.config(font=("Arial", 12), height=2, width=15)

    def positionInGrid(self):
        self.taskItem_name_input.grid(row=1, column=0, sticky='w')
        self.taskItem_category_input.grid(row=1, column=0, sticky='w')
        self.taskItem_colour_input.grid(row=1, column=0, sticky='w')
        self.taskItem_size_input.grid(row=1, column=0, sticky='w')

    def configureInputs(self):
        self.taskItem_name_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.taskItem_category_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.taskItem_colour_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.taskItem_size_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')

    def placeInputs(self):
        self.taskItem_name_input.place(relx=0.75, rely=0.25, anchor='center')
        self.taskItem_category_input.place(relx=0.75, rely=0.40, anchor='center')
        self.taskItem_colour_input.place(relx=0.75, rely=0.55, anchor='center')
        self.taskItem_size_input.place(relx=0.75, rely=0.70, anchor='center')
    
    def createNewTask(self):
        if not self.isFormComplete():
            return

        item_name = self.taskItem_name.get()
        item_category = self.taskItem_category.get()
        item_colour = self.taskItem_colour.get()
        item_size = self.taskItem_size.get()

        data = {"item_name": item_name, "size": item_size, "colour": item_colour, "item_category": item_category}

        print(data)

        with open('data/tasks.json', 'r+', encoding='utf-8') as file:
            file_data = json.load(file)
            file_data["tasks"].append(data)
            file.seek(0)
            json.dump(file_data, file, indent=4, ensure_ascii=False)

        self.destroy()
            

    
    def isFormComplete(self):
        if not self.taskItem_name.get().strip():
            mb.showerror(title='Cant Create New Task', message='Name Cant Be Blank')
            return False
        if not self.taskItem_category.get().strip():
            mb.showerror(title='Cant Create New Task', message='Category Cant Be Blank')
            return False
        if not self.taskItem_colour.get().strip():
            mb.showerror(title='Cant Create New Task', message='Colour Cant Be Blank')
            return False
        if not self.taskItem_size.get().strip():
            mb.showerror(title='Cant Create New5 Task', message='Size Cant Be Blank')
            return False

        return True