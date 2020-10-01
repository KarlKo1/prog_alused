ringide_arv = int(input("Sisestage ringide arv "))
ringi_number = 1
porgandite_arv = 0
while(ringi_number <= ringide_arv):
    print (str(ringi_number) +". ring")
    if (ringi_number % 2 == 0):
        print("said " + str(ringi_number) + " porgandeid")
        porgandite_arv = ringi_number + porgandite_arv
        print("Hetkel on kokku " + str(porgandite_arv)+ " porgandeid")
    ringi_number += 1
print("Porgandite koguarv on " + str(porgandite_arv))