import socket,optparse,sys,threading

parser = optparse.OptionParser('Usage: '+ sys.argv[0] + ' -t <ip_target> -p <ports_list>')
parser.add_option('-t','--target', dest='target_ip', type='string', help='specify target ip')
parser.add_option('-p','--ports', dest='ports', type='string', help='specify target ports')

options, args = parser.parse_args()

# a ameliorer (verifier si ip est valide and ports est valide)

# log time start socket

if options.target_ip==None or options.ports==None:
    print(parser.usage)
    exit(0)

ip=options.target_ip
ports = options.ports.split(',')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def scanPort(ip, port):
    try:  
        result = s.connect_ex((ip,int(port)))
        if result == 0:
            print(f"port : {port} is open")
        else:
            print(f"port : {port} is closed")  
    except Exception as e:
        print(f"error : {e}")
    
    finally:
        s.close()
        
        
for port in ports:
    t=threading.Thread(target=scanPort, args=(ip,int(port)))
    t.start()
    
            

