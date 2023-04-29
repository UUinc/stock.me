from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from user import User

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        SCR_HEIGHT = self.winfo_screenheight()

        #Background left side
        # Load background image file
        img = Image.open("../assets/background/background.png")
        img = img.resize((SCR_HEIGHT, SCR_HEIGHT), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Load logo file
        logo_img = Image.open("../assets/icon/logo.png")
        logo_img = logo_img.resize((int(SCR_HEIGHT*0.42), int(SCR_HEIGHT*0.42)), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=SCR_HEIGHT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # Set canvas height to window height
        self.canvas.config(height=SCR_HEIGHT)
        # Place image at bottom-left corner with canvas width and image height
        self.canvas.create_image(0, SCR_HEIGHT, image=self.img, anchor="sw", tags="bg")
        # Add logo image on top of background image
        self.canvas.create_image(SCR_HEIGHT*0.15, SCR_HEIGHT*0.35, image=self.logo_img, anchor="nw")
        # Add text on top of the image
        self.canvas.create_text(int(SCR_HEIGHT/2.63), int(SCR_HEIGHT/1.2), text="STOCK.ME", font=("Livvic Bold", int(SCR_HEIGHT/15)), fill="white", tags="text")
        self.canvas.create_text(int(SCR_HEIGHT/2.63), int(SCR_HEIGHT/1.08), text="Power Up Your Inventory Management: Our App's Got You Covered!", font=("Livvic Medium", int(SCR_HEIGHT/68)), fill="white", tags="text")


        #Form login

        #login page title
        self.pageTitle = ttk.Label(self, text="LOGIN", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/13)))
        #entries labels
        self.usernameLabel = ttk.Label(self, text="username", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.passwordLabel = ttk.Label(self, text="password", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        #entries logos
        # Load logo files
        username_img = Image.open("../assets/logo/user.png")
        username_img = username_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(username_img)
        self.usernameIcon = Label(self, image=photo, bd=0)
        self.usernameIcon.image = photo
        password_img = Image.open("../assets/logo/padlock.png")
        password_img = password_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(password_img)
        self.passwordIcon = Label(self, image=photo, bd=0)
        self.passwordIcon.image = photo
        #entries
        self.usernameEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=36)
        self.passwordEntry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/58)), width=36, show="*")

        #login button
        #style button
        s = ttk.Style()
        s.configure('login_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/48)), padding=(int(SCR_HEIGHT/9), 10), background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        #create button
        self.loginBTN = ttk.Button(self, text="login", style='login_btn.TButton', bootstyle=PRIMARY, command=self.login)
        #sign up message text
        self.signupMessage = ttk.Label(self, text="Don't have an account?", foreground="#4D5D69", font=("Livvic Medium", int(SCR_HEIGHT/63)))
        #sign up button
        #style button
        s = ttk.Style()
        s.configure('signup_btn.TButton', font=('Livvic Bold', int(SCR_HEIGHT/64)), background='#FFFFFF', foreground='#4D5D69', borderwidth=0)
        s.map('signup_btn.TButton', background=[('active', '!disabled', '#FFFFFF')], foreground=[('active', '!disabled', '#4D5D69')])
        #create button
        self.signupBTN = ttk.Button(self, text="SIGN UP", style='signup_btn.TButton', command=self.signup)

        #set widgets position
        self.pageTitle.place(relx=0.72, rely=0.19, anchor="center")
        self.usernameLabel.place(relx=0.615, rely=0.35, anchor="center")
        self.usernameIcon.place(relx=0.84, rely=0.40, anchor="center")
        self.usernameIcon.lift()
        self.usernameEntry.place(relx=0.72, rely=0.4, anchor="center")
        self.passwordLabel.place(relx=0.615, rely=0.47, anchor="center")
        self.passwordIcon.place(relx=0.84, rely=0.52, anchor="center")
        self.passwordIcon.lift()
        self.passwordEntry.place(relx=0.72, rely=0.52, anchor="center")
        self.loginBTN.place(relx=0.72, rely=0.7, anchor="center")
        self.signupMessage.place(relx=0.692, rely=0.76, anchor="center")
        self.signupBTN.place(relx=0.785, rely=0.76, anchor="center")

        # self.textbox = ttk.Text(self, height=5)
        # self.textbox.pack(padx=10, pady=10)

        # self.check_state = ttk.IntVar()

        # self.check = ttk.Checkbutton(self, text="Show Messagebox", variable=self.check_state)
        # self.check.pack(padx=10, pady=10)
        
        # self.button = ttk.Button(self, text="Show Message", command=self.show_message)
        # self.button.pack(padx=10, pady=10)

        self.controller = controller

    # def show_message(self):
    #     print(self.check_state.get())

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if User.login(username, password):
            from pages.home_page import HomePage
            self.controller.show_page(HomePage)
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def signup(self):
        from pages.signup_page import SignupPage
        self.controller.show_page(SignupPage)
