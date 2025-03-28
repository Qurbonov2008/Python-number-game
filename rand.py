import random

son = int(input("Son kiriting: (1 dan 100 gacha)"))

rand = random.randint(1,100)


urinish = 0

while rand!=son:
    if rand>son: print("Men o'ylagan son kattaroq\n")
    if rand<son: print("Men o'ylagan son kichikroq\n")
    
    son  = int(input("Son kiriting: "))
    urinish+=1
     
        
        
        
print(f"Siz Toqdingiz Men o'ylagan son {rand} edi\n Siz {urinish} martaada topdingiz ")