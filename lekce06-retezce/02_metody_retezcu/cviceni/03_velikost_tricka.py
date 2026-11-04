# Cvičení 3 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na velikost trička, dokud uživatelka nenapíše S, M nebo L.
#    Na nic jiného se nespokoj a zeptej se znovu. Velikost písmen
#    ani mezery navíc ať nevadí – "s" i "  M  " mají projít.
#    Nakonec vypiš objednanou velikost velkým písmenem.
#
#    Cyklus while True a break znáš z lekce 4.

while True:
    velikost = input("Zadej velikost trička (S, M, L)").upper().strip()
    if velikost  == "S" or velikost == "M" or velikost == "L":
        break
    print("Vyber S, M, nebo L.") 
 print (f"Vybraná velikost trička je {velikost}.")