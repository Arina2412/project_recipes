import tkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import socket
from Db_classes import *
from tkinter import ttk, messagebox


class StartScreen(tkinter.Tk):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

        super().__init__()
        img = Image.open(r'C:\Users\ארינה\PycharmProjects\project_recipes\Classes\background.png')
        bg = ImageTk.PhotoImage(img)
        self.geometry('600x700')
        self.title('Start Screen')
        #self.configure(bg="#BCEAD5")
        self.resizable(False,False)

        Label(self, image=bg).place(x=0, y=0)

        self.create_gui()
    def create_gui(self):
        self.L1=Label(self,text="Tasty Pages",background="#BCEAD5",foreground="Green",font=("Calibri",30))
        self.L1.place(x=200,y=180)

        self.buttonLogin=Button(self,text='LOG IN',background="green",foreground="white",font=("Calibri",15),command=self.open_login_screen)
        self.buttonLogin.place(x=230,y=300,width=140,height=50)
        self.buttonSignup=Button(self, text='SIGN UP', background="green",foreground="white",font=("Calibri",15),command=self.open_signup_screen)
        self.buttonSignup.place(x=230,y=370,width=140,height=50)

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
        self.client_socket.connect((self.ip, self.port))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)


class LoginScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x700')
        self.title('LogIn Screen')
        self.configure(bg="#BCEAD5")
        self.UserDb = UsersDb()

        self.create_gui()

    def create_gui(self):
        self.lblLogin = Label(self, text="Log In", foreground="Green", font=("Calibri", 30),background="#BCEAD5")
        self.lblLogin.place(x=250, y=150)

        self.lblUsernameLogin = Label(self, text="Username", foreground="Black", font=("Calibri", 15),background="#BCEAD5")
        self.lblUsernameLogin.place(x=100, y=250)
        self.entryUsernameLogin = Entry(self, width=70)
        self.entryUsernameLogin.place(x=95, y=280)

        self.lblPasswordLogin = Label(self, text="Password", foreground="Black", font=("Calibri", 15),background="#BCEAD5")
        self.lblPasswordLogin.place(x=100, y=350)
        self.entryPasswordLogin = Entry(self, width=70)
        self.entryPasswordLogin.place(x=95, y=380)

        self.buttonEnterUserLogin = Button(self, text="Log In", background="green", foreground="white", font=("Calibri", 17),command=self.login_user)
        self.buttonEnterUserLogin .place(x=230, y=450, width=140, height=50)

        self.buttonReturnToStartScreen = Button(self, text='Return Back', background="green", foreground="white", font=("Calibri", 15),
                          command=self.return_back)
        self.buttonReturnToStartScreen.place(x=245, y=550)

        self.str = StringVar()
        self.str.set("")
        Label(self, textvariable=self.str,foreground="red",font=("Calibri", 15)).place(x=250, y=400)

    def login_user(self):
        if len(self.entryUsernameLogin.get())==0 and len(self.entryPasswordLogin.get())==0:
            messagebox.showerror("Please write email and password", "Error")
            return
        print("login")
        if self.UserDb.check_user(self.entryUsernameLogin.get(),self.entryPasswordLogin.get())==False:
            message = "Please Sign Up"
            self.str.set(message)
            print(self.str.get())
        else:
            message2="Welcome"
            self.str.set(message2)
            print(self.str.get())

    def return_back(self):
        self.parent.deiconify() #displays the window, after using the withdraw method
        self.destroy()

class SignupScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x700')
        self.title('SignUp Screen')
        self.configure(bg="#BCEAD5")
        self.UserDb=UsersDb()

        self.create_gui()
        self.buttonReturnToStartScreen2 = Button(self, text='Return Back', background="green", foreground="white",font=("Calibri", 15),command=self.return_back)
        self.buttonReturnToStartScreen2.place(x=245, y=600)

    def create_gui(self):
        self.lblSignup = Label(self, text="Sign Up", foreground="Green", font=("Calibri", 30),background="#BCEAD5")
        self.lblSignup.place(x=250, y=150)

        self.lblEmailSignup = Label(self, text="Email", foreground="Black", font=("Calibri", 15),background="#BCEAD5")
        self.lblEmailSignup.place(x=100, y=250)
        self.entryEmailSignup = Entry(self, width=70)
        self.entryEmailSignup.place(x=95, y=280)

        self.lblUsernameSignup = Label(self, text="Username", foreground="Black", font=("Calibri", 15),background="#BCEAD5")
        self.lblUsernameSignup.place(x=100, y=330)
        self.entryUsernameSignup = Entry(self, width=70)
        self.entryUsernameSignup .place(x=95, y=360)

        self.lblPasswordSignup = Label(self, text="Password", foreground="Black", font=("Calibri", 15),background="#BCEAD5")
        self.lblPasswordSignup.place(x=100, y=410)
        self.entryPasswordSignup = Entry(self, width=70)
        self.entryPasswordSignup.place(x=95, y=440)

        self.buttonAddUserSignup = Button(self, text="Sign Up", background="green", foreground="white", font=("Calibri", 17),command=self.signup_user)
        self.buttonAddUserSignup.place(x=230, y=500, width=140, height=50)


    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.signup_user, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def signup_user(self):
        if len(self.entryEmailSignup.get())==0 or len(self.entryUsernameSignup.get())==0 or len(self.entryPasswordSignup.get())==0:
            messagebox.showerror("Please write Email,Username and Password", "Error")
            return
        print("Sign Up")
        arr = ["SignUp", self.entryEmailSignup.get(),self.entryUsernameSignup.get(),self.entryPasswordSignup.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 1803
    window = StartScreen(ip,port)
    window.mainloop()
