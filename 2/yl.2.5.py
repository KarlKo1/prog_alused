letter = float(input("Sisestage kirja suurus: "))
title = input("Sisestage kirja teema pealkiri: ")
attachment = input("Kas kirjale on lisatud fail?: ")

if title != "" or (letter > 1.0 and attachment == "jah"):
    print("Kiri ei ole spämm")
else:
    print("Kiri on spämm")