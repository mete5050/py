import os
import time
while True:
    os.system("clear")
    
    top_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    
    klr=int(used_m)+390
    yüzdelik_dilimdeki_sayi=klr
    tumsayi=top_m
    
    sonuc = int(yüzdelik_dilimdeki_sayi) * 100 / int(tumsayi)
    
    print("%",int(sonuc))
    time.sleep(0.07)

