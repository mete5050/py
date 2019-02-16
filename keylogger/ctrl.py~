from __future__ import print_function


import pyxhook
import time


def kbevent(event):
    global running


    if event.Ascii == 119:
        print("ileri")
    if event.Ascii == 115:
        print("geri")
    if event.Ascii == 97:
        print("sol")
    if event.Ascii == 100:
        print("sag")


hookman = pyxhook.HookManager()

hookman.KeyDown = kbevent

hookman.HookKeyboard()

hookman.start()


running = True
while running:
    time.sleep(0.1)

hookman.cancel()
