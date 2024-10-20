from cryptography.fernet import Fernet
import socket

# generate key 
key = Fernet.generate_key()

print("your key is: ", key)

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind
s.bind(('', 4321))

s.listen()

con,addr = s.accept()
print("connected with ", addr)


# when you receive key 
msg=con.recv(2048).decode()
if msg == 'key':
    con.send(key)
    print("key send !")

