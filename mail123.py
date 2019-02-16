import smtplib   
import socket
calis=True
while(calis):
    try:                        
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("metearduino@gmail.com","mete2002")
        mail.sendmail("metearduino@gmail.com","meteeker2350@gmail.com","Bilgisayariniz internete bagli bir sekilde acildi")
        calis=False 
    except socket.gaierror:
        calis=True

