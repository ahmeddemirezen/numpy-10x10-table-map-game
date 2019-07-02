import numpy as np
import keyboard as kb
import time

liste=[]

for i in range(100):
    liste.append(0)
    

harita=np.array(liste).reshape(10,10)#mapi row ve column bicimine donusturme


print("Map yukleniyor\n",harita)

baslangic=input("Lutfen baslamak istediginiz konumu giriniz.Ornegin=(5,3).Not=map 10x10 buyuklugundedir\n")

b_koordinat=baslangic.split(",")#map koordinat listeleme islemi
try:
    
    
    if  int(b_koordinat[0])>9 or int(b_koordinat[0])<0 or int(b_koordinat[1])>9 or int(b_koordinat[1])<0 :
        print("lutfen min=0 max=9 arasinda deger giriniz. Tekrar deneyiniz.")
        
        
    else:
        print("konum alindi")
        harita[int(b_koordinat[0]),int(b_koordinat[1])]=1
        print(harita)
        
        while True:
            if kb.is_pressed("w"):
                if int(b_koordinat[0])==0:
                    pass
                else:
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=0
                    b_koordinat[0]=int(b_koordinat[0])-1
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=1
                    print(harita)
                    time.sleep(0.1)
                    
            if kb.is_pressed("s"):
                if int(b_koordinat[0])==9:
                    pass
                else:
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=0
                    b_koordinat[0]=int(b_koordinat[0])+1
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=1
                    print(harita)
                    time.sleep(0.1)
                    
            if kb.is_pressed("a"):
                if int(b_koordinat[1])==0:
                    pass
                else:
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=0
                    b_koordinat[1]=int(b_koordinat[1])-1
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=1
                    print(harita)
                    time.sleep(0.1)
                    
            if kb.is_pressed("d"):
                if int(b_koordinat[1])==9:
                    pass
                else:
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=0
                    b_koordinat[1]=int(b_koordinat[1])+1
                    harita[int(b_koordinat[0]),int(b_koordinat[1])]=1
                    print(harita)
                    time.sleep(0.1)

            if kb.is_pressed("q"):
                print("Cikis basarili.")
                break
            
except ValueError:
    print("lutfen (sayi,sayi) seklinde giriniz. Tekrar deneyiniz.") 
    
  

