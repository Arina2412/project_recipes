import tkinter
from tkinter import *
from PIL import ImageTk, Image
import threading
from tkinter import messagebox



class ProfileScreen(tkinter.Toplevel):
    def __init__(self, parent,username,email):
        super().__init__(parent)
        self.parent = parent
        self.username=username
        self.email=email

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
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.canvas=Canvas(self,width=200,height=200,background="#B5D5C5",bd=0,highlightthickness=0)
        self.canvas.place(x=200,y=100)
        self.img_profile = Image.open('photos/other/profile photo2.png')
        self.resized = self.img_profile.resize((200, 200), Image.LANCZOS)
        self.image_profile = ImageTk.PhotoImage(self.resized)
        self.photo = self.canvas.create_image(100,100,image=self.image_profile)
        #_______________________________
        self.lbl_username=Label(self, text="Username:",bg="#B5D5C5", fg="black",font=('Calibri', 14,"underline"))
        self.lbl_username.place(x=100,y=350)
        self.username_info=Label(self,text=self.username,bg="#B5D5C5", fg="black",font=('Calibri', 14))
        self.username_info.place(x=190,y=350)
        # _______________________________
        self.lbl_email=Label(self,text="Email:",bg="#B5D5C5", fg="black",font=('Calibri', 14,"underline"))
        self.lbl_email.place(x=100,y=400)
        self.info_email=Label(self,text=self.email[0],bg="#B5D5C5", fg="black",font=('Calibri', 14))
        self.info_email.place(x=150,y=400)
        # _______________________________
        self.lbl_change_email = Label(self, text="Change email:", bg="#B5D5C5", fg="black",
                                      font=('Calibri', 14, "underline"))
        self.lbl_change_email.place(x=100, y=440)
        # _______________________________
        self.en_email=Entry(self,width=40,font=('Calibri', 13))
        self.en_email.place(x=100,y=470)
        self.en_email.insert(0, "Enter new email...")
        self.en_email.config(fg="grey")
        # _______________________________
        self.btn_change_email=Button(self,text="Change",bg="#658864", fg="white",bd=0, font=('Calibri', 12),
                               highlightthickness=0,activebackground="#658864", activeforeground="white",command=self.handle_add)
        self.btn_change_email.place(x=470,y=469)
        # _______________________________
        self.lbl_change_password=Label(self,text="Change password:",bg="#B5D5C5", fg="black",font=('Calibri', 14,"underline"))
        self.lbl_change_password.place(x=100,y=510)
        # ______________________________
        self.btn_change_password = Button(self, text="Change", bg="#658864", fg="white", bd=0, font=('Calibri', 12),
                                          highlightthickness=0, activebackground="#658864", activeforeground="white",
                                          command=self.handle_add2)
        self.btn_change_password.place(x=470, y=539)
        # _______________________________
        self.en_password=Entry(self,width=40,font=('Calibri', 13))
        self.en_password.place(x=100,y=540)
        self.en_password.insert(0, "Enter new password...")
        self.en_password.config(fg="grey")
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)


    def handle_add(self):
        self.client_handler = threading.Thread(target=self.change_email, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def change_email(self):
        arr = ["change_email", self.username, self.en_email.get()]
        str_change = ",".join(arr)
        print(str_change)
        self.parent.parent.parent.client_socket.send(str_change.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        print(data)
        if data == "Email changed successfully":
            messagebox.showinfo("Success", "Email changed successfully.\nReset the window")
        else:
            messagebox.showerror("Error", "Try again")

    def handle_add2(self):
        self.client_handler = threading.Thread(target=self.change_password, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def change_password(self):
        arr = ["change_password", self.username, self.en_password.get()]
        str_change = ",".join(arr)
        print(str_change)
        self.parent.parent.parent.client_socket.send(str_change.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        print(data)
        if data == "Password changed successfully":
            messagebox.showinfo("Success", "Password changed successfully.\nEnter the app again")
        else:
            messagebox.showerror("Error", "Try again")

    def return_back(self):
        self.parent.deiconify()
        self.destroy()