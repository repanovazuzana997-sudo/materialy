# Cvičení 3 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci soucet_do(n), která vrátí součet čísel od 1 do n.
#    soucet_do(5) vrátí 15.

def soucet_do(n):
    soucet = 0
    for cislo in range(1,6):
         soucet = soucet + cislo
    return(soucet)

print("součet do 5 je:",soucet_do(5))