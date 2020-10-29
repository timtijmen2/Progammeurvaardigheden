import os
import time
factory = ["car", "bike", "chair"]
distribution = []
shop = []
os.system("cls")
print(factory)
print(distribution)
print(shop)
time.sleep(1)
while True:
    
    if not distribution == []:
        shop.append(distribution[0])
        distribution.remove(distribution[0])
    if not factory == []:
        distribution.append(factory[0])
        factory.remove(factory[0])
        time.sleep(1)
    
    

    
    
    os.system("cls")
    print("factory:", factory)
    print("distribution" ,distribution)
    print("shop", shop)
    time.sleep(1)
    if factory == [] and distribution == []:
        kies = input("repeat? Y/N")
        if keis.lower() == "y":
            continue
        elif kies.lower() == "n":
            break