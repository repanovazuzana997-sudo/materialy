# Cvičení 4 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Vypiš prvních deset násobků čísla 3 (3, 6, 9, ... 30).

# for protože dopředu víme počet
pocet = 0
for cislo in range (3, 31, 3):
    pocet = pocet + 1
    if pocet <11:
        print(cislo)