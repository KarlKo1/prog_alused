nimi = input("Sisestage nimi: ")
if (nimi[-2:] == "ne"):
    print("abielus")
elif(nimi[-2:] == "te"):
    print("vallaline")
elif(nimi[-1:] == "e" and (nimi[-2:] != "ne" or nimi[-2:] != "te")):
    print("määramata")