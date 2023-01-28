import threading
import tkinter
from tkinter import *
from tkinter import messagebox
from Classes.Db_classes import *
from PIL import ImageTk, Image
from Classes.MainScreen import MainScreen


class SignupScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x7')
        self.title('SignUp Screen')
        self.resizable(False, False)
        self.UserDb=UsersDb()

        self.create_gui()

    def create_gui(self):
        self.img = Image.open('photos/other/background.png')
        self.resized = self.img.resize((600, 770), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self, image=self.image)
        self.label_image.place(x=0, y=0)
        #________________________________________________________________________________________________________
        self.lblSignup = Label(self, text="Sign Up", foreground="white",background="#658864", font=("Calibri", 30))
        self.lblSignup.place(x=250, y=150)
        # ________________________________________________________________________________________________________
        self.lblEmailSignup = Label(self, text="Email", foreground="Black",background="#C27664",font=("Calibri", 14))
        self.lblEmailSignup.place(x=100, y=245)
        self.entryEmailSignup1 = Entry(self, width=70)
        self.entryEmailSignup1.place(x=100, y=280)
        # self.entryEmailSignup1.insert(0, "Enter your email...")
        # self.entryEmailSignup1.config(fg="grey")
        # ________________________________________________________________________________________________________
        self.lblUsernameSignup = Label(self, text="Username", foreground="Black",background="#C27664",font=("Calibri", 14))
        self.lblUsernameSignup.place(x=100, y=325)
        self.entryUsernameSignup1 = Entry(self, width=70)
        self.entryUsernameSignup1 .place(x=100, y=360)
        # self.entryUsernameSignup1.insert(0, "Enter your username...")
        # self.entryUsernameSignup1.config(fg="grey")
        # ________________________________________________________________________________________________________
        self.lblPasswordSignup = Label(self, text="Password", foreground="Black",background="#C27664",font=("Calibri", 14))
        self.lblPasswordSignup.place(x=100, y=405)
        self.entryPasswordSignup1 = Entry(self, width=70)
        self.entryPasswordSignup1.place(x=100, y=440)
        # self.entryPasswordSignup1.insert(0, "Enter your password...")
        # self.entryPasswordSignup1.config(fg="grey")
        # ________________________________________________________________________________________________________
        self.buttonAddUserSignup = Button(self, text="Sign Up", background="#C27664", foreground="white", font=("Calibri", 17),command=self.handle_add_user)
        self.buttonAddUserSignup.place(x=230, y=500, width=140, height=50)
        # ________________________________________________________________________________________________________
        self.buttonReturnToStartScreen2 = Button(self, text='Return Back', background="#C27664", foreground="white",
                                                 font=("Calibri", 14), command=self.return_back)
        self.buttonReturnToStartScreen2.place(x=245, y=600)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.signup_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def signup_user(self):
        if len(self.entryEmailSignup1.get()) == 0 or len(self.entryPasswordSignup1.get()) == 0 :
            messagebox.showerror("Error", "Please write your email,username and password")
            return
        print("signup")
        arr = ["signup", self.entryEmailSignup1.get(), self.entryUsernameSignup1.get(), self.entryPasswordSignup1.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        self.open_main_screen()

    def open_main_screen(self):
        window = MainScreen(self)
        window.grab_set()
        self.withdraw()

    def return_back(self):
        self.parent.deiconify()
        self.destroy()