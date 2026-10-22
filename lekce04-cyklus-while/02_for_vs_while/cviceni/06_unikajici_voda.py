# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.

# while protože nevíme, jak dlouho bude trvat únik vody

litry = 45
minuta = 1

while litry > 0:
    litry = litry - 3
    minuta = minuta + 1
    print("Po minutě", minuta,"zůstává", litry, "litrů.")
print("Nádrž je prázdná po minutě", minuta,".")
