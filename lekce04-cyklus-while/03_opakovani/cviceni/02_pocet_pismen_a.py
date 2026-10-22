# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.

slovo = str(input("Zadej slovo:"))
samohlaska = 0
for pismeno in slovo:
    if pismeno in "a":
        samohlaska = samohlaska +1
print("Počet písmen a je", samohlaska)
