import socket
import threading
from Db_classes import *
import ast

class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.running = True
        self.count = 0
        self.UserDb = UsersDb()
        self.CategoryDb = CategoryDb()
        self.RecipesDb = RecipesDb()
        self.IngredientsDb = IngredientsDb()
        self.HistoryRecipesDb = HistoryRecipesDb()
        self.FavoritesRecipesDb = FavoritesRecipesDb()
        self.SendReceiveRecipesDb = SendReceiveRecipesDb()
        self.ShoppingListDb = ShoppingListDb()

    def start(self):
        try:
            print('Server starting up on ip %s port %s' % (self.ip, self.port))
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip, self.port))
            self.sock.listen(3)

            while True:
                print(' Waiting for a new client')
                clientSocket, client_addresses = self.sock.accept()
                print('New client entered')
                clientSocket.send('Hello this is server'.encode())
                self.count += 1
                print(self.count)
                self.handleClient(clientSocket)

        except socket.error as e:
            print(e)

    def handleClient(self, clientSock):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock,))
        client_handler.start()

    def handle_client_connection(self, client_socket):
        not_crash = True
        # print(not_crash)
        while self.running:
            while not_crash:
                try:
                    server_data = client_socket.recv(1024).decode('utf-8')
                    # print(server_data)
                    arr=server_data.split("*")
                    # print(arr)
                    if arr!=None and arr[0]=="signup" and len(arr)==4:
                        print("Sign up user")
                        print(arr)
                        server_data=self.UserDb.insert_user(arr[1],arr[2],arr[3])
                        print("Server data: ",server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Signed up successfully".encode())
                        elif server_data==False:
                            client_socket.send("Sign up failed".encode())
                        elif server_data=="Exists":
                            client_socket.send("Already exists".encode())
                    #_____________________________________________
                    elif arr!=None and arr[0]=="login" and len(arr)==3:
                        print("Login user")
                        print(arr)
                        server_data = self.UserDb.check_user(arr[1],arr[2])
                        print("Server data: ", server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Loged In successfully".encode())
                        elif server_data==False:
                            client_socket.send("Wrong password".encode())
                        elif server_data=="Fail":
                            client_socket.send("Login failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_category_image" and len(arr)==2:
                        server_data=self.CategoryDb.get_image_path(arr[1])
                        arr_to_send = server_data.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data=="Category is not found in the table":
                            client_socket.send("Search for num of recipes failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_num_of_recipes" and len(arr)==2:
                        server_data=self.CategoryDb.get_num_of_recipes(arr[1])
                        # print("Server data: ", server_data)
                        arr_to_send = server_data.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data=="Category is not found in the table":
                            client_socket.send("Search for num of recipes failed".encode())
                     # _____________________________________________
                    elif arr != None and arr[0] == "get_all_recipes_names" and len(arr) == 1:
                        server_data = self.RecipesDb.get_recipe_names()
                        # print("Server data: ", server_data)
                        arr_to_send = "*".join(server_data)
                        arr_to_send = arr_to_send.encode("utf-8")
                        # print(arr_to_send)
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data == "No recipes in the table":
                            client_socket.send("No recipes found".encode())
                    # _____________________________________________
                    elif arr!= None and arr[0] == "get_one_recipe" and len(arr) == 2:
                        # print(arr)
                        server_data=self.RecipesDb.get_one_recipe(arr[1])
                        print("Server data: ",server_data)
                        arr_to_send= "*".join(server_data)
                        arr_to_send = arr_to_send.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data:
                            client_socket.send("Search for recipe failed".encode())

                    #______________________________________________
                    elif arr!=None and arr[0]=="get_recipe_name_and_image" and len(arr)==2:
                        server_data=self.RecipesDb.get_name_and_image_by_ctg_id(arr[1])
                        print("Server data: ", server_data)
                        if server_data:
                            arr_to_send = "#".join(server_data)
                            arr_to_send = arr_to_send.encode("utf-8")
                            print(arr_to_send)
                            client_socket.send(arr_to_send)
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_ingredients" and len(arr)==2:
                        server_data=self.IngredientsDb.get_ingredients_by_recipe_name(arr[1])
                        print("Server data: ", server_data)
                        arr_to_send = "*".join(server_data)
                        arr_to_send = arr_to_send.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif arr_to_send[0]=="No ingredients":
                            client_socket.send("No users exist".encode())
                    # _____________________________________________
                    elif arr!= None and arr[0] == "get_email" and len(arr) == 2:
                        # print(arr)
                        server_data=self.UserDb.get_email_by_name(arr[1])
                        print("Server data: ",server_data)
                        arr_to_send = server_data.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data:
                            client_socket.send("Search for email failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="change_email" and len(arr)==3:
                        print(arr)
                        server_data=self.UserDb.update_email(arr[1],arr[2])
                        print("Server data: ",server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Email changed successfully".encode())
                        elif server_data==False:
                            client_socket.send("Changing email failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="change_password" and len(arr)==3:
                        print(arr)
                        server_data=self.UserDb.update_password(arr[1],arr[2])
                        print("Server data: ",server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Password changed successfully".encode())
                        elif server_data==False:
                            client_socket.send("Changing password failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0] == "insert_recipe_history" and len(arr)==7:
                        print(arr)
                        server_data=self.HistoryRecipesDb.insert_recipe(arr[1],arr[2],arr[3],arr[4],arr[5],arr[6])
                        print("Server data: ", server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Recipe added to history successfully".encode())
                        elif server_data==False:
                            client_socket.send("Already exists".encode())
                    # _____________________________________________
                    elif arr != None and arr[0] == "clear_history" and len(arr) == 2:
                        print(arr)
                        username = arr[1]
                        print(username)
                        server_data = self.HistoryRecipesDb.delete_all_recipes(username)
                        print("Server data: ", server_data)
                        if server_data==True:
                            client_socket.send("History cleared successfully".encode())
                        elif server_data==False:
                            client_socket.send("Clearing history failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_history" and len(arr)==2:
                        server_data=self.HistoryRecipesDb.get_all_recipes(arr[1])
                        print("Server data: ", server_data)
                        if server_data == 0:
                            arr = []
                            info="Clear"
                            arr = info.split("#")
                            arr_to_send = "#".join(arr)
                            arr_to_send = arr_to_send.encode("utf-8")
                            # print(arr_to_send)
                            client_socket.send(arr_to_send)
                        else:
                            arr_to_send = "#".join(server_data)
                            arr_to_send = arr_to_send.encode("utf-8")
                            print(arr_to_send)
                            client_socket.send(arr_to_send)
                    # _____________________________________________
                    elif arr!=None and arr[0] == "insert_recipe_favorites" and len(arr)==7:
                        # print(arr)
                        server_data=self.FavoritesRecipesDb.insert_recipe(arr[1],arr[2],arr[3],arr[4],arr[5],arr[6])
                        print("Server data: ", server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Recipe added to favorites successfully".encode())
                        elif server_data==False:
                            client_socket.send("Already exists".encode())
                    # _____________________________________________
                    elif arr != None and arr[0] == "clear_favorites" and len(arr) == 2:
                        # print(arr)
                        username = arr[1]
                        # print(username)
                        server_data = self.FavoritesRecipesDb.delete_all_recipes(username)
                        print("Server data: ", server_data)
                        if server_data==True:
                            client_socket.send("Favorites cleared successfully".encode())
                        elif server_data==False:
                            client_socket.send("Clearing history of favorites failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_favorites" and len(arr)==2:
                        server_data=self.FavoritesRecipesDb.get_all_recipes(arr[1])
                        print("Server data: ", server_data)
                        if server_data == 0:
                            arr = []
                            info="Clear"
                            arr = info.split("#")
                            arr_to_send = "#".join(arr)
                            arr_to_send = arr_to_send.encode("utf-8")
                            # print(arr_to_send)
                            client_socket.send(arr_to_send)
                        else:
                            arr_to_send = "#".join(server_data)
                            arr_to_send = arr_to_send.encode("utf-8")
                            print(arr_to_send)
                            client_socket.send(arr_to_send)
                    # _____________________________________________
                    elif arr!=None and arr[0]=="check_favorite_recipe" and len(arr)==3:
                        server_data=self.FavoritesRecipesDb.check_recipe(arr[1],arr[2])
                        print("Server data: ", server_data)
                        if server_data==True:
                            client_socket.send("Recipe already exists in table".encode())
                        elif server_data==False:
                            client_socket.send("Recipe not exists in table".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_all_users" and len(arr)==2:
                        server_data=self.UserDb.get_all_users(arr[1])
                        print("Server data: ", server_data)
                        arr_to_send = "*".join(server_data)
                        arr_to_send = arr_to_send.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data=="No users":
                            client_socket.send("No users exist".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0] == "insert_recipe_to_send" and len(arr)==8:
                        # print(arr)
                        server_data=self.SendReceiveRecipesDb.insert_recipe(arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])
                        print("Server data: ", server_data)
                        if server_data==True:
                            print(server_data)
                            client_socket.send("Recipe added to table successfully".encode())
                        elif server_data==False:
                            client_socket.send("Already exists".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_received_recipes" and len(arr)==2:
                        server_data=self.SendReceiveRecipesDb.get_all_recipes(arr[1])
                        print("Server data: ", server_data)
                        if server_data == 0:
                            arr = []
                            info="Clear"
                            arr = info.split("#")
                            arr_to_send = "#".join(arr)
                            arr_to_send = arr_to_send.encode("utf-8")
                            # print(arr_to_send)
                            client_socket.send(arr_to_send)
                        else:
                            arr_to_send = "#".join(server_data)
                            arr_to_send = arr_to_send.encode("utf-8")
                            print(arr_to_send)
                            client_socket.send(arr_to_send)
                    # _____________________________________________
                    elif arr != None and arr[0] == "clear_received_recipes" and len(arr) == 2:
                        # print(arr)
                        username = arr[1]
                        server_data = self.SendReceiveRecipesDb.delete_all_recipes(username)
                        print("Server data: ", server_data)
                        if server_data==True:
                            client_socket.send("Received recipes cleared successfully".encode())
                        elif server_data==False:
                            client_socket.send("Clearing history of received recipes failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="insert_ingredient" and len(arr)==3:
                        server_data=self.ShoppingListDb.insert_ingredient(arr[1],arr[2])
                        print("Server data: ", server_data)
                        if server_data == True:
                            print(server_data)
                            client_socket.send("Ingredient added to table successfully".encode())
                        elif server_data == False:
                            client_socket.send("Already exists".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="get_ingredients_by_username" and len(arr)==2:
                        server_data=self.ShoppingListDb.get_ingredients_by_username(arr[1])
                        print("Server data: ", server_data)
                        if server_data == 0:
                            arr = []
                            info = "Clear"
                            arr = info.split("#")
                            arr_to_send = "#".join(arr)
                            arr_to_send = arr_to_send.encode("utf-8")
                            # print(arr_to_send)
                            client_socket.send(arr_to_send)
                        else:
                            arr_to_send = "#".join(server_data)
                            arr_to_send = arr_to_send.encode("utf-8")
                            print(arr_to_send)
                            client_socket.send(arr_to_send)
                    # _____________________________________________
                    elif arr != None and arr[0] == "clear_shopping_list" and len(arr) == 3:
                        arr_ingredients=ast.literal_eval(arr[1])
                        server_data = self.ShoppingListDb.delete_ingredients_by_name_and_username(arr_ingredients,arr[2])
                        print("Server data: ", server_data)
                        if server_data==True:
                            client_socket.send("Shopping list cleared successfully".encode())
                        elif server_data==False:
                            client_socket.send("Clearing shopping list failed".encode())
                    # _____________________________________________
                    elif arr!=None and arr[0]=="log_out" and len(arr)==1:
                        client_socket.send("Server is shutting down".encode())
                        client_socket.close()
                        self.running = False
                        self.sock.close()
                    else:
                        server_data = "False"

                except:
                    print("Error")
                    not_crash=False
                    break


if __name__ == '__main__':
   ip = '127.0.0.1'
   port = 1803
   S = Server(ip, port)
   S.start()