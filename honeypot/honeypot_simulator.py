import socket
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor
import argparse 
 
class HoneyPotSimulator:
     
        """
        A class that simulates a honeypot."""
 
        def __init__(self,target_ip='127.0.0.1',intensity='medium'):
            
            self.target_ip = target_ip 
            self.intensity = intensity
            
            #commons ports attack 
            self.target_ports = [21,22,25,80,443,3306,5432,27017,2222]
            
            # Dictionary of common commands used by attackers for different services
            self.attack_patterns = {
                21: [  # FTP commands
                    "USER admin\r\n",
                    "PASS admin123\r\n",
                    "LIST\r\n",
                    "STOR malware.exe\r\n"
                ],
                22: [  # SSH attempts
                    "SSH-2.0-OpenSSH_7.9\r\n",
                    "admin:password123\n",
                    "root:toor\n"
                ],
                80: [  # HTTP requests
                    "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n",
                    "POST /admin HTTP/1.1\r\nHost: localhost\r\nContent-Length: 0\r\n\r\n",
                    "GET /wp-admin HTTP/1.1\r\nHost: localhost\r\n\r\n"
                ]
            }
            #Intensity settings for different attack levels
            self.intensity_settings = {
                "low": {"max_threads": 2, "delay_range": (1, 3)},
                "medium": {"max_threads": 5, "delay_range": (0.5, 1.5)},
                "high": {"max_threads": 10, "delay_range": (0.1, 0.5)}
            }
        
        def simulate_connection(self,port):
            """
            Simulate a connection to a target port."""
            
            try:
                # Create a socket 
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                sock.settimeout(3)
                
                print(f"Connecting to {self.target_ip}:{port}")
                sock.connect((self.target_ip, port)) 
                
                # get banner if any  
                banner = sock.recv(1024) 
                print(f"[+] Received banner from port {port}: {banner.decode('utf-8', 'ignore').strip()}")
                
                if port in self.attack_patterns:
                    for command in self.attack_patterns[port]:
                        print(f"Sending command: {command.strip()}")
                        sock.send(command.encode())
                        
                        # wait for a response  
                        try:
                            response = sock.recv(1024)
                            print(f"Received response: {response.decode('utf-8', 'ignore').strip()}")
                        except socket.timeout:
                            print("Connection timed out. No response received.")
                
                        time.sleep(random.uniform(*self.intensity_settings[self.intensity]['delay_range'])) 
                        
                # Close the socket 
                sock.close() 
            except ConnectionRefusedError:
                print(f"Connection to {self.target_ip}:{port} refused.")
            except socket.timeout:
                print(f"[-] Connection timeout on port {port}")
            except Exception as e:
                print(f"[-] Error connecting to port {port}: {e}")
                
        def simulate_port_scan(self):
            
            """
            Simulate a port scan on the target IP address."""
            
            print(f"Starting port scan on {self.target_ip}")
            
            for port in self.target_ports:
                self.simulate_connection(port)
                time.sleep(random.uniform(0.1,0.3))
                
        def simulate_brute_force(self,port):
            """
            Simulate a brute force attack on a target port.""" 
            
            common_usernames = ["admin", "root", "user", "test"]
            common_passwords = ["password123", "admin123", "123456", "root"]
            
            print(f"Starting brute force attack on port {port}")
            
            for username in common_usernames:
                for password in common_passwords:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(2)
                        sock.connect((self.target_ip, port))
                        
                        if port == 21:
                            sock.send(f"USER {username}\r\n".encode())
                            sock.recv(1024)
                            sock.send(f"PASS {password}\r\n".encode())
                        elif port == 22:
                            sock.send(f"{username}:{password}\n".encode())
                            
                        sock.close()
                        time.sleep(random.uniform(0.1,0.3))
                        
                    except Exception as e:
                        print(f"Error during brute force attack: {e}")
                        
        
        def run_continous_simulation(self,duration=300):
            """
            Runs a continuous simulation for a specified duration."""
            
            print(f"Starting continuous simulation for {duration} seconds")
            print(f"Intensity: {self.intensity}")
            
            end_time = time.time() + duration 
            
            with ThreadPoolExecutor(max_workers=self.intensity_settings[self.intensity]['max_threads']) as executor:
                while time.time() < end_time:
                    # mix of different attacks 
                     simulation_choices=[
                         lambda: self.simulate_port_scan(),
                         lambda: self.simulate_brute_force(21),
                         lambda: self.simulate_brute_force(22),
                         lambda: self.simulate_connection(80),
                     ]
                     # Randomly choose and execute an attack pattern
                     executor.submit(random.choice(simulation_choices))
                     time.sleep(random.uniform(*self.intensity_settings[self.intensity]["delay_range"])) 
                     

def main():
    """
    Main function to run the honeypot simulator with command-line arguments
    """
    parser = argparse.ArgumentParser(description="Honeypot Attack Simulator")
    parser.add_argument("--target", default="127.0.0.1", help="Target IP address")
    parser.add_argument(
        "--intensity",
        choices=["low", "medium", "high"],
        default="medium",
        help="Simulation intensity level"
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=300,
        help="Simulation duration in seconds"
    )

    args = parser.parse_args()

    simulator = HoneyPotSimulator(args.target, args.intensity)

    try:
        simulator.run_continuous_simulation(args.duration)
    except KeyboardInterrupt:
        print("\n[*] Simulation interrupted by user")
    except Exception as e:
        print(f"[-] Simulation error: {e}")
    finally:
        print("\n[*] Simulation complete")
        
if __name__ == "__main__":
    main()