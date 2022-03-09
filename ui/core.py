import tkinter as tk
import tkinter.messagebox as mb

import settings

from ui.profile import Profile
from ui.add_task import AddTask
from ui.show_tasks import ShowTasks

class Core(tk.Tk):
    def __init__(self):
        super().__init__()

        # --------------------------------------
        self.initialiseView()
        self.setUpHeader()
        self.setUpProfileButton()
        self.setUpAddTaskButton()
        if len(settings.userTasksList) > 0: self.setUpViewTaskButton()

    def initialiseView(self):
        width = 600
        height = 200

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        xPos = int((screenWidth / 2) - (width / 2))
        yPos = int((screenHeight / 4) - (height / 4))

        self.title('SimplyBots - Supreme Bot')

        image_url = settings.setWindowIcon()

        self.iconbitmap(image_url)

        # Set the max and min size of the window to ensure it cant be resized
        self.minsize(width=width, height=height)
        self.maxsize(width=width, height=height)

        self.geometry("{0}x{1}+{2}+{3}".format(width, height, xPos, yPos))

        self.configure(background='white')

    def setUpHeader(self):
        main_header = tk.Label(self, text='SimplyBots - Supreme Bot', background='#e03533', foreground='white', anchor='center')
        main_header.grid(row=1, sticky="w")
        main_header.place(relx=0.5, rely=0.05, anchor='center')
        main_header.configure(font=("Arial", 16), width=600)
    
    def setUpProfileButton(self):
        loadProfileButton = tk.Button(self, text="Load Profile Data", background='#e03533', foreground='white', command=self.showProfilePage)
        loadProfileButton.grid(columnspan=2, sticky='w')
        loadProfileButton.place(relx=0.25, rely=0.75, anchor='center')
        loadProfileButton.config(font=("Arial", 12), height=2, width=20)

    def setUpAddTaskButton(self):
        loadTaskButton = tk.Button(self, text="Load Task Data", background='#e03533', foreground='white', command=self.showAddTaskPage)
        loadTaskButton.grid(columnspan=2, sticky='w')
        loadTaskButton.place(relx=0.75, rely=0.75, anchor='center')
        loadTaskButton.config(font=("Arial", 12), height=2, width=20)

    def setUpViewTaskButton(self):
        viewTasksButton = tk.Button(self, text="View Tasks", background='#e03533', foreground='white', command=self.showTasksPage)
        viewTasksButton.grid(columnspan=2, sticky='w')
        viewTasksButton.place(relx=0.50, rely=0.35, anchor='center')
        viewTasksButton.config(font=("Arial", 12), height=2, width=20)

    def showProfilePage(self):
        self.add_profile_page = Profile(self)
    
    def showAddTaskPage(self):
        if len(settings.userTasksList) >= 1:
            mb.showerror(title='Cant Show Add Task Page', message='You can only make 1 task, please delete the task before trying to make a new one')
        else:
            self.add_task_page = AddTask(self)
    
    def showTasksPage(self):
        if len(settings.userTasksList) > 0:
            self.show_tasks_page = ShowTasks(self)
        else:
            mb.showerror(title='Cant Show Tasks Page', message='There are no tasks available, please create a new task')

    def errorMessage(self):
        mb.showerror("Supreme Bot", "Incorrect Hardware ID sorry")