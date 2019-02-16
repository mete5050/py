import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
####################################################
#Sag
global ms1a=3
global msa2=5
global mso1=7
global mso2=11
#############
#Sol
global msoa1=13
global msoa2=15
global msoo1=19
global msoo2=21
####################################################
GPIO.setup(ms1a, GPIO.OUT)
GPIO.setup(msa2, GPIO.OUT)
GPIO.setup(mso1, GPIO.OUT)
GPIO.setup(mso2, GPIO.OUT)
#############
GPIO.setup(msoa1,GPIO.OUT)
GPIO.setup(msoa2,GPIO.OUT)
GPIO.setup(msoo1,GPIO.OUT)
GPIO.setup(msoo2,GPIO.OUT)
####################################################
def ileri():
    #sag ileri
    GPIO.output(ms1a,GPIO.HIGH)
    GPIO.output(msa2,GPIO.LOW)
    GPIO.output(mso1,GPIO.HIGH)
    GPIO.output(mso2,GPIO.LOW)
    ##########################
    #sol ileri
    GPIO.output(msoa1,GPIO.HIGH)
    GPIO.output(msoa2,GPIO.LOW)
    GPIO.output(msoo1,GPIO.HIGH)
    GPIO.output(msoo2,GPIO.LOW)
####################################################
def geri():
    #sag geri
    GPIO.output(ms1a,GPIO.LOW)
    GPIO.output(msa2,GPIO.HIGH)
    GPIO.output(mso1,GPIO.LOW)
    GPIO.output(mso2,GPIO.HIGH)
    ##########################
    #sol geri
    GPIO.output(msoa1,GPIO.LOW)
    GPIO.output(msoa2,GPIO.HIGH)
    GPIO.output(msoo1,GPIO.LOW)
    GPIO.output(msoo2,GPIO.HIGH)
####################################################
def sag()
    #sag geri
    GPIO.output(ms1a,GPIO.LOW)
    GPIO.output(msa2,GPIO.HIGH)
    GPIO.output(mso1,GPIO.LOW)
    GPIO.output(mso2,GPIO.HIGH)
    ##########################
    #sol ileri
    GPIO.output(msoa1,GPIO.HIGH)
    GPIO.output(msoa2,GPIO.LOW)
    GPIO.output(msoo1,GPIO.HIGH)
    GPIO.output(msoo2,GPIO.LOW)
####################################################
def sol():
    #sag ileri
    GPIO.output(ms1a,GPIO.HIGH)
    GPIO.output(msa2,GPIO.LOW)
    GPIO.output(mso1,GPIO.HIGH)
    GPIO.output(mso2,GPIO.LOW)
    ##########################
    GPIO.output(msoa1,GPIO.LOW)
    GPIO.output(msoa2,GPIO.HIGH)
    GPIO.output(msoo1,GPIO.LOW)
    GPIO.output(msoo2,GPIO.HIGH)
####################################################
def dur():
    #sag dur
    GPIO.output(ms1a,GPIO.LOW)
    GPIO.output(msa2,GPIO.LOW)
    GPIO.output(mso1,GPIO.LOW)
    GPIO.output(mso2,GPIO.LOW)  
    ##########################  
    #sol dur
    GPIO.output(msoa1,GPIO.LOW)
    GPIO.output(msoa2,GPIO.LOW)
    GPIO.output(msoo1,GPIO.LOW)
    GPIO.output(msoo2,GPIO.LOW)
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
basla = True
while basla:

    if( ==""):
      ileri()
      print("ileri \n")
####################################################
    if( ==""):
       geri()
       print("geri \n")
####################################################
    if( ==""):
       sag()
       print("sag \n")
####################################################
    if( ==""):
       sol()
       print("sol \n")
####################################################
    if( ==""):
       dur()
       print("dur \n")









GPIO.cleanup()
