poiss = int(input("Mitu pöialpoissi soovib õunu? "))
i = 0
from random import randint
õuntearv = 0
while i < poiss:
    i += 1
    õunad = (randint(1, 2))
    print(str(õunad))
    õuntearv += õunad
print ("Lumivalgekesele jäi " + str(14 - (int(õunad))) + " õuna.")