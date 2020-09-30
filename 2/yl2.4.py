from random import randint
seat = ""
choice = input("Kas soovite istekohta ise valida (\"ise\") või loosida (\"loos\")?")
if choice == "ise":
    win_or_else = input("Kas soovite istud akna ääres (\"aken\") või mitte (\"muu\")? ")

    if win_or_else == "aken":
        print ("Valisite ise. Aknakoht")
    else:
        seat == "muu"
        print("Valisite ise. Vahekäigukoht")

if choice == "loos":
    seat_chance = randint(1, 3)
    if seat_chance == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print ("Istekoht loositi. Vahekäigukoht")