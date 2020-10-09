def eelarve(kylalised):
    sook = 10 * kylalised
    rent = 55
    kokku = sook + rent
    return kokku

# kasutaja sisend
kylaliste_koguarv = int(input("Mitu inimest on kutsutud "))
kylaliste_kindel_arv = int(input("Mitu inimest tuleb "))

# väljund
print("Maksimaalne eelarv on " + str(eelarve(kylaliste_koguarv)) + "eurot")
print("Minimaalne eelarve on " + str(eelarve (kylaliste_kindel_arv)) + "eurot")