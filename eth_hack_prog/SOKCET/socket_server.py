
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket binding
s.bind(('127.0.0.1', 1337))

#socket listening
s.listen()

# getting client 
c,addr = s.accept()

print('got connection from ', addr)

data=c.recv(1024)

print(data.decode('utf-8'))

if data.decode('utf-8') == 'hello':
    c.send(str(['server: hi']).encode('utf-8'))

c.close()
s.close()


    
