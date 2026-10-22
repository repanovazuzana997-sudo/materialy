# Cvičení 5 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange


from random import randrange
hadanecislo = randrange(1,21)
pocet = 0
while True:
    odpoved = int(input("Zadej číslo od 1-20:"))
    pocet = pocet + 1

    if odpoved == hadanecislo:
        print("Trefa!")
        break

    if pocet == 5:
        print("Končíš, pokusů bylo 5.")
        break

    if odpoved > hadanecislo:
        print("Moc velké!")

    else:
        print("Moc malé!")