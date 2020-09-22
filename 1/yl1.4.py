# kasutaja sisend
nimi = input("Sisestage oma nimi: ")
lubatud = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik = int(input("Sisestage tegelik kiirus (km/h): "))
# arvutused
#vahe = tegelik - lubatud
#trahv = vahe * 3
trahv = min(190, (tegelik - lubatud ) * 3)
# väljund
print( nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")
