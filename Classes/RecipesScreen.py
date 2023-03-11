import tkinter
from tkinter import *
from PIL import ImageTk, Image
from Classes.Db_classes import *
import textwrap

class RecipesScreen(tkinter.Toplevel):
    def __init__(self,parent,recipe_name,arr_recipe):
        self.RecipesDb=RecipesDb()
        self.IngredientsDb=IngredientsDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #________________________________________________________________
        self.recipe_name=recipe_name
        self.arr_recipe=arr_recipe
        # print(self.arr_recipe[3])

        self.create_gui()

    def create_gui(self):
        self.head_frame = Frame(self, bg="#658864", highlightbackground="white", highlightthickness=1)
        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=70)
        self.title_lb = Label(self.head_frame, text=self.recipe_name, bg="#658864", fg="white", font=('Calibri', 20))
        self.title_lb.pack(pady=20)
        # _____________________________________________________________________________________________________
        self.buttonReturnToMainScreen = Button(self.head_frame, text='←', bd=0, background="#658864",
                                               foreground="white",
                                               font=("Calibri", 17), activebackground="#658864",
                                               activeforeground="white", command=self.return_back)
        self.buttonReturnToMainScreen.place(x=5, y=12)
        #_______________________________________________________________________________________________________
        self.lnl_nutrition= Label(self,text="Nutritions: ",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=100)
        self.lbl_cooking_time = Label(self,text="Cooking Time: ",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=150)
        self.lbl_ingredients = Label(self,text="Ingredients",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=190)
        self.lbl_instructions= Label(self,text="Instructions",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=470)
        #________________________________________________________________________________________________________
        max_width = 80
        wrapped_text = textwrap.fill(self.arr_recipe[5], width=max_width)
        print(wrapped_text)

        self.title(self.arr_recipe[1])
        self.img_recipe = Image.open(self.arr_recipe[2])
        self.resized = self.img_recipe.resize((190, 190), Image.LANCZOS)
        self.image_recipe = ImageTk.PhotoImage(self.resized)
        self.lbl_image = Label(self, image=self.image_recipe,bd=0).place(x=370, y=100)
        #______________________________________
        self.nutritions_text= Label(self,text=self.arr_recipe[3],foreground="black",bg="#B5D5C5",font=("Calibri", 13))
        self.nutritions_text.place(x=120,y=102)
        #______________________________________
        self.cooking_time_text=Label(self,text=self.arr_recipe[4],foreground="black",bg="#B5D5C5",font=("Calibri", 13))
        self.cooking_time_text.place(x=150,y=152)
        #______________________________________
        self.instructuons_text=Label(self,text=wrapped_text,foreground="black",bg="#B5D5C5",font=("Calibri", 12))
        self.instructuons_text.place(x=30,y=500)
        #______________________________________
        ingredient_list = self.IngredientsDb.get_ingredients_by_recipe_id(self.arr_recipe[0]).split("\n")
        placeY=220
        for ingredient in ingredient_list:
            self.btn_ingredients=Button(self,text=ingredient,foreground="black",bg="#B5D5C5",bd=0,font=("Calibri", 10),
                                        highlightthickness=0,activebackground="#B5D5C5", activeforeground="black")
            self.btn_ingredients.place(x=30,y=placeY)
            placeY=placeY+25
        #________________________________________________________________________________________________________
        self.btn_add_to_favorites=Button(self,text="🤍",bg="#B5D5C5",activebackground="#B5D5C5",bd=0,font=("Calibri", 20),command=lambda: toggle_symbol(self.btn_add_to_favorites))
        self.btn_add_to_favorites.place(x=480,y=290)
        def toggle_symbol(button):
            if button["text"] == "🤍":

                button.config(text="🖤")
            else:
                button.config(text="🤍")
        #________________________________________________________________________________________________________
        self.btn_share=Button(self,text="🔗",bg="#B5D5C5",activebackground="#B5D5C5",bd=0,font=("Calibri", 20))
        self.btn_share.place(x=520,y=290)


    def return_back(self):
        self.parent.deiconify()
        self.destroy()