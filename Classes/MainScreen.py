from CategoriesScreens import *
import threading
from ProfileScreen import ProfileScreen
from tkinter import messagebox
from FavoritesScreen import FavoritesScreen
from HistoryScreen import HistoryScreen
from ReceivedRecipesScreen import ReceivedRecipesScreen
from ShoppingListScreen import ShoppingListScreen


class MainScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        super().__init__(parent)
        self.CategoryDb=CategoryDb()
        self.RecipesDb=RecipesDb()
        self.username=username

        self.parent=parent
        # print(self.parent.parent.client_socket)
        self.geometry('600x770')
        self.title('Main Screen')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")

        self.create_gui()

    def create_gui(self):
        self.head_frame=Frame(self,bg="#658864",highlightbackground="white",highlightthickness=1)
        self.head_frame.pack(side=TOP,fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        #______________________________________________________________________________
        # self.img_search = Image.open('photos/other/loupe2.png')
        # self.resized = self.img_search.resize((20, 18), Image.LANCZOS)
        # self.image_loupe = ImageTk.PhotoImage(self.resized)
        # self.btn_loupe = Button(self.head_frame, image=self.image_loupe, bd=0).place(x=550, y=45)
        # self.entry_search=Entry(self.head_frame,width=80)
        # self.entry_search.place(x=60,y=45)
        # self.entry_search.insert(0, "Search recipe...")
        # self.entry_search.config(fg="grey")
        #_______________________________________________________________________________
        self.toogle_btn=Button(self.head_frame,text="☰",bg="#658864",fg="white",
                               font=('Bold',17),bd=0,activebackground="#658864",activeforeground="white",
                               command=self.toogle_menu)
        self.toogle_btn.pack(side=LEFT)
        self.title_lb=Label(self.head_frame,text="Tasty Pages",bg="#658864",fg="white",font=('Calibri',20))
        self.title_lb.place(x=220,y=10)
        #_______________________________________________________________________________
        self.img_appetizers=Image.open('photos/appetizers_recipes/appetizers.jpg')
        self.resized= self.img_appetizers.resize((150,150),Image.LANCZOS)
        self.image=ImageTk.PhotoImage(self.resized)
        self.btn_appetizers = Button(self,image=self.image,bd=0,command=self.open_appetizers_screen).place(x=100,y=150)
        self.lbl_appetizers=Label(self,text="Appetizers\n"+self.CategoryDb.get_num_of_recipes("Appetizers"),bg="white",fg="#3C6255",
                                  width=21,font=('Calibri',10)).place(x=100,y=280)
        #_______________________________________________________________________________
        self.img_soups = Image.open('photos/soups_recipes/soups.png')
        self.resized = self.img_soups.resize((150, 150), Image.LANCZOS)
        self.image2 = ImageTk.PhotoImage(self.resized)
        self.btn_soups = Button(self, image=self.image2, bd=0,command=self.open_soups_screen).place(x=330, y=150)
        self.lbl_soups = Label(self, text="Soups\n"+self.CategoryDb.get_num_of_recipes("Soups"), bg="white", fg="#3C6255",
                               width=21, font=('Calibri', 10)).place(x=330, y=280)
        #_______________________________________________________________________________
        self.img_main_dishes = Image.open('photos/main_dishes_recipes/main meals.jpeg')
        self.resized = self.img_main_dishes.resize((150, 150), Image.LANCZOS)
        self.image3 = ImageTk.PhotoImage(self.resized)
        self.btn_mdishes = Button(self, image=self.image3, bd=0,command=self.open_main_dishes_screen).place(x=100, y=340)
        self.lbl_mdishes = Label(self, text="Main dishes\n"+self.CategoryDb.get_num_of_recipes("Main Dishes"), bg="white", fg="#3C6255",
                               width=21, font=('Calibri', 10)).place(x=100, y=470)
        # _______________________________________________________________________________
        self.img_salads = Image.open('photos/salads_recipes/salads.jpg')
        self.resized = self.img_salads.resize((150, 150), Image.LANCZOS)
        self.image4 = ImageTk.PhotoImage(self.resized)
        self.btn_salads = Button(self, image=self.image4, bd=0,command=self.open_salad_screen).place(x=330, y=340)
        self.lbl_salads = Label(self, text="Salads\n"+self.CategoryDb.get_num_of_recipes("Salads"), bg="white", fg="#3C6255",
                                 width=21, font=('Calibri', 10)).place(x=330, y=470)
        # _______________________________________________________________________________
        self.img_deserts = Image.open('photos/desserts_recipes/deserts.jpg')
        self.resized = self.img_deserts.resize((150, 150), Image.LANCZOS)
        self.image5 = ImageTk.PhotoImage(self.resized)
        self.btn_deserts = Button(self, image=self.image5, bd=0,command=self.open_desserts_screen).place(x=100, y=530)
        self.lbl_deserts = Label(self, text="Desserts\n"+self.CategoryDb.get_num_of_recipes("Deserts"), bg="white", fg="#3C6255",
                                width=21, font=('Calibri', 10)).place(x=100, y=660)
        # _______________________________________________________________________________
        self.img_drinks = Image.open('photos/drinks_recipes/drinks.png')
        self.resized = self.img_drinks.resize((150, 150), Image.LANCZOS)
        self.image6 = ImageTk.PhotoImage(self.resized)
        self.btn_drinks = Button(self, image=self.image6, bd=0,command=self.open_drinks_screen).place(x=330, y=530)
        self.lbl_drinks = Label(self, text="Drinks\n"+self.CategoryDb.get_num_of_recipes("Drinks"), bg="white", fg="#3C6255",
                                width=21, font=('Calibri', 10)).place(x=330, y=660)
        # _______________________________________________________________________________

    def toogle_menu(self):
        def collapse_toogle_menu():
            self.toogle_menu_fm.destroy()
            self.toogle_btn.config(text="☰")
            self.toogle_btn.config(command=self.toogle_menu)
        # __________________________________________________________________________
        self.toogle_menu_fm = Frame(self, bg="#658864")
        self.my_profile_btn=Button(self.toogle_menu_fm,text="My Profile",
                               font=("Calibri",16),bd=0,bg="#658864",fg="white",
                            activebackground="#658864",activeforeground="white",command=lambda: self.handle_add(self.username,self.parent.parent.client_socket))
        self.my_profile_btn.place(x=20,y=20)
        #__________________________________________________________________________
        self.favorites_btn = Button(self.toogle_menu_fm, text="Favorites",
                                     font=("Calibri", 16), bd=0, bg="#658864", fg="white",
                                     activebackground="#658864", activeforeground="white",command=lambda: self.handle_add3(self.parent.parent.client_socket))
        self.favorites_btn.place(x=20, y=80)
        #__________________________________________________________________________
        self.history_btn = Button(self.toogle_menu_fm, text="History",
                                    font=("Calibri", 16), bd=0, bg="#658864", fg="white",
                                    activebackground="#658864", activeforeground="white",command=lambda: self.handle_add2(self.parent.parent.client_socket))
        self.history_btn.place(x=20, y=140)
        #__________________________________________________________________________
        self.received_recipes_btn = Button(self.toogle_menu_fm, text="Received recipes",
                                  font=("Calibri", 16), bd=0, bg="#658864", fg="white",
                                  activebackground="#658864", activeforeground="white",command=lambda: self.handle_add4(self.parent.parent.client_socket))
        self.received_recipes_btn.place(x=20, y=200)
        #__________________________________________________________________________
        self.shopping_list_btn = Button(self.toogle_menu_fm, text="Shopping list",
                                           font=("Calibri", 16), bd=0, bg="#658864", fg="white",
                                           activebackground="#658864", activeforeground="white",command=self.open_shopping_list_screen)
        self.shopping_list_btn.place(x=20, y=260)
        #__________________________________________________________________________
        self.log_out_btn = Button(self.toogle_menu_fm, text="Log out",
                                        font=("Calibri", 16), bd=0, bg="#658864", fg="white",
                                        activebackground="#658864", activeforeground="white",command=lambda :self.logout(self.parent.parent.client_socket))
        self.log_out_btn.place(x=20, y=320)
        #__________________________________________________________________________
        window_height = self.winfo_height()
        #__________________________________________________________________________
        self.toogle_menu_fm.place(x=0, y=70, height=window_height, width=200)
        self.toogle_btn.config(text='X')
        self.toogle_btn.config(command=collapse_toogle_menu)
        #__________________________________________________________________________


    def handle_add(self, username, client_socket):
        self.client_handler = threading.Thread(target=self.get_email, args=(username, client_socket))
        self.client_handler.daemon = True
        self.client_handler.start()

    def get_email(self, username, client_socket):
        arr = ["get_email", username]
        str_get_email = "*".join(arr)
        print(str_get_email)
        client_socket.send(str_get_email.encode())
        data = client_socket.recv(1024)
        data = data.decode("utf-8")
        arr = data.split("*")
        print(arr)
        self.open_profile_screen(arr)

    def handle_add2(self,client_socket):
        self.client_handler = threading.Thread(target=self.get_history, args=(client_socket,self.username))
        self.client_handler.daemon = True
        self.client_handler.start()

    def get_history(self,client_socket,username):
        arr=["get_history",username]
        str_get_history="*".join(arr)
        client_socket.send(str_get_history.encode())
        data = client_socket.recv(4000)
        # print("Received {} bytes".format(len(data)))
        data = data.decode("utf-8")
        print(data)
        arr = data.split("#")
        print(arr)
        # print("Recipe: "+arr[0])
        self.open_history_screen(arr)

    def handle_add3(self,client_socket):
        self.client_handler = threading.Thread(target=self.get_favorites, args=(client_socket,self.username))
        self.client_handler.daemon = True
        self.client_handler.start()

    def get_favorites(self,client_socket,username):
        arr=["get_favorites",username]
        str_get_favorites="*".join(arr)
        client_socket.send(str_get_favorites.encode())
        data = client_socket.recv(4000)
        # print("Received {} bytes".format(len(data)))
        data = data.decode("utf-8")
        print(data)
        arr = data.split("#")
        print(arr)
        # print("Recipe: "+arr[0])
        self.open_favorites_screen(arr)

    def handle_add4(self,client_socket):
        self.client_handler = threading.Thread(target=self.get_received_recipes, args=(client_socket,self.username))
        self.client_handler.daemon = True
        self.client_handler.start()

    def get_received_recipes(self,client_socket,username):
        arr=["get_received_recipes",username]
        str_get_received_recipes="*".join(arr)
        client_socket.send(str_get_received_recipes.encode())
        data = client_socket.recv(4000)
        # print("Received {} bytes".format(len(data)))
        data = data.decode("utf-8")
        print(data)
        arr2 = data.split("#")
        print(arr2)
        # print("Recipe: "+arr[0])
        self.open_received_recipes_screen(arr2)

    def open_appetizers_screen(self):
        window = AppetizersScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_soups_screen(self):
        window = SoupsScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_main_dishes_screen(self):
        window = MainDishesScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_salad_screen(self):
        window = SaladsScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_desserts_screen(self):
        window = DessertsScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_drinks_screen(self):
        window = DrinksScreen(self,self.username)
        window.grab_set()
        self.withdraw()

    def open_profile_screen(self,email):
        window = ProfileScreen(self,self.username,email)
        window.grab_set()
        self.withdraw()

    def open_favorites_screen(self,arr):
        window = FavoritesScreen(self,arr,self.username)
        window.grab_set()
        self.withdraw()

    def open_history_screen(self,arr):
        window = HistoryScreen(self,arr,self.username)
        window.grab_set()
        self.withdraw()

    def open_received_recipes_screen(self,arr):
        window = ReceivedRecipesScreen(self,arr,self.username)
        window.grab_set()
        self.withdraw()

    def open_shopping_list_screen(self):
        window = ShoppingListScreen(self)
        window.grab_set()
        self.withdraw()

    def logout(self,client_socket):
        arr = ["log_out"]
        str_log_out = "*".join(arr)
        client_socket.send(str_log_out.encode())
        data = client_socket.recv(1024).decode()
        if data == "Server is shutting down":
            client_socket.close()
            self.return_back_to_start_screen()
            self.parent.parent.running = False
        else:
            messagebox.showerror("Error","Try again")

    def return_back_to_start_screen(self):
        self.parent.parent.deiconify()
        self.destroy()




