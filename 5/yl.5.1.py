"""
aasta = input("Sisesta aasta 2011-2019: ")
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
if aasta == "2011":
    print(vastuvõetud[0])
elif aasta == "2012":
    print(vastuvõetud[1])
elif aasta == "2013":
    print(vastuvõetud[2])
elif aasta == "2014":
    print(vastuvõetud[3])
elif aasta == "2015":
    print(vastuvõetud[4])
elif aasta == "2016":
    print(vastuvõetud[5])
elif aasta == "2017":
    print(vastuvõetud[6])
elif aasta == "2018":
    print(vastuvõetud[7])
elif aasta == "2019":
    print(vastuvõetud[8])
"""


fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
     aasta = input(("Sisesta aasta: "))
     print(str(vastuvõetud))
     break
fail.close()

