import tkinter as tk
import tkinter.messagebox as mb
import settings

class Profile(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # -----------------------------------

        self.initialiseView(parent)
        self.setUpVariables()
        self.setUpHeader()
        self.setUpPage()

    def initialiseView(self, parent):
        width = 600
        height = 750

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

        self.title("A Simple Supreme Bot - Create Profile")

        image_url = settings.setWindowIcon()
        self.iconbitmap(image_url)

        self.configure(background='white')

    def setUpVariables(self):
        self.profile_name = tk.StringVar()
        self.profile_email = tk.StringVar()
        self.profile_address1 = tk.StringVar()
        self.profile_phone_number = tk.StringVar()
        self.profile_city = tk.StringVar()
        self.profile_postcode = tk.StringVar()
        self.profile_card_number = tk.StringVar()
        self.profile_card_expire_date = tk.StringVar()
        self.profile_card_security_number = tk.StringVar()
        self.profile_country_selected = tk.StringVar()
        self.profile_card_type_selected = tk.StringVar()

        self.profile_name_input = tk.Entry(self, textvariable=self.profile_name)
        self.profile_email_input = tk.Entry(self, textvariable=self.profile_email)
        self.profile_address1_input = tk.Entry(self, textvariable=self.profile_address1)
        self.profile_phone_number_input = tk.Entry(self, textvariable=self.profile_phone_number)
        self.profile_city_input = tk.Entry(self, textvariable=self.profile_city)
        self.profile_postcode_input = tk.Entry(self, textvariable=self.profile_postcode)
        self.profile_card_number_input = tk.Entry(self, textvariable=self.profile_card_number)
        self.profile_card_expire_date_input = tk.Entry(self, textvariable=self.profile_card_expire_date)
        self.profile_card_security_number_input = tk.Entry(self, textvariable=self.profile_card_security_number)
    
    def setUpHeader(self):
        main_header = tk.Label(self, text='A Simple Supreme Bot - Profile Page', background='#e03533', foreground='white')
        main_header.grid(row=1, sticky="w")
        main_header.place(relx=0.5, rely=0.05, anchor='center')
        main_header.configure(font=("Arial", 16), width=600)
    
    def setUpPage(self):        
        self.createLabels()
        # -----------------------------------------------------------
        self.setUpDropDowns()
        # -----------------------------------------------------------
        self.positionInGrid()
        # -----------------------------------------------------------
        self.configureInputs()
        # -----------------------------------------------------------
        self.placeInputs()
        # -----------------------------------------------------------
        self.setUpButtons()

    def createLabels(self):
        for i in range(0, len(settings.profileLabelNameList)):
            labelText = settings.profileLabelNameList[i][0]
            labelXPos = settings.profileLabelNameList[i][1]
            labelYPos = settings.profileLabelNameList[i][2]
            labelAnchor = settings.profileLabelNameList[i][3]

            label = tk.Label(self, text=labelText)
            label.grid(row=1, column=0, sticky='w')
            label.configure(font=('Arial', 12), background='white', foreground='#272822')
            label.place(relx=labelXPos, rely=labelYPos, anchor=labelAnchor)

            settings.userLabelsList.append(label)

    def setUpDropDowns(self):
        self.profile_country_selected.set(settings.listOfCountries[0])
        self.profile_country_dropdown = tk.OptionMenu(self, self.profile_country_selected, *settings.listOfCountries)

        # -----------------------------------------------------------

        self.profile_card_type_selected.set(settings.cardTypeList[0])
        self.profile_card_type_dropdown = tk.OptionMenu(self, self.profile_card_type_selected, *settings.cardTypeList)

    def positionInGrid(self):
        self.profile_country_dropdown.grid(row=1, column=0, sticky='w')
        self.profile_card_type_dropdown.grid(row=1, column=0, sticky='w')

        self.profile_name_input.grid(row=1, column=0, sticky='w')
        self.profile_email_input.grid(row=1, column=0, sticky='w')
        self.profile_address1_input.grid(row=1, column=0, sticky='w')
        self.profile_phone_number_input.grid(row=1, column=0, sticky='w')
        self.profile_city_input.grid(row=1, column=0, sticky='w')
        self.profile_postcode_input.grid(row=1, column=0, sticky='w')
        self.profile_card_number_input.grid(row=1, column=0, sticky='w')
        self.profile_card_expire_date_input.grid(row=1, column=0, sticky='w')
        self.profile_card_security_number_input.grid(row=1, column=0, sticky='w')

    def configureInputs(self): 
        self.profile_name_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_email_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_address1_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_phone_number_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_city_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_postcode_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_card_number_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_card_expire_date_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')
        self.profile_card_security_number_input.configure(font=('Arial', 12), background='#FF4A4A', foreground='white')

    def placeInputs(self):
        self.profile_name_input.place(relx=0.75, rely=0.10, anchor='center')
        self.profile_email_input.place(relx=0.75, rely=0.15, anchor='center')
        self.profile_address1_input.place(relx=0.75, rely=0.20, anchor='center')
        self.profile_country_dropdown.place(relx=0.75, rely=0.25, anchor='center')
        self.profile_phone_number_input.place(relx=0.75, rely=0.30, anchor='center')
        self.profile_city_input.place(relx=0.75, rely=0.35, anchor='center')
        self.profile_postcode_input.place(relx=0.75, rely=0.40, anchor='center')
        self.profile_card_type_dropdown.place(relx=0.75, rely=0.45, anchor='center')
        self.profile_card_number_input.place(relx=0.75, rely=0.50, anchor='center')
        self.profile_card_expire_date_input.place(relx=0.75, rely=0.55, anchor='center')
        self.profile_card_security_number_input.place(relx=0.75, rely=0.60, anchor='center')
    
    def setUpButtons(self):
        self.add_new_profile_button = tk.Button(self, text='Add New Profile', background='#e03533', foreground='white', command=self.createNewProfile)
        self.add_new_profile_button.grid(columnspan=2, sticky='w')
        self.add_new_profile_button.place(relx=0.25, rely=0.7, anchor='center')
        self.add_new_profile_button.config(font=("Arial", 12), height=2, width=15)

        self.cancel_add_profile_button = tk.Button(self, text='Cancel', background='#e03533', foreground='white', command=self.destroy)
        self.cancel_add_profile_button.grid(columnspan=2, sticky='w')
        self.cancel_add_profile_button.place(relx=0.75, rely=0.7, anchor='center')
        self.cancel_add_profile_button.config(font=("Arial", 12), height=2, width=15)

    def createNewProfile(self):
        if not self.isFormComplete():
            return

        current_profile_name = self.profile_name.get()
        current_profile_email = self.profile_email.get()
        current_profile_address1 = self.profile_address1.get()
        current_profile_phone_number = self.profile_phone_number.get()
        current_profile_city = self.profile_city.get()
        current_profile_phone_number = self.profile_phone_number.get()
        current_profile_postcode = self.profile_postcode.get()
        current_profile_card_number = self.profile_card_number.get()
        current_profile_card_expire_date = self.profile_card_expire_date.get()
        current_profile_card_security_number = self.profile_card_security_number.get()
        current_profile_card_type = self.profile_card_type_selected.get()
        current_profile_country = self.profile_country_selected.get()

        with open("data/profile.json", "a+") as data_file:
            data_file.seek(0)
            data = data_file.read(100)

            if len(data) > 0:
                data_file.write("\n")

            data_file.write('{"profile_username":"Test", "name":"' + current_profile_name + '", "email":"' + current_profile_email + '", "address1":"' + current_profile_address1 + 
                            '", "country":"' + current_profile_country + '", "phone":"' + current_profile_phone_number + '", "city":"' + current_profile_city + 
                            '", "zip":"' + current_profile_postcode + '", "cardtype":"' + current_profile_card_type + '", "cardnumber":"' + current_profile_card_number + 
                            '", "expire":"' + current_profile_card_expire_date + '", "security":"' + current_profile_card_security_number +'"}')
        self.destroy()
    
    def isFormComplete(self):
        if not self.profile_name.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Name Can't Be Blank!")
            return False
        if not self.profile_email.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Email Can't Be Blank!")
            return False
        if not self.profile_address1.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Address 1 Can't Be Blank!")
            return False
        if not self.profile_phone_number.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Phone Number Can't Be Blank!")
            return False
        if not self.profile_city.get().strip():
            mb.showerror(title="Cant Create New Profile", message="City Can't Be Blank!")
            return False
        if not self.profile_postcode.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Postcode Can't Be Blank!")
            return False
        if not self.profile_card_number.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Card Number Can't Be Blank!")
            return False
        if not len(self.profile_card_number.get()) == 16:
            mb.showerror(title="Cant Create New Profile", message="Card Length Too Short!")
            return False
        if not self.profile_card_expire_date.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Card Expire Date Can't Be Blank!")
            return False
        if not self.profile_card_security_number.get().strip():
            mb.showerror(title="Cant Create New Profile", message="Card Security Number Can't Be Blank!")
            return False
        if not len(self.profile_card_number.get()) == 16:
            mb.showerror(title="Cant Create New Profile", message="Card Length Too Short!")
            return False
        return True