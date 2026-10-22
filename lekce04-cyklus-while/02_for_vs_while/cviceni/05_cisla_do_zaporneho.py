# Cvičení 5 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.

# while protože nevím, jak dlouho bude uživatel zadávat

cislo = int(input("Zadej číslo:"))
pocet = 1

while cislo > 0:
    cislo = int(input("Zadej číslo:"))
    pocet = pocet + 1
    if cislo < 0:
         break
print("Uživatel stihnul zadat", pocet, "čísel.")