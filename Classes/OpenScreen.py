import tkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import socket
from Classes.Db_classes import *
from Classes.SignupScreen import SignupScreen
from tkinter import messagebox
from Classes.MainScreen import MainScreen


class StartScreen(tkinter.Tk):
    def __init__(self):
        self.UserDb=UsersDb()
        super().__init__()

        self.geometry("600x770")
        self.title('Start Screen')
        #self.configure(bg="#BCEAD5")
        self.resizable(False,False)

        self.handle_thread_socket()
        self.create_gui()
    def create_gui(self):
        self.img = Image.open('photos/other/background.png')
        self.resized = self.img.resize((600, 770), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self, image=self.image)
        self.label_image.place(x=0, y=0)
        # ________________________________________________________________________________________________________
        self.L1=Label(self,text="Tasty Pages",background="#658864",foreground="white",font=("Calibri",30))
        self.L1.place(x=200,y=180)
        # ________________________________________________________________________________________________________
        self.buttonLogin=Button(self,text='LOG IN',background="#C27664",foreground="white",font=("Calibri",15),command=self.open_login_screen)
        self.buttonLogin.place(x=230,y=300,width=140,height=50)
        self.buttonSignup=Button(self, text='SIGN UP', background="#C27664",foreground="white",font=("Calibri",15),command=self.open_signup_screen)
        self.buttonSignup.place(x=230,y=370,width=140,height=50)
        # ________________________________________________________________________________________________________

    def open_login_screen(self):
        window=LoginScreen(self)
        window.grab_set()
        self.withdraw()

    def open_signup_screen(self):
        window=SignupScreen(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1',1803))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)


class LoginScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('LogIn Screen')
        self.resizable(False, False)
        #self.configure(bg="#BCEAD5")
        self.UserDb = UsersDb()

        self.create_gui()

    def create_gui(self):
        self.img = Image.open('photos/other/background.png')
        self.resized = self.img.resize((600, 770), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.label_image = Label(self, image=self.image)
        self.label_image.place(x=0, y=0)
        # ________________________________________________________________________________________________________
        self.lblLogin = Label(self, text="Log In", foreground="white",background="#658864", font=("Calibri", 30))
        self.lblLogin.place(x=250, y=150)
        # ________________________________________________________________________________________________________
        self.lblUsernameLogin = Label(self, text="Username", foreground="Black",background="#C27664",font=("Calibri", 14))
        self.lblUsernameLogin.place(x=100, y=245)
        self.entryUsernameLogin = Entry(self, width=70)
        self.entryUsernameLogin.place(x=95, y=280)
        # self.entryUsernameLogin.insert(0, "Enter your username...")
        # self.entryUsernameLogin.config(fg="grey")
        # ________________________________________________________________________________________________________
        self.lblPasswordLogin = Label(self, text="Password", foreground="Black",background="#C27664",font=("Calibri", 14))
        self.lblPasswordLogin.place(x=100, y=345)
        self.entryPasswordLogin = Entry(self, width=70,show="*")
        self.entryPasswordLogin.place(x=95, y=380)
        # ________________________________________________________________________________________________________
        self.buttonEnterUserLogin = Button(self, text="Log In", background="#C27664", foreground="white", font=("Calibri", 17),command=self.open_main_screen)
        self.buttonEnterUserLogin .place(x=230, y=450, width=140, height=50)
        # ________________________________________________________________________________________________________
        self.buttonReturnToStartScreen = Button(self, text='Return Back', background="#C27664", foreground="white", font=("Calibri", 14),
                          command=self.return_back)
        self.buttonReturnToStartScreen.place(x=245, y=550)
        # ________________________________________________________________________________________________________
        self.str = StringVar()
        self.str.set("")
        Label(self, textvariable=self.str,foreground="red",font=("Calibri", 15)).place(x=240, y=410)

    def login_user(self):
        if len(self.entryUsernameLogin.get())==0 and len(self.entryPasswordLogin.get())==0:
            messagebox.showerror("Error", "Please write your username and password")
            return
        print("login")
        if self.UserDb.check_user(self.entryUsernameLogin.get(),self.entryPasswordLogin.get())==False:
            message = "Please Sign Up"
            self.str.set(message)
            print(self.str.get())
        else:
            print("welcome")
            # message2="Welcome"
            # self.str.set(message2)
            # print(self.str.get())
            self.open_main_screen()

    def open_main_screen(self):
        window = MainScreen(self)
        window.grab_set()
        self.withdraw()

    def return_back(self):
        self.parent.deiconify() #displays the window, after using the withdraw method
        self.destroy()

if __name__ == "__main__":
    window = StartScreen()
    window.mainloop()
