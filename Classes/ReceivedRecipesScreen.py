from RecipesScreen import *
from tkinter import messagebox

class ReceivedRecipesScreen(tkinter.Toplevel):
    def __init__(self, parent,arr,username):
        super().__init__(parent)
        self.parent = parent

        self.geometry('600x770')
        self.title('Received Recipes Screen')
        self.resizable(False, False)
        self.configure(bg="#B5D5C5")
        #______________________________
        self.username=username

        if arr[0]=="Clear":
            self.create_gui()
            self.str = StringVar()
            message = "History of received recipes is empty. No recipes have been received yet."
            self.str.set(message)
            Label(self, textvariable=self.str,background="#B5D5C5", foreground="red", font=("Calibri", 13)).place(x=40, y=130)
        else:
            new_arr = []
            for item in arr:
                new_arr.append(item.split('^'))
            # print(new_arr)
            self.arr_received_recipes = new_arr
            self.create_gui()
            self.create_recipes_screen()

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Received Recipes", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=220, y=12)
        # _____________________________________________________________________________________________________
        self.clear_btn = Button(self, text="Clear recipes", bd=0, background="#658864", foreground="white",
                                font=("Calibri", 15), activebackground="#658864",
                                activeforeground="white",
                                command=lambda: self.handle_add(self.username, self.parent.parent.parent.client_socket))
        self.clear_btn.place(x=450, y=90)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)


    def create_recipes_screen(self):
        count = 0
        btnX = 0
        btnY = 150

        while count < len(self.arr_received_recipes) and self.arr_received_recipes[count][0] is not None:
            recipe_name = self.arr_received_recipes[count][1]
            recipe_image = self.arr_received_recipes[count][2]
            cooking_time = self.arr_received_recipes[count][4]
            from_user=self.arr_received_recipes[count][6]

            # print(recipe_name)
            count = count + 1
            if count > 2 and count % 2 != 0:
                btnY += 210
            if count % 2 != 0:
                btnX = 100
            elif count % 2 == 0:
                btnX = 330
            count = count - 1
            # print(count)
            # print(self.arr_history[3])
            image = Image.open(recipe_image).resize((150, 150), Image.LANCZOS)
            image = ImageTk.PhotoImage(image)
            button = Button(self, image=image, text=recipe_name + "\n" + "From user: " + from_user, bg="white",
                            fg="#3C6255",
                            font=('Calibri', 10), bd=0,
                            command=lambda count=count: self.open_recipes_screen(recipe_name, self.arr_received_recipes[count],
                                                                                 self.username))
            button.config(compound='top')
            button.image = image
            button.place(x=btnX, y=btnY)
            count = count + 1

    def open_recipes_screen(self, recipe_name, data_recipe, username):
        window = RecipesScreen(self, recipe_name, data_recipe, username)
        window.grab_set()
        self.withdraw()

    def handle_add(self, username, client_socket):
        self.client_handler = threading.Thread(target=self.clear_received_recipes, args=(username, client_socket))
        self.client_handler.daemon = True
        self.client_handler.start()

    def clear_received_recipes(self, username, client_socket):
        arr = ["clear_received_recipes", username]
        str_clear = "*".join(arr)
        client_socket.send(str_clear.encode())
        data = client_socket.recv(1024).decode()
        print(data)
        if data == "Received recipes cleared successfully":
            messagebox.showinfo("Success", "History of received recipes cleared successfully.\nReset the window")
        elif data == "Clearing history of received recipes failed":
            messagebox.showerror("Fail", "Try again")

    def return_back(self):
        self.parent.deiconify()
        self.destroy()