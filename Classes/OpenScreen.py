import tkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import socket
from Db_classes import *
from SignupScreen import SignupScreen
from tkinter import messagebox
from MainScreen import MainScreen

class StartScreen(tkinter.Tk):
    def __init__(self):
        self.UserDb=UsersDb()
        super().__init__()
        self.running=True
        self.geometry("600x770")
        self.title('Start Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        #self.configure(bg="#BCEAD5")
        self.resizable(False,False)

        self.handle_thread_socket()
        self.create_gui()
    def create_gui(self):
        self.canvas=Canvas(self,width=600,height=770,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.img = Image.open('photos/other/background.png')
        self.resized = self.img.resize((600, 770), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.photo = self.canvas.create_image(0,0,anchor=NW,image=self.image)
        # ________________________________________________________________________________________________________
        self.canvas.create_text(300, 230,text="Tasty Pages",fill="#4E6C50",font=("Calibri",38,"bold"))
        # ________________________________________________________________________________________________________
        self.buttonLogin=Button(self.canvas,text='LOG IN',background="#C27664",foreground="white",font=("Calibri",18),command=self.open_login_screen)
        self.buttonLogin.place(x=210,y=320,width=170,height=60)
        self.buttonSignup=Button(self.canvas, text='SIGN UP', background="#C27664",foreground="white",font=("Calibri",18),command=self.open_signup_screen)
        self.buttonSignup.place(x=210,y=400,width=170,height=60)
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
        print("data: "+data)
        print("hi", self.client_socket)


class LoginScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent

        self.geometry('600x770')
        self.title('LogIn Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False, False)
        self.UserDb = UsersDb()

        self.create_gui()

    def create_gui(self):
        self.canvas = Canvas(self, width=600, height=770, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.img = Image.open('photos/other/background.png')
        self.resized = self.img.resize((600, 770), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.resized)
        self.photo = self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        # ________________________________________________________________________________________________________
        self.canvas.create_text(300, 200,text="Log In",fill="#658864",font=("Calibri",38,"bold"))
        # ________________________________________________________________________________________________________
        self.lblUsernameLogin=self.canvas.create_text(135,268,text="Username",fill="black",font=("Calibri", 15))
        self.entryUsernameLogin = Entry(self, width=70)
        self.entryUsernameLogin.place(x=95, y=280)
        # ________________________________________________________________________________________________________
        self.lblPasswordLogin=self.canvas.create_text(135,368,text="Password",fill="black",font=("Calibri", 15))
        self.entryPasswordLogin = Entry(self, width=70,show="*")
        self.entryPasswordLogin.place(x=95, y=380)
        # ________________________________________________________________________________________________________
        self.buttonEnterUserLogin = Button(self, text="Log In", background="#C27664", foreground="white", font=("Calibri", 17),command=self.login_user)
        self.buttonEnterUserLogin .place(x=230, y=450, width=140, height=50)
        # ________________________________________________________________________________________________________
        self.buttonReturnToStartScreen = Button(self, text='Return Back', background="#C27664", foreground="white", font=("Calibri", 14),
                          command=self.return_back)
        self.buttonReturnToStartScreen.place(x=245, y=530)
        # ________________________________________________________________________________________________________
        self.str = StringVar()
        self.str.set("")
        Label(self, textvariable=self.str,foreground="red",font=("Calibri", 15)).place(x=240, y=410)

    def login_user(self):
        if len(self.entryUsernameLogin.get())==0 and len(self.entryPasswordLogin.get())==0:
            messagebox.showerror("Error", "Please write your username and password")
            return
        arr=["login",self.entryUsernameLogin.get(),self.entryPasswordLogin.get()]
        str_check = "*".join(arr)
        print(str_check)
        self.parent.client_socket.send(str_check.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)
        if data=="Loged In successfully":
            self.open_main_screen()
        else:
            message = "Please Sign Up"
            self.str.set(message)
            print(self.str.get())

    def open_main_screen(self):
        window = MainScreen(self,self.entryUsernameLogin.get())
        window.grab_set()
        self.withdraw()

    def return_back(self):
        self.parent.deiconify() #displays the window, after using the withdraw method
        self.destroy()


if __name__ == "__main__":
    window = StartScreen()
    window.mainloop()

