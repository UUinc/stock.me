from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.user import User

class SettingsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        SCR_HEIGHT = self.winfo_screenheight()

        self.show_password = False
        self.show_new_password = False
        #Background left side
        # Load background image file
        img = Image.open("assets/background/sidebar.png")
        img = img.resize((int(SCR_HEIGHT/3.01), SCR_HEIGHT), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)

        # Load logo file
        logo_img = Image.open("assets/icon/logo.png")
        logo_img = logo_img.resize((int(SCR_HEIGHT*0.08), int(SCR_HEIGHT*0.08)), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(logo_img)

        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=SCR_HEIGHT, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        # Set canvas height to window height
        self.canvas.config(height=SCR_HEIGHT)
        # Place image at bottom-left corner with canvas width and image height
        self.canvas.create_image(0, SCR_HEIGHT, image=self.img, anchor="sw", tags="bg")
        # Add logo image on top of background image
        self.canvas.create_image(int(SCR_HEIGHT*0.04), int(SCR_HEIGHT*0.05), image=self.logo_img, anchor="nw")
        # Add text on top of the image
        self.canvas.create_text(int(SCR_HEIGHT*0.21), int(SCR_HEIGHT*0.09), text="STOCK.ME", font=("Livvic Bold", int(SCR_HEIGHT/52)), fill="#313f4a", tags="text")

        #Sidebar buttons
        s = ttk.Style()
        s.configure('sidebar_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/64)), background='#BDC3C6', foreground='#38393B', borderwidth=0)
        s.map('sidebar_btn.TButton', background=[('active', '!disabled', '#A7AEB1')], foreground=[('active', '!disabled', '#38393B')])
        s = ttk.Style()
        s.configure('sidebar_disabled_btn.TButton', font=('Livvic Bold', int(SCR_HEIGHT/64)), background='#BDC3C6', foreground='#38393B', borderwidth=0)
        s.map('sidebar_disabled_btn.TButton', background=[('active', '!disabled', '#A7AEB1')], foreground=[('active', '!disabled', '#38393B')])
        #create buttons
        from src.pages.home_page import HomePage
        self.home_sidebar_btn = ttk.Button(self, text="Dashboard", style='sidebar_btn.TButton', padding=(120, 10, 132, 10), command=lambda: controller.update_page(HomePage))
        from src.pages.notification_page import NotificationPage
        self.notification_sidebar_btn = ttk.Button(self, text="Notification", style='sidebar_btn.TButton', padding=(120, 10, 127, 10), command=lambda: controller.update_page(NotificationPage))
        self.settings_sidebar_btn = ttk.Button(self, text="Settings", style='sidebar_disabled_btn.TButton', padding=(120, 10, 153, 10))
        from src.pages.login_page import LoginPage
        self.logout_sidebar_btn = ttk.Button(self, text="Logout", style='sidebar_btn.TButton', padding=(120, 10, 172, 10), command=lambda: controller.update_page(LoginPage))
        #Sidebar logos
        #Dashboard icon
        home_img = Image.open("assets/logo/home.png")
        home_img = home_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(home_img)
        self.homeIcon = Label(self, image=photo, bd=0)
        self.homeIcon.image = photo
        #Notification icon
        notification_img = Image.open("assets/logo/notification.png")
        notification_img = notification_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(notification_img)
        self.notificationIcon = Label(self, image=photo, bd=0)
        self.notificationIcon.image = photo
        #Settings icon
        settings_img = Image.open("assets/logo/settings.png")
        settings_img = settings_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(settings_img)
        self.settingsIcon = Label(self, image=photo, bd=0)
        self.settingsIcon.image = photo
        #Logout icon
        logout_img = Image.open("assets/logo/logout.png")
        logout_img = logout_img.resize((25, 25), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(logout_img)
        self.logoutIcon = Label(self, image=photo, bd=0)
        self.logoutIcon.image = photo

        #set sidebar buttons position
        self.home_sidebar_btn.place(relx=0, rely=0.2, anchor="w")
        self.homeIcon.place(relx=0.038, rely=0.2, anchor="w")
        self.notification_sidebar_btn.place(relx=0, rely=0.25, anchor="w")
        self.notificationIcon.place(relx=0.038, rely=0.25, anchor="w")
        self.settings_sidebar_btn.place(relx=0, rely=0.3, anchor="w")
        self.settingsIcon.place(relx=0.038, rely=0.3, anchor="w")
        self.logout_sidebar_btn.place(relx=0, rely=0.35, anchor="w")
        self.logoutIcon.place(relx=0.038, rely=0.35, anchor="w")

        #Settings page
        #Settings page title
        self.pageTitle = ttk.Label(self, text="Settings", foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        #set widgets position
        self.pageTitle.place(relx=0.23, rely=0.08, anchor="w")

        #body 
        #User information
        self.username = controller.get_username()
        user = User.get_information(self.username)
        firstname = user.get_firstname()
        lastname = user.get_lastname()
        email = user.get_email()

        user_img = Image.open("assets/logo/profile.png")
        user_img = user_img.resize((180, 180), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(user_img)
        self.userIcon = Label(self, image=photo, bd=0)
        self.userIcon.image = photo
        self.userIcon.place(relx=0.58, rely=0.25, anchor="center")
        self.usernameTitle = ttk.Label(self, text=self.username, foreground="#4D5D69", font=("Livvic Bold", int(SCR_HEIGHT/30)))
        self.usernameTitle.place(relx=0.58, rely=0.39, anchor="center")
        
        self.firstnameLabel = ttk.Label(self, text="First name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.firstnameLabel.place(relx=0.28, rely=0.45, anchor="w")
        self.firstname_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=31)
        self.firstname_entry.insert(0, firstname)
        self.firstname_entry.place(relx=0.28, rely=0.50, anchor="w")
        
        self.lastnameLabel = ttk.Label(self, text="Last name", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.lastnameLabel.place(relx=0.599, rely=0.45, anchor="w")
        self.lastname_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=31)
        self.lastname_entry.insert(0, lastname)
        self.lastname_entry.place(relx=0.599, rely=0.50, anchor="w")
        
        self.emailLabel = ttk.Label(self, text="Email", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.emailLabel.place(relx=0.28, rely=0.55, anchor="w")
        self.email_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=67,bootstyle=SECONDARY,background='#FFFFFF')
        self.email_entry.insert(0, email)
        self.email_entry.place(relx=0.28, rely=0.60, anchor="w")
        
        #####
        user_img = Image.open("assets/logo/email.png")
        user_img = user_img.resize((30, 30), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(user_img)
        self.userIcon = Label(self, image=photo, bd=0)
        self.userIcon.image = photo
        self.userIcon.place(relx=0.865, rely=0.60, anchor="center")
        #####
        
        self.passwordLabel = ttk.Label(self, text="Password", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.passwordLabel.place(relx=0.28, rely=0.65, anchor="w")
        self.password_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=31, show="•" )
        self.password_entry.place(relx=0.28, rely=0.70, anchor="w")
        #####
        #password icons
        hide_img = Image.open("assets/logo/hide.png")
        hide_img = hide_img.resize((30, 30), Image.ANTIALIAS)
        self.photo_hide = ImageTk.PhotoImage(hide_img)
        show_img = Image.open("assets/logo/show.png")
        show_img = show_img.resize((30, 30), Image.ANTIALIAS)
        self.photo_show = ImageTk.PhotoImage(show_img)

        self.passwordIcon = Label(self, image=self.photo_hide, bd=0)
        self.passwordIcon.image = self.photo_hide
        self.passwordIcon.bind("<Button-1>", self.toggle_password_visibility)
        self.passwordIcon.place(relx=0.546, rely=0.70, anchor="center")
        #####
        
        self.newpasswordLabel = ttk.Label(self, text="New password", foreground="#4D5D69", font=("Livvic Regular", int(SCR_HEIGHT/60)))
        self.newpasswordLabel.place(relx=0.599, rely=0.65, anchor="w")
        self.newpassword_entry = ttk.Entry(self, font=('Livvic Regular', int(SCR_HEIGHT/50)), width=31, show="•")
        self.newpassword_entry.place(relx=0.599, rely=0.70, anchor="w")
        #####
        self.newpasswordIcon = Label(self, image=self.photo_hide, bd=0)
        self.newpasswordIcon.image = self.photo_hide
        self.newpasswordIcon.bind("<Button-1>", self.toggle_newpassword_visibility)
        self.newpasswordIcon.place(relx=0.865, rely=0.70, anchor="center")
        #####
        
        s = ttk.Style()
        s.configure('settings_save_btn.TButton', font=('Livvic Medium', int(SCR_HEIGHT/50)), padding=(20,12), width=14, background='#4D5D69', foreground='#FFFFFF', borderwidth=0)
        self.save_btn= ttk.Button(self, text="save", style='settings_save_btn.TButton', command=self.save)
        self.save_btn.place(relx=0.58, rely= 0.84, anchor="center")
        
        self.controller = controller

    def save(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        newpassword = self.newpassword_entry.get()

        #get user
        user = User.get_information(self.username)

        if newpassword != '' and user.check_password(password):
            user.update_password(newpassword)

        user.set_firstname(firstname)
        user.set_lastname(lastname)
        user.set_email(email)

        user.update_information()
        messagebox.showinfo(title="Settings", message="Information updated")

    def toggle_password_visibility(self, event):
        if self.show_password:
            self.passwordIcon.configure(image=self.photo_show)
            self.password_entry.config(show="")
        else:
            self.passwordIcon.configure(image=self.photo_hide)
            self.password_entry.config(show="•")

        self.show_password = not self.show_password

    def toggle_newpassword_visibility(self, event):
        if self.show_new_password:
            self.newpasswordIcon.configure(image=self.photo_show)
            self.newpassword_entry.config(show="")
        else:
            self.newpasswordIcon.configure(image=self.photo_hide)
            self.newpassword_entry.config(show="•")

        self.show_new_password = not self.show_new_password