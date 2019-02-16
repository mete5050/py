import time
import os
def yaz(y,x,yaz):
    a=0
    while(a<=47):

        print(" ")
        if(a==y):
            b=x-1
            print(b * " "+yaz)
            bslk=y+1

        a+=1
os.system("clear")
a=0
b=0
while(True):
    a=0
    b=0
    while(a<=166):
        os.system("clear")
        time.sleep(0.1)
        yaz(1,,"xxx")
        a+=1  
        
    while(b<=47):
        os.system("clear")
        time.sleep(0.1)
        yaz(,,"xxx")
        b+=1

        '''
    while(a>=0):
        os.system("clear")
        time.sleep(0.1)
        yaz(1,a,"xxx")
        a-=1 
    
    while(b>=0):
        os.system("clear")
        time.sleep(0.1)
        yaz(b,0,"xxx")
        b-=1'''
    
