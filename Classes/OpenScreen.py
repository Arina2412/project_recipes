import tkinter
from tkinter import *
from PIL import ImageTk, Image

class StartScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        img = Image.open(r'C:\Users\ארינה\OneDrive\שולחן העבודה\background.png')
        bg = ImageTk.PhotoImage(img)
        self.geometry('600x700')
        self.title('Start Screen')
        self.resizable(False,False)
        Label(self, image=bg).place(x=0, y=0)

        L1=Label(self,text="Tasty Pages",foreground="Green",font=("Calibri",30))
        L1.place(x=200,y=180)

        B1=Button(self,text='LOG IN',background="green",foreground="white",font=("Calibri",15),command=self.open_login_screen)
        B1.place(x=230,y=300,width=140,height=50)
        B2=Button(self, text='SIGN UP', background="green",foreground="white",font=("Calibri",15),command=self.open_signup_screen)
        B2.place(x=230,y=370,width=140,height=50)

    def open_login_screen(self):
        window=LoginScreen(self)
        window.grab_set()
        self.withdraw()

    def open_signup_screen(self):
        window=SignupScreen(self)
        window.grab_set()
        self.withdraw()


class LoginScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x700')
        self.title('LogIn Screen')

        L1 = Label(self, text="Log In", foreground="Green", font=("Calibri", 30))
        L1.place(x=250, y=150)

        L_Username=Label(self,text="Username",foreground="Black",font=("Calibri", 15))
        L_Username.place(x=100,y=250)
        E_Username=Entry(self,width=70)
        E_Username.place(x=95,y=280)

        L_Password=Label(self,text="Password",foreground="Black",font=("Calibri", 15))
        L_Password.place(x=100,y=350)
        E_Password=Entry(self,width=70)
        E_Password.place(x=95,y=380)

        B_Login = Button(self,text="Log In", background="green",foreground="white",font=("Calibri",17))
        B_Login.place(x=230, y=450,width=140,height=50)

        B_Return=Button(self,text='Return Back',background="green",foreground="white",font=("Calibri",15),command=self.return_back)
        B_Return.place(x=245,y=550)

    def return_back(self):
        self.parent.deiconify() #displays the window, after using the withdraw method
        self.destroy()

class SignupScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x700')
        self.title('SignUp Screen')

        L1 = Label(self, text="Sign Up", foreground="Green", font=("Calibri", 30))
        L1.place(x=250, y=150)

        L_Email = Label(self, text="Email", foreground="Black", font=("Calibri", 15))
        L_Email.place(x=100, y=250)
        E_Email = Entry(self, width=70)
        E_Email.place(x=95, y=280)

        L_Username = Label(self, text="Username", foreground="Black", font=("Calibri", 15))
        L_Username.place(x=100, y=330)
        E_Username = Entry(self, width=70)
        E_Username.place(x=95, y=360)

        L_Password = Label(self, text="Password", foreground="Black", font=("Calibri", 15))
        L_Password.place(x=100, y=410)
        E_Password = Entry(self, width=70)
        E_Password.place(x=95, y=440)

        B_Signup = Button(self, text="Sign Up", background="green", foreground="white", font=("Calibri", 17))
        B_Signup.place(x=230, y=500, width=140, height=50)

        B_Return=Button(self, text='Return Back', background="green",foreground="white",font=("Calibri",15), command=self.return_back)
        B_Return.place(x=245,y=600)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

if __name__ == "__main__":
    window = StartScreen()
    window.mainloop()