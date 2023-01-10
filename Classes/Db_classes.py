import sqlite3
import hashlib
class RecipesDb(object):
    def __init__(self, tablename="RecipesDb",recipe_id="recipe_id", recipe_name="recipe_name", category_id="category_id", nutritions="nutritions", cooking_time="cooking_time", ingredient_id="ingredient_id", description="description"):
        self.__tablename=tablename
        self.__recipe_id=recipe_id
        self.__recipe_name=recipe_name
        self.__category_id=category_id
        self.__nutritions=nutritions
        self.__cooking_time=cooking_time
        self.__ingredient_id=ingredient_id
        self.__description=description

        conn=sqlite3.connect('project_recipes.db')
        print("Database opened successfuly")
        str= "Create table if not exists " + self.__tablename + "(" + self.__recipe_id + " " + "integer primary key autoincrement ,"
        str+= " " + self.__recipe_name + " text not null ,"
        str+= " " + self.__category_id + " integer not null ,"
        str+= " " + self.__nutritions + " integer not null ,"
        str+= " " + self.__cooking_time + " integer not null ,"
        str+= " " + self.__ingredient_id + " integer not null ,"
        str+= " " + self.__description + " text not null ,"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_recipe(self, recipe_name, category_id,nutritions,cooking_time, ingredient_id, description):
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_insert = "Insert into " + self.__tablename + " (" + self.__recipe_name + "," + self.__category_id + "," + self.__nutritions + "," + self.__cooking_time + "," + self.__ingredient_id + "," + self.__description + ") values (" + "'" + recipe_name + "'" + "," + "'" + str(
                category_id) + "'" + "," + "'" + nutritions + "'" + "," + "'" + str(
                cooking_time) + "'" + "," + "'" + str(ingredient_id) + "'" + "," + "'" + description + "');"
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
                    row[2]) + "  Nutritions: " + str(row[3]) + "  Cooking Time: " + str(row[4]) + "  Ingrediend Id: " + str(row[5])+ "  Description: " + row[6]
                print(row[0], row[1], row[2], row[3], row[4],row[5],row[6])
            conn.close()
            if len(rows) == 0:
                info = "Not found"
            return info
        except:
            return "Trouble in DataBase"

    def get_all_recipes(self):
        conn = sqlite3.connect('project_recipes.db')
        str_get_all_recipes = "Select * from "+ self.__tablename
        cursor = conn.execute(str_get_all_recipes)
        for row in cursor:
            print("recipe_id=", row[0])
            print("recipe_name=", row[1])
            print("category_id=", row[2])
            print("nutritions=", row[3])
            print("cooking_time=", row[4])
            print("ingredient_id=", row[5])
            print("description=",row[6])
            print("_____________________________________")
        print("Success")
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
        print("Database opened successfully")
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
        print("Database opened successfully")
        str= "Create table if not exists " + self.__tablename + "(" + self.__user_id + " "+ "integer primary key autoincrement ,"
        str+= " " + self.__user_email + " text not null ,"
        str+= " " + self.__user_name + " text not null ,"
        str+= " " + self.__password + " text not null ,"
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

    def check_user(self,user_email, password):
        conn = sqlite3.connect('project_recipes.db')
        salt = "ARINA"
        md5hash = hashlib.md5(salt.encode('utf-8') + password.encode()).hexdigest()
        str_is_exist = "SELECT * from " + self.__tablename + " where " + self.__user_email + " = '" + user_email + "' and " + self.__password + " = '" + str(
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

class Ingredients(object):
    def __init__(self, tablename="Ingredients",ingredient_id="ingredient_id",ingredient_name="ingredient_name",ingredient_amount="ingredient_amount" ):
        self.__tablename=tablename
        self.__ingredient_id=ingredient_id
        self.__ingredient_name=ingredient_name
        self.__ingredient_amount=ingredient_amount

        conn=sqlite3.connect('project_recipes.db')
        str = "Create table if not exists " + self.__tablename + "(" + self.__ingredient_id + " " + "integer primary key autoincrement ,"
        str += " " + self.__ingredient_name + " text not null ,"
        str += " " + self.__ingredient_amount + " integer not null )"
        conn.execute(str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def insert_ingredient(self, ingredient_name, ingredient_amount):
        try:
            conn = sqlite3.connect('project_recipes.db')
            str_insert = "Insert into " + self.__tablename + " (" + self.__ingredient_name + "," + self.__ingredient_amount + ") values (" + "'" + ingredient_name + "'" + "," + "'" + str(ingredient_amount) + "');"
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
                    row[2])
                print(row[0], row[1], row[2])
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
            print("_____________________________________")
        print("Success")
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

