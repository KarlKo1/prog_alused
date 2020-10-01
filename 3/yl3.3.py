
täringute_arv = int(input("Sisesta täringute arv: "))
i = 0
from random import randint
while i < täringute_arv:
    print("Täringu viskel saadi " + str(randint(1, 6)))
    i += 1