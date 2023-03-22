from RecipesScreen import *
import threading
from tkinter import messagebox

class HistoryScreen(tkinter.Toplevel):
    def __init__(self, parent,arr,username):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x770')
        self.title('History Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False, False)
        self.configure(bg="#B5D5C5")
        self.username=username

        if arr[0]=="Clear":
            self.create_gui()
            self.str = StringVar()
            message = "History is empty. No recipes have been viewed yet."
            self.str.set(message)
            Label(self, textvariable=self.str,background="#B5D5C5", foreground="red", font=("Calibri", 15)).place(x=90, y=130)
        else:
            new_arr = []
            for item in arr:
                new_arr.append(item.split('^'))
            # print(new_arr)
            self.arr_history = new_arr
            self.create_gui()
            self.create_recipes_screen()

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="History", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.img_search = Image.open('photos/other/trash can.png')
        self.resized = self.img_search.resize((30, 30), Image.LANCZOS)
        self.image_trach_can = ImageTk.PhotoImage(self.resized)
        self.clear_btn = Button(self.head_frame, image=self.image_trach_can, bd=0, bg="#658864", fg="white",
                                activebackground="#658864", activeforeground="white",
                                command=lambda: self.clear_history(self.username,self.parent.parent.parent.client_socket))
        self.clear_btn.place(x=530, y=20)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)
        # _____________________________________________________________________________________________________

    def create_recipes_screen(self):
        count=0
        btnX=0
        btnY=150

        while count < len(self.arr_history) and self.arr_history[count][0] is not None:
            recipe_name=self.arr_history[count][1]
            recipe_image = self.arr_history[count][2]
            cooking_time = self.arr_history[count][4]

            # print(recipe_name)
            count = count + 1
            if count>2 and count%2!=0:
                btnY+=210
            if count%2!=0:
                btnX = 100
            elif count%2==0:
                btnX = 330
            count=count-1
            # print(count)
            # print(self.arr_history[3])
            image = Image.open(recipe_image).resize((150, 150), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            button = Button(self, image=image, text=recipe_name +"\n"+"Cooking time: "+ cooking_time, bg="white", fg="#3C6255",
                            font=('Calibri', 10), bd=0,
                            command=lambda count=count: self.open_recipes_screen(recipe_name,self.arr_history[count],self.username))
            button.config(compound='top')
            button.image = image
            button.place(x=btnX, y=btnY)
            count=count + 1


    def open_recipes_screen(self, recipe_name, data_recipe,username):
        window = RecipesScreen(self, recipe_name, data_recipe,username)
        window.grab_set()
        self.withdraw()

    def clear_history(self,username,client_socket):
        arr=["clear_history",username]
        str_clear = "*".join(arr)
        client_socket.send(str_clear.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        if data=="History cleared successfully":
            messagebox.showinfo("Success", "History cleared successfully.\nReset the window")
        elif data=="Clearing history failed":
            messagebox.showerror("Fail","Try again")

    def return_back(self):
        self.parent.deiconify()
        self.destroy()