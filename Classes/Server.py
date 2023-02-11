import socket
import threading
from Db_classes import *

class Server(object):
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.running=True
        self.count=0
        self.UserDb=UsersDb()
        self.RecipesDb=RecipesDb()

    def start(self):
        try:
            print('server starting up on ip %s port %s' % (self.ip, self.port))
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.ip, self.port))
            self.sock.listen(3)

            while True:
                print('waiting for a new client')
                clientSocket, client_addresses = self.sock.accept()
                print('new client entered')
                clientSocket.send('Hello this is server'.encode())
                self.count += 1
                print(self.count)
                self.handleClient(clientSocket, self.count)

        except socket.error as e:
            print(e)

    def handleClient(self, clientSock, current):
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        client_handler.start()

    def handle_client_connection(self, client_socket,current):
        not_crash = True
        print(not_crash)
        while self.running:
            while not_crash:
                try:
                    server_data = client_socket.recv(1024).decode('utf-8')
                    arr=server_data.split(",")
                    print(server_data)
                    if arr!=None and arr[0]=="signup" and len(arr)==4:
                        print("Sign up user")
                        print(arr)
                        server_data=self.UserDb.insert_user(arr[1],arr[2],arr[3])
                        print("Server data: ",server_data)
                        if server_data:
                            print(server_data)
                            client_socket.send("Signed up successfully".encode())
                        elif server_data:
                            client_socket.send("Sign up failed".encode())
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
                            client_socket.send("Log In failed".encode())
                            # _____________________________________________
                    elif arr != None and arr[0] == "get_all_users" and len(arr) == 1:
                        print("get_all_users")
                        server_data = self.UserDb.get_all_users()
                        server_data = ",".join(server_data)  # convert data to string
                    elif arr!= None and arr[0] == "get_one_recipe" and len(arr) == 2:
                        print(arr)
                        server_data=self.RecipesDb.get_one_recipe(arr[1])
                        print("Server data: ",server_data)
                        arr_to_send= "*".join(server_data)
                        arr_to_send = arr_to_send.encode("utf-8")
                        if server_data:
                            client_socket.send(arr_to_send)
                        elif server_data:
                            client_socket.send("Search for recipe failed".encode())
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