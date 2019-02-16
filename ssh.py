import os
normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pyesil = '\033[92m'
psarı = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan parlak
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'
print(pmavi)
ad = str(input("Bilgisayar adini giriniz: " ))
ip = str(input("IP adresini giriniz: "))
def read():
    os.system("sudo scp "+ad+"@"+ip+":/home/ssh/message.txt dowland")
    message = open("dowland","r")
    print(message.read())
def send():
    os.system("cd /home/ssh")
    os.system("sudo nano message.txt")
def check():
    print(os.system("ls /home/ssh"))
def remove():
    os.system("cd /home/ssh/dowload")
    os.system("sudo rm -")
    os.system("sudo mkdir ssh")
    print(os.system("ls /home"))
    os.system("cd ssh")
    
print(pyesil)
while True:
    grs = input(sari + ">>> "+normal)
    if(grs == "read"):
        read()
    if(grs == "send"):
        send()
    if(grs == "chk"):
        check()
    if(grs == "rmv"):
        remove()































