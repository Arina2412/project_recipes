import tkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
import socket
from Db_classes import *
from tkinter import ttk, messagebox
import sqlite3


# def fetch_db():
#     connection = sqlite3.connect('project_recipes.db')
#     cursor=connection.cursor()
#     cursor.execute()

class MainScreen(tkinter.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x700')
        self.title('Main Screen')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")

        self.create_gui()

    def create_gui(self):
        self.head_frame=Frame(self,bg="#658864",highlightbackground="white",highlightthickness=1)
        self.head_frame.pack(side=TOP,fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        #_______________________________________________________________________________
        self.toogle_btn=Button(self.head_frame,text="☰",bg="#658864",fg="white",
                               font=('Bold',20),bd=0,activebackground="#658864",activeforeground="white",
                               command=self.toogle_menu)
        self.toogle_btn.pack(side=LEFT)
        self.title_lb=Label(self.head_frame,text="Tasty Pages",bg="#658864",fg="white",font=('Calibri',24))
        self.title_lb.place(x=220,y=10)
        #_______________________________________________________________________________


    def toogle_menu(self):
        def collapse_toogle_menu():
            self.toogle_menu_fm.destroy()
            self.toogle_btn.config(text="☰")
            self.toogle_btn.config(command=self.toogle_menu)
        # __________________________________________________________________________
        self.toogle_menu_fm = Frame(self, bg="#658864")
        self.my_profile_btn=Button(self.toogle_menu_fm,text="My Profile",
                               font=("Calibri",18),bd=0,bg="#658864",fg="white",
                            activebackground="#658864",activeforeground="white")
        self.my_profile_btn.place(x=20,y=20)
        #__________________________________________________________________________
        self.favorites_btn = Button(self.toogle_menu_fm, text="Favorites",
                                     font=("Calibri", 18), bd=0, bg="#658864", fg="white",
                                     activebackground="#658864", activeforeground="white")
        self.favorites_btn.place(x=20, y=80)
        #__________________________________________________________________________
        self.history_btn = Button(self.toogle_menu_fm, text="History",
                                    font=("Calibri", 18), bd=0, bg="#658864", fg="white",
                                    activebackground="#658864", activeforeground="white")
        self.history_btn.place(x=20, y=140)
        #__________________________________________________________________________
        self.received_recipes_btn = Button(self.toogle_menu_fm, text="Received recipes",
                                  font=("Calibri", 18), bd=0, bg="#658864", fg="white",
                                  activebackground="#658864", activeforeground="white")
        self.received_recipes_btn.place(x=20, y=200)
        #__________________________________________________________________________
        self.shopping_list_btn = Button(self.toogle_menu_fm, text="Shopping list",
                                           font=("Calibri", 18), bd=0, bg="#658864", fg="white",
                                           activebackground="#658864", activeforeground="white")
        self.shopping_list_btn.place(x=20, y=260)
        #__________________________________________________________________________
        self.log_out_btn = Button(self.toogle_menu_fm, text="Log out",
                                        font=("Calibri", 18), bd=0, bg="#658864", fg="white",
                                        activebackground="#658864", activeforeground="white")
        self.log_out_btn.place(x=20, y=320)
        #__________________________________________________________________________
        window_height = self.winfo_height()
        #__________________________________________________________________________
        self.toogle_menu_fm.place(x=0, y=70, height=window_height, width=200)
        self.toogle_btn.config(text='X')
        self.toogle_btn.config(command=collapse_toogle_menu)
        #__________________________________________________________________________




if __name__ == "__main__":
    window = MainScreen()
    window.mainloop()







