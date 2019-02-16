print ("Sayiyi giriniz : ")
sayi=input()
if(sayi==1):
    print("Bu sayi asal degil")
if(sayi==2):
    print("Bu sayi asal")
if(sayi==3):
    print("Bu sayi asal degil")
i=3
while (i<sayi):
    if (sayi%i==0):
        print("Bu sayi asal degil")
        break
    else:
        i+=1
    if(i==sayi):
        print ("Bu sayi asal")

