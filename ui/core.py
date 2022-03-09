from operator import le
import tkinter as tk
import tkinter.messagebox as mb 
import settings
from ui.profile import Profile

class Core(tk.Tk):
    def __init__(self):
        super().__init__()

        # --------------------------------------
        self.initialiseView()
        self.setUpHeader()

        if len(settings.userProfilesList) <= 0: self.setUpProfileButton()
        if len(settings.userTasksList) <= 0: self.setUpTaskButton()

    def initialiseView(self):
        width = 600
        height = 300

        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        xPos = int((screenWidth / 2) - (width / 2))
        yPos = int((screenHeight / 4) - (height / 4))

        self.title('A Simple Supreme Bot')

        image_url = settings.setWindowIcon()

        self.iconbitmap(image_url)

        # Set the max and min size of the window to ensure it cant be resized
        self.minsize(width=width, height=height)
        self.maxsize(width=width, height=height)

        self.geometry("{0}x{1}+{2}+{3}".format(width, height, xPos, yPos))

        self.configure(background='white')

    def setUpHeader(self):
        main_header = tk.Label(self, text='A Simple Supreme Bot', background='#e03533', foreground='white')
        main_header.grid(row=1, sticky="w")
        main_header.place(relx=0.5, rely=0.05, anchor='center')
        main_header.configure(font=("Arial", 16), width=600)
    
    def setUpProfileButton(self):
        loadProfileButton = tk.Button(self, text="Load Profile Data", background='#e03533', foreground='white', command=self.showProfilePage)
        loadProfileButton.grid(columnspan=2, sticky='w')
        loadProfileButton.place(relx=0.25, rely=0.65, anchor='center')
        loadProfileButton.config(font=("Arial", 12), height=2, width=20)

    def setUpTaskButton(self):
        loadTaskButton = tk.Button(self, text="Load Task Data", background='#e03533', foreground='white', command=self.showTaskPage)
        loadTaskButton.grid(columnspan=2, sticky='w')
        loadTaskButton.place(relx=0.75, rely=0.65, anchor='center')
        loadTaskButton.config(font=("Arial", 12), height=2, width=20)

    def showProfilePage(self):
        Profile(self)
    
    def showTaskPage(self):
        print('Show Task Page')

    def errorMessage(self):
        mb.showerror("Supreme Bot", "Incorrect Hardware ID sorry")