# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.



kolikrat = 0
while True:
    heslo = input("Zadej heslo: ")
    kolikrat = kolikrat + 1
    if heslo == "pyladies":
        kolikrat = kolikrat + 1
        print("Vítej!")
        break
    if kolikrat ==3:
        print("Zablokováno!")
        break
    print("Špatně, zkus to znovu.")