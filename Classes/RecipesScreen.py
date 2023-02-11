import tkinter
from tkinter import *
from PIL import ImageTk, Image
from Classes.Db_classes import *
import textwrap

class RecipesScreen(tkinter.Toplevel):
    def __init__(self,parent,recipe_name,arr_recipe):
        self.RecipesDb=RecipesDb()
        super().__init__(parent)
        self.parent=parent
        self.geometry('600x770')
        self.resizable(False,False)
        self.configure(bg="#B5D5C5")
        #________________________________________________________________
        self.recipe_name=recipe_name
        self.arr_recipe=arr_recipe
        print(self.arr_recipe[3])
        self.IngredientsDb=IngredientsDb()

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
        self.lbl_cooking_time = Label(self,text="Cooking Time: ",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=200)
        self.lbl_ingredients = Label(self,text="Ingredients",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=240)
        self.lbl_instructions= Label(self,text="Instructions",foreground="black",bg="#B5D5C5",font=("Calibri", 14,"underline")).place(x=30,y=520)
        #________________________________________________________________________________________________________
        max_width = 80
        wrapped_text = textwrap.fill(self.arr_recipe[4], width=max_width)
        print(wrapped_text)

        self.title(self.arr_recipe[1])
        self.nutritions_text= Label(self,text=self.arr_recipe[2],foreground="black",bg="#B5D5C5",font=("Calibri", 13))
        self.nutritions_text.place(x=120,y=102)
        self.cooking_time_text=Label(self,text=self.arr_recipe[3],foreground="black",bg="#B5D5C5",font=("Calibri", 13))
        self.cooking_time_text.place(x=150,y=202)
        self.ingredients_text=Label(self,text=self.IngredientsDb.get_ingredients_by_recipe_id(self.arr_recipe[0]),bg="#B5D5C5",font=("Calibri", 12))
        self.ingredients_text.place(x=35,y=270)
        self.instructuons_text=Label(self,text=wrapped_text,foreground="black",bg="#B5D5C5",font=("Calibri", 13))
        self.instructuons_text.place(x=10,y=550)

        #________________________________________________________________________________________________________
        self.btn_add_to_favorites=Button(self,text="🤍",bg="#B5D5C5",activebackground="#B5D5C5",bd=0,font=("Calibri", 20),command=lambda: toggle_symbol(self.btn_add_to_favorites))
        self.btn_add_to_favorites.place(x=460,y=300)
        def toggle_symbol(button):
            if button["text"] == "🤍":

                button.config(text="🖤")
            else:
                button.config(text="🤍")
        #________________________________________________________________________________________________________
        self.btn_share=Button(self,text="🔗",bg="#B5D5C5",activebackground="#B5D5C5",bd=0,font=("Calibri", 20))
        self.btn_share.place(x=500,y=300)


    def return_back(self):
        self.parent.deiconify()
        self.destroy()