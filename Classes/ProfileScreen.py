from PIL import ImageTk, Image
import tkinter
from tkinter import *



class ProfileScreen(tkinter.Toplevel):
    def __init__(self, parent,username):
        super().__init__(parent)
        self.parent = parent
        self.username=username

        self.geometry('600x770')
        self.title('Profile Screen')
        self.resizable(False, False)
        self.configure(bg="#B5D5C5")

        self.create_gui()

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Profile", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=240, y=12)
    # _____________________________________________________________________________________________________
    #     self.img_profile = Image.open('photos/drinks_recipes/drinks.png')
    #     self.resized = self.img_profile.resize((150, 150), Image.LANCZOS)
    #     self.image = ImageTk.PhotoImage(self.resized)
    #     self.btn_drinks = Label(self, image=self.image).place(x=330, y=100)
        self.lbl_username=Label(self, text="Username: "+self.username,bg="#B5D5C5", fg="black",font=('Calibri', 14))
        self.lbl_username.place(x=200,y=300)


    # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)


    def return_back(self):
        self.parent.deiconify()
        self.destroy()