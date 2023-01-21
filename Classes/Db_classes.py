import sqlite3
import hashlib
class RecipesDb(object):
    def __init__(self, tablename="RecipesDb",recipe_id="recipe_id", recipe_name="recipe_name", category_id="category_id", nutritions="nutritions", cooking_time="cooking_time", description="description"):
        self.__tablename=tablename
        self.__recipe_id=recipe_id
        self.__recipe_name=recipe_name
        self.__category_id=category_id
        self.__nutritions=nutritions
        self.__cooking_time=cooking_time
        self.__description=description

        conn=sqlite3.connect('project_recipes.db')
        #print("Database opened successfuly")
        str= "Create table if not exists " + self.__tablename + "(" + self.__recipe_id + " " + "integer primary key autoincrement ,"
        str += " " + self.__recipe_name + " text not null ,"
        str += " " + self.__category_id + " integer not null ,"
        str += " " + self.__nutritions + " text not null ,"
        str += " " + self.__cooking_time + " text not null ,"
        str += " " + self.__description + " text not null )"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_recipe(self, recipe_name, category_id, nutritions, cooking_time, description):
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_insert = "Insert into " + self.__tablename + " (" + self.__recipe_name + "," + self.__category_id + "," + self.__nutritions + "," + self.__cooking_time + "," + self.__description + ") values (" + "'" + recipe_name + "'" + "," + "'" + str(
                category_id) + "'" + "," + "'" + nutritions + "'" + "," + "'" + cooking_time + "'" + "," + "'" + description + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert recipe")
            return False


    def get_one_recipe(self,recipe_id):
        info = ""
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_get_one_recipe = "Select * from " + self.__tablename + " where " + self.__recipe_id + "=" + "'" + str(recipe_id) + "'"
            cursor = conn.execute(str_get_one_recipe)
            rows = cursor.fetchall()
            print(len(rows))
            for row in rows:
                info = "Recipe Id: " + str(row[0]) + "  Recipe name: " + row[1] + "  Category Id: " + str(
                    row[2]) + "  Nutritions: " + row[3] + "  Cooking Time: " + row[4] + "  Description: " + row[5]
                print(row[0], row[1], row[2], row[3], row[4],row[5])
            conn.close()
            if len(rows) == 0:
                info = "Not found"
            return info
        except:
            return "Trouble in DataBase"

    # def get_all_recipes(self):
    #     conn = sqlite3.connect('project_recipes.db')
    #     str_get_all_recipes = "Select * from "+ self.__tablename
    #     cursor = conn.execute(str_get_all_recipes)
    #     for row in cursor:
    #         print("recipe_id=", row[0])
    #         print("recipe_name=", row[1])
    #         print("category_id=", row[2])
    #         print("nutritions=", row[3])
    #         print("cooking_time=", row[4])
    #         print("description=",row[5])
    #         print("_____________________________________")
    #     print("Success")
    #     conn.close()

    def get_one_recipe2(self):
        conn = sqlite3.connect('project_recipes.db')
        str = ("""
                SELECT recipe_id, recipe_name, CategoryDb.category_name, nutritions, cooking_time,description 
                FROM CategoryDb
                INNER JOIN RecipesDb ON RecipesDb.category_id = CategoryDb.category_id
                """)
        cursor = conn.execute(str)
        for row in cursor:
            print("recipe_id =", row[0])
            print("recipe_name =", row[1])
            print("category_name =", row[2])
            print("nutritions =", row[3])
            print("cooking_time =", row[4])
            print("description =", row[5])
        conn.commit()
        conn.close()

    def delete_recipe(self, recipe_id):
        conn = sqlite3.connect('project_recipes.db')
        str_delete_recipe = "Delete from " + self.__tablename + "where " + self.__recipe_id + "=" + "'" + str(recipe_id) + "'"
        print(str_delete_recipe)
        conn.execute(str_delete_recipe)
        conn.commit()
        conn.close()
        print("Recipe deleted successfully")

    def check_recipe(self, recipe_id):
        conn1 = sqlite3.connect('project_recipes.db')
        str_if_exist = "Select * from " + self.__tablename + " where " + self.__recipe_id + " = " + "'" + str(recipe_id) + "'"
        print(str_if_exist)
        cursor = conn1.execute(str_if_exist)
        row = cursor.fetchall()
        if row:
            print("Recipe already exists in table")
            return True
        else:
            print("Recipe not exists in table")
            return False

class CategoryDb(object):
    def __init__(self, tablename="CategoryDb", category_id="category_id",category_name="category_name",number_of_recipes="number_of_recipes"):
        self.__tablename=tablename
        self.__category_id=category_id
        self.__category_name=category_name
        self.__number_of_recipes=number_of_recipes

        conn = sqlite3.connect('project_recipes.db')
        #print("Database opened successfully")
        str = "Create table if not exists " + self.__tablename + "(" + self.__category_id + " "+ "integer primary key autoincrement ,"
        str+=" " + self.__category_name + " text not null ,"
        str+=" " + self.__number_of_recipes + " integer not null )"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_category(self, category_name,number_of_recipes):
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_insert = "Insert into " + self.__tablename + " (" + self.__category_name + "," + self.__number_of_recipes + ") values (" + "'" + category_name + "'" + "," + "'" + str(number_of_recipes) + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert category")
            return False


    def get_one_category(self,category_id):
        info = ""
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_get_one_category = "Select * from " + self.__tablename + " where " + self.__category_id + "=" + "'" + str(category_id) + "'"
            cursor = conn.execute(str_get_one_category)
            rows = cursor.fetchall()
            print(len(rows))
            for row in rows:
                info = "Category Id: " + str(row[0]) + "  Category Name: " + row[1] + "  Number of recipes: " + str(row[2])
                print(row[0], row[1], row[2])
            conn.close()
            if len(rows) == 0:
                info = "Category is not found in the table"
            return info
        except:
            return "Trouble in DataBase"

    def get_num_of_recipes(self,category_name):
        info= ""
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_get_num_of_recipes="Select number_of_recipes from " +self.__tablename+" where "+ self.__category_name + "=" + "'" + category_name + "'"
            cursor = conn.execute(str_get_num_of_recipes)
            rows = cursor.fetchall()
            #print(len(rows))
            for row in rows:
                info = "Number of recipes: " + str(row[0])
                #print(row[0])
            conn.close()
            if len(rows) == 0:
                info = "Category is not found in the table"
            return info
        except:
            return "Trouble in DataBase"

    def delete_category(self,category_id):
        conn = sqlite3.connect('project_recipes.db')
        str_delete_category = "Delete from " + self.__tablename + "where " + self.__category_id + "=" + "'" + str(category_id) + "'"
        print(str_delete_category)
        conn.execute(str_delete_category)
        conn.commit()
        conn.close()
        print("Category deleted successfully")

    def update_number_of_recipes(self,category_id,number_of_recipes):
        conn = sqlite3.connect('project_recipes.db')
        str_update_num_of_recipes = "Update " + self.__tablename + "set " + self.__number_of_recipes + "=" + "'" + str(number_of_recipes) + "'"
        str_update_num_of_recipes += " where " + self.__category_id + "=" + "'" + str(category_id) + "'"
        print(str_update_num_of_recipes)
        conn.execute(str_update_num_of_recipes)
        conn.commit()
        conn.close()
        print("Number of recipes updated successfully")



class UsersDb(object):
    def __init__(self, tablename="UsersDb",user_id="user_id", user_email="user_email", user_name="user_name", password="password"):
        self.__tablename=tablename
        self.__user_id=user_id
        self.__user_email=user_email
        self.__user_name=user_name
        self.__password=password

        conn=sqlite3.connect('project_recipes.db')
        #print("Database opened successfully")
        str= "Create table if not exists " + self.__tablename + "(" + self.__user_id + " "+ "integer primary key autoincrement ,"
        str+= " " + self.__user_email + " text not null ,"
        str+= " " + self.__user_name + " text not null ,"
        str+= " " + self.__password + " text not null )"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_user(self, user_email, user_name, password):
        try:
            conn = sqlite3.connect('project_recipes.db')
            salt = "ARINA"
            md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
            str_insert = "Insert into " + self.__tablename + " (" + self.__user_email + "," + self.__user_name + "," + self.__password + ") values (" + "'" + user_email + "'" + "," + "'" + user_name + "'" + "," + "'" + str(md5hash) + "');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert user")
            return False


    def get_one_user(self, user_id):
        info = ""
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_get_one_user = "Select * from " + self.__tablename + " where " + self.__user_id + "=" + "'" + str(
                user_id) + "'"
            cursor = conn.execute(str_get_one_user)
            rows = cursor.fetchall()
            print(len(rows))
            for row in rows:
                info = "User Id: " + str(row[0]) + "  User Email: " + row[1] + "  User Name: " + row[2] + "  Password: "+ row[3]
                print(row[0], row[1], row[2],row[3])
            conn.close()
            if len(rows) == 0:
                info = "User is not found in the table"
            return info
        except:
            return "Trouble in DataBase"


    def get_all_users(self):
        conn = sqlite3.connect('project_recipes.db')
        str_get_all_users = "Select * from "+ self.__tablename
        cursor = conn.execute(str_get_all_users)
        for row in cursor:
            print("User_id=", row[0])
            print("User_email=", row[1])
            print("User_name=", row[2])
            print("Password=", row[3])
            print("_____________________________________")
        print("Success")
        conn.close()


    def check_user(self,user_name, password):
        conn = sqlite3.connect('project_recipes.db')
        salt = "ARINA"
        md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
        str_is_exist = "SELECT * from " + self.__tablename + " where " + self.__user_name + " = '" + user_name + "' and " + self.__password + " = '" + str(
            md5hash) + "'"
        print(str_is_exist)
        cursor = conn.execute(str_is_exist)
        row = cursor.fetchall()
        if row:
            print("User is exist in table")
            return True
        else:
            print("User is not exist in table")
            return False

    def update_email(self, user_id,user_email):
        conn = sqlite3.connect('project_recipes.db')
        str_update_email = "Update " + self.__tablename + "set " + self.__user_email + "=" + "'" +user_email + "'"
        str_update_email += " where " + self.__user_id + "=" + "'" + str(user_id) + "'"
        print(str_update_email)
        conn.execute(str_update_email)
        conn.commit()
        conn.close()
        print("Email updated successfully")

class IngredientsDb(object):
    def __init__(self, tablename="IngredientsDb",ingredient_id="ingredient_id",ingredient_name="ingredient_name",ingredient_amount="ingredient_amount",recipe_id="recipe_id"):
        self.__tablename=tablename
        self.__ingredient_id=ingredient_id
        self.__ingredient_name=ingredient_name
        self.__ingredient_amount=ingredient_amount
        self.__recipe_id = recipe_id

        conn=sqlite3.connect('project_recipes.db')
        str = "Create table if not exists " + self.__tablename + "(" + self.__ingredient_id + " " + "integer primary key autoincrement ,"
        str += " " + self.__ingredient_name + " text not null ,"
        str += " " + self.__ingredient_amount + " text not null ,"
        str += " " + self.__recipe_id + " integer not null )"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_ingredient(self, ingredient_name, ingredient_amount, recipe_id):
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_insert = "Insert into " + self.__tablename + " (" + self.__ingredient_name + "," + self.__ingredient_amount + ","+ self.__recipe_id + ") values (" + "'" + ingredient_name + "'" + "," + "'" + ingredient_amount + "'" + "," + "'" + str(recipe_id) +"');"
            print(str_insert)
            conn.execute(str_insert)
            conn.commit()
            conn.close()
            print("Record created successfully")
            return True
        except:
            print("Failed to insert category")
            return False

    def get_one_ingredient(self, ingredient_id):
        info = ""
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_get_one_ingredient = "Select * from " + self.__tablename + " where " + self.__ingredient_id + "=" + "'" + str(
                ingredient_id) + "'"
            cursor = conn.execute(str_get_one_ingredient)
            rows = cursor.fetchall()
            print(len(rows))
            for row in rows:
                info = "Ingredient id: " + str(row[0]) + "  Ingredient Name: " + row[1] + "  Ingredient Amount: " + str(
                    row[2]) + "Recipe id: " + str(row[3])
                print(row[0], row[1], row[2],row[3])
            conn.close()
            if len(rows) == 0:
                info = "Not found"
            return info
        except:
            return "Trouble on db"

    def get_all_ingredients(self):
        conn = sqlite3.connect('project_recipes.db')
        str_get_all_ingredients = "Select * from "+ self.__tablename
        cursor = conn.execute(str_get_all_ingredients)
        for row in cursor:
            print("Ingredient_id=", row[0])
            print("Ingredient_name=", row[1])
            print("Ingredient_amount=", row[2])
            print("Recipe_id",row[3])
            print("_____________________________________")
        print("Success")
        conn.close()

    def get_one_ingredient2(self):
        conn = sqlite3.connect('project_recipes.db')
        str = ("""
                SELECT ingredient_id, ingredient_name, ingredient_amount, RecipesDb.recipe_name 
                FROM RecipesDb
                INNER JOIN IngredientsDb ON IngredientsDb.recipe_id = RecipesDb.recipe_id
                """)
        cursor = conn.execute(str)
        for row in cursor:
            print("ingredient_id =", row[0])
            print("ingredient_name =", row[1])
            print("ingredient_amount =", row[2])
            print("recipe_name =", row[3])
        conn.commit()
        conn.close()

    def check_ingredient(self,ingredient_id):
        conn1 = sqlite3.connect('project_recipes.db')
        str_if_exist = "Select * from " + self.__tablename + " where " + self.__ingredient_id + " = " + "'" + str(
            ingredient_id) + "'"
        print(str_if_exist)
        cursor = conn1.execute(str_if_exist)
        row = cursor.fetchall()
        if row:
            print("Ingredient already exists in table")
            return True
        else:
            print("Ingredient not exists in table")
            return False

    def delete_ingredient(self,ingredient_id):
        conn = sqlite3.connect('project_recipes.db')
        str_delete_ingredient = "Delete from " + self.__tablename + "where " + self.__ingredient_id + "=" + "'" + str(
            ingredient_id) + "'"
        print(str_delete_ingredient)
        conn.execute(str_delete_ingredient)
        conn.commit()
        conn.close()
        print("Ingredient deleted successfully")


def JoinRecipesTblToCategoryTbl():
    conn = sqlite3.connect('project_recipes.db')
    str= ("""
            SELECT recipe_id, recipe_name, CategoryDb.category_name, nutritions, cooking_time,description 
            FROM CategoryDb
            INNER JOIN RecipesDb ON RecipesDb.category_id = CategoryDb.category_id
            """)
    cursor = conn.execute(str)
    for row in cursor:
        print("recipe_id =", row[0])
        print("recipe_name =", row[1])
        print("category_name =", row[2])
        print("nutritions =", row[3])
        print("cooking_time =", row[4])
        print("description =", row[5])
    conn.commit()
    conn.close()



R=RecipesDb()
C=CategoryDb()
U=UsersDb()
I=IngredientsDb()
#______________________________________________________________________________________________________________________________________
# R.insert_recipe("Aussie Sausage Rolls",1,"116 calories","40 minutes","""Preheat oven to 350°. Combine first 6 ingredients and 3/4 teaspoon paprika. Add sausage; mix lightly but thoroughly.
#                 On a lightly floured surface, roll each pastry sheet into an 11x10-1/2-in. rectangle. Cut lengthwise into 3 strips. Spread 1/2 cup sausage mixture lengthwise down the center of each strip. Fold over sides, pinching edges to seal. Cut each log into 6 pieces.
#                 Place on a rack in a 15x10x1-in. pan, seam side down. Sprinkle with remaining 1/4 teaspoon paprika. Bake until golden brown and sausage is no longer pink, 20-25 minutes.""")
# R.insert_recipe("Chicken & Bacon Roll Ups",1,"43 calories","20 minutes","Mix chicken, cream cheese, 1/2 cup salsa and bacon; spread over tortillas. Roll up tightly; wrap. Refrigerate at least 1 hour. "
#                                                                         "Just before serving, unwrap and cut tortillas into 1-in. slices. Serve with remaining salsa.")
# R.insert_recipe("Party Shrimps",1,"14 calories","25 minutes","""In a bowl or shallow dish, combine the first 7 ingredients. Add shrimp; toss to coat. Refrigerate 2 hours.
#                 Drain shrimp, discarding marinade. Place shrimp on an ungreased baking sheet. Broil 4 in. from heat until shrimp turn pink, 3-4 minutes on each side.""")
# R.insert_recipe("South-of-the-Border Bruschetta",1,"62 calories","25 minutes","""In a small bowl, mix avocados, cilantro, chili peppers and salt. Finely grate zest from limes. Cut limes crosswise in half; squeeze juice from limes. Stir lime zest and juice into avocado mixture. Refrigerate 30 minutes.
#                 Preheat broiler. Place bread slices on an ungreased baking sheet. Broil 3-4 in. from heat 1-2 minutes on each side or until golden brown. Top with avocado mixture. If desired, sprinkle with cheese.""")
# R.insert_recipe("Champion Chicken Puffs",1,"67 calories","30 minutes","""Preheat oven to 375°. In a small bowl, beat cream cheese and garlic powder until smooth. Stir in chicken.
#                 Unroll crescent dough; separate into 16 triangles. Cut each triangle in half lengthwise, forming 2 triangles. Place 1 teaspoon chicken mixture in the center of each. Fold short side over filling; press sides to seal and roll up.
#                 Place 1 in. apart on greased baking sheets. Bake until golden brown, 12-14 minutes. Serve warm.""")
# #__________________________________________________________________________________________________________________________
# C.insert_category("Appetizers",4)
# C.insert_category("Soups",4)
# C.insert_category("Main Dishes",5)
# C.insert_category("Salads",5)
# C.insert_category("Deserts",3)
# C.insert_category("Drinks",3)
# #__________________________________________________________________
# U.insert_user("arina@gmail.com","arina24","1234")
# #______________________________________________________
#
# I.insert_ingredient("Onion","1 medium",1)
# I.insert_ingredient("Minced fresh chives","2 tablespoons",1)
# I.insert_ingredient("Minced fresh basil","2 teaspoons",1)
# I.insert_ingredient("Garlic cloves","2 pieces",1)
# I.insert_ingredient("Salt","1/2 teaspoon",1)
# I.insert_ingredient("Pepper","1/4 teaspoon",1)
# I.insert_ingredient("Paprika","1 teaspoon",1)
# I.insert_ingredient("Pork sausage","1-1/4 pounds",1)
# I.insert_ingredient("Frozen puff pastry","1 package",1)
# #______________________________________________________
# I.insert_ingredient("White chicken","1 can",2)
# I.insert_ingredient("Vegetable cream cheese","1 carton",2)
# I.insert_ingredient("Salsa","1 cup",2)
# I.insert_ingredient("Cooked bacon","4 pieces",2)
# I.insert_ingredient("Flour tortillas","6 pieces",2)
# #_______________________________________________________
# I.insert_ingredient("Olive oil","1 tablespoon",3)
# I.insert_ingredient("Brown sugar","1-1/2 teaspoons",3)
# I.insert_ingredient("Garlic clove","1 piece",3)
# I.insert_ingredient("Lemon juice","1-1/2 teaspoons",3)
# I.insert_ingredient("Paprika","1/2 teaspoon",3)
# I.insert_ingredient("Dried basil","1/2 teaspoon",3)
# I.insert_ingredient("Pepper","1/3 teaspoon",3)
# I.insert_ingredient("Uncooked shrimp","1 pound",3)
# #________________________________________________________
# I.insert_ingredient("Avocado","2 medium pieces",4)
# I.insert_ingredient("Minced fresh cilantro","3 tablespoons",4)
# I.insert_ingredient("Red chili peppers","2 pieces",4)
# I.insert_ingredient("Salt","1/4 teaspoon",4)
# I.insert_ingredient("Lime","2 small pieces",4)
# I.insert_ingredient("French bread baguette","12 slices",4)
# #_________________________________________________________
# I.insert_ingredient("Cream cheese","4 ounces",5)
# I.insert_ingredient("Garlic powder","1/2 teaspoon",5)
# I.insert_ingredient("Shredded cooked chicken","1/2 cup",5)
# I.insert_ingredient("Refrigerated crescent rolls","16 ounces",5)
# #_________________________________________________________
# R.get_one_recipe2()
# I.get_one_ingredient2()
# print("_____________________________")
# C.get_num_of_recipes("Salads")
#
