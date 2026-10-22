# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))


soucet = 0
kolik = 0
cislo = int(input("Zadej číslo. Když zadáš 0, tak je konec."))

while cislo != 0:
    soucet = soucet + cislo
    kolik = kolik +1
    cislo = int(input("Zadej číslo znovu."))

if cislo == 0:
    print("Toto je konec.")
    print("Součet je:", soucet)
    print("Počet je:", kolik)
    print("Průměr je:", round(soucet/kolik, 1))


