#kasutaja sisend
#äratamise korrad kokku
kordamine = int(input("Sisestage mitu korda äratada: "))
#valmistame tsükli juhtimismuutuja
kord = 1
#nii kaua kui kord muutuja jooksev väärtus ei ületa kordamine väärtust
while (kord <= kordamine):
    #ärata
    print("Tõuse ja sära")
    #suurenda juhtimismuutuja väärtus 1 võrra
    kord += 1 #kord = kord + 1