#defineerin funktsiooni, argumendid
def inimeste_arv(naiskondade_arv, tugiisikute_arv):
    vastavalt_inimesi = naiskondade_arv * (22 + tugiisikute_arv)
    return vastavalt_inimesi
#kasutaja sisend
koht = input("Kus toimusid maailmameistrivõistlused: ")
print("Turniirid toimusid " + (koht))
turniiride_arv = int(input("Kui palju turniiri toimus: "))
#leian juhuarvu vahemikust 10, 30
from random import randint
naiskondade_arv = 0
juhuslik = []
i = 1
inimesi_kokku = 0
while(i<=turniiride_arv):
    juhuslik.append(randint(10, 30))
    i += 1
    kokku = 0
#et funktsioon toimiks, kutsun impordi
#leian vastavalt reeglitele, kas tugiisikuid on 8 või 10 - vastavalt võistkondade arvule
for naiskondade_arv in juhuslik:
    if naiskondade_arv > 15:
        tugiisikute_arv = 8
    elif naiskondade_arv <= 15:
        tugiisikute_arv = 10
        print("Turniiril oli " + str(naiskondade_arv) + " naiskondi ja vastavalt inimesi: " + str(inimeste_arv(naiskondade_arv, tugiisikute_arv)))
#leian naiskondadega seotud inimeste arvu igal turniiril - vastavalt valemi järgi
vastavalt_inimesi = naiskondade_arv * (22 + tugiisikute_arv)
#leian kõikidel turniiridel kokku olnud naiskondadega seotud isiktue arvu, kuid kahuks ei ole turniiride arv leitud
inimesi_kokku = turniiride_arv * naiskondade_arv * tugiisikute_arv
#väljund
print("Turniiril oli " + str(naiskondade_arv) + " naiskondi ja vastavalt inimesi: " + str(vastavalt_inimesi))
print("Kokku oli kõigil turniiridel inimesi: " + str(inimesi_kokku))