from RecipesScreen import *

def create_recipes_screen(self,arr2,client_socket,username):
    for recipe_image, recipe_name, btnX, btnY in arr2:
        # print(recipe_name)
        image = Image.open(recipe_image).resize((150, 150), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        button = Button(self, image=image, text=recipe_name, bg="white", fg="#3C6255", font=('Calibri', 10), bd=0,
                        command=lambda recipe_name=recipe_name: get_recipe(self, recipe_name, client_socket,username))
        button.config(compound='top')
        button.image = image
        button.place(x=btnX, y=btnY)


def get_recipe(self,name,client_socket,username):
    arr = ["get_one_recipe", name]
    str_get_recipe = "*".join(arr)
    # print(str_get_recipe)
    client_socket.send(str_get_recipe.encode())
    data = client_socket.recv(1024)
    data=data.decode("utf-8")
    arr=data.split("*")
    # print(arr)
    # print("place: "+arr[3])
    open_recipes_screen(self,name,arr,username)
    # print("Length: "+str(len(arr)))
    insert_recipe(self,arr,client_socket,username)

def open_recipes_screen(self,recipe_name,data_recipe,username):
    window = RecipesScreen(self,recipe_name,data_recipe,username)
    window.grab_set()
    self.withdraw()

def insert_recipe(self,arr,client_socket,username):
    arr=["insert_recipe",arr[1],arr[2],arr[3],arr[4],arr[5],username]
    str_insert = "*".join(arr)
    # print(str_insert)
    client_socket.send(str_insert.encode())
    data = client_socket.recv(1024)
    print(data)
    if data == "Recipe added to history successfully":
        return True
    else:
        return False

class AppetizersScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        # print(self.parent.parent.parent.client_socket)
        self.geometry('600x770')
        self.title('Appetizers Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")

        self.create_gui()
        self.arr_recipes_names=["Aussie Sausage Rolls","Chicken & Bacon Roll Ups","Party Shrimps","South-of-Border Bruschetta"]
        self.arr_appetizers = [('photos/appetizers_recipes/aussie sausage rolls.jpg', "Aussie Sausage Rolls",100,150),
                               ('photos/appetizers_recipes/chicken&bacon roll ups.jpg',"Chicken & Bacon Roll Ups",330,150),
                               ('photos/appetizers_recipes/party shrimps.jpg',"Party Shrimps",100,360),
                               ('photos/appetizers_recipes/south-of-the-border bruschetta.jpg',"South-of-Border Bruschetta",330,360)]
        create_recipes_screen(self,self.arr_appetizers,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Appetizers", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=220, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()


class SoupsScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('Soups Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #______________________________________________________________________________________________
        self.create_gui()
        self.arr_soups=[('photos/soups_recipes/Asian Chicken Noodle Soup.jpg', "Asian Chicken Noodle Soup",100,150),
                        ('photos/soups_recipes/Easy Tortellini Spinach Soup.jpg', "Tortellini Spinach Soup",330,150),
                        ('photos/soups_recipes/Homemade Cheesy Potato Soup.jpg',"Cheesy Potato Soup",100,360),
                        ('photos/soups_recipes/Onion Cheese Soup.jpg', "Onion Cheese Soup",330,360)]
        create_recipes_screen(self,self.arr_soups,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Soups", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

class MainDishesScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('Main Dishes Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #______________________________________________________________________________________________
        self.create_gui()
        self.arr_main_dishes = [('photos/main_dishes_recipes/Breaded Pork Chops.jpg', "Breaded Pork Chops", 100, 150),
                          ('photos/main_dishes_recipes/Chicken with Butter Sauce.jpg', "Chicken with Butter Sauce", 330, 150),
                          ('photos/main_dishes_recipes/Parmesan Chicken Breast.jpg', "Parmesan Chicken Breast", 100, 360),
                          ('photos/main_dishes_recipes/Ravioli Lasagna.jpg',  "Ravioli Lasagna", 330, 360),
                                ('photos/main_dishes_recipes/Sausage Hash.jpg',"Sausage Hash",100,570)]
        create_recipes_screen(self,self.arr_main_dishes,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Main Dishes", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=220, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

class SaladsScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('Salads Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #______________________________________________________________________________________________
        self.create_gui()
        self.arr_salads = [('photos/salads_recipes/Bacon Chicken Chopped Salad.jpg', "Bacon Chopped Salad", 100, 150),
                                ('photos/salads_recipes/Caesar Salad.jpg',"Caesar Salad",330, 150),
                                ('photos/salads_recipes/Caprese Salad.jpg',"Caprese Salad",100, 360),
                                ('photos/salads_recipes/Garden Tomato Salad.jpg', "Garden Tomato Salad", 330, 360),
                                ('photos/salads_recipes/Greek Salad.jpg',"Greek Salad", 100, 570)]
        create_recipes_screen(self,self.arr_salads,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Salads", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

class DessertsScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('Desserts Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #______________________________________________________________________________________________
        self.create_gui()
        self.arr_desserts = [('photos/desserts_recipes/Berry Dream Cake.jpg', "Berry Dream Cake", 100, 150),
                           ('photos/desserts_recipes/Cherry Cream Cheese Tarts.jpg', "Cherry Tarts", 330, 150),
                           ('photos/desserts_recipes/Spiced Chocolate Molten Cakes.jpg', "Chocolate Molten Cakes", 100, 360)]
        create_recipes_screen(self,self.arr_desserts,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Desserts", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()

class DrinksScreen(tkinter.Toplevel):
    def __init__(self,parent,username):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.title('Drinks Screen')
        self.iconbitmap('photos/other/icon_recipe.ico')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #______________________________________________________________________________________________
        self.create_gui()
        self.arr_drinks = [('photos/drinks_recipes/Citrus Cider Punch.jpg', "Citrus Cider Punch", 100, 150),
                             ('photos/drinks_recipes/Cranberry Fizz.jpg', "Cranberry Fizz", 330, 150),
                             ('photos/drinks_recipes/Pineapple Iced Tea.jpg',"Pineapple Iced Tea", 100,360)]
        create_recipes_screen(self,self.arr_drinks,self.parent.parent.parent.client_socket,username)

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text="Drinks", bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.place(x=250, y=12)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)

    def return_back(self):
        self.parent.deiconify()
        self.destroy()
