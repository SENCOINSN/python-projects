#! /usr/bin/python3

import threading
import logging
import time

format = "%(asctime)s: %(message)s"

logging.basicConfig(format=format,level=logging.INFO,datefmt="%H:%M:%S")

def threadFunction(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(5)
    logging.info(f"Thread {name} finishing")
    
logging.info("......Creating ........")
t= threading.Thread(target=threadFunction,args=(1,))

logging.info("____Start_______")

t.start()

logging.info("____waiting_______")

t.join() # attendre que le thread termine

print("something")