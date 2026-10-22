# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".

hlmesto = input("Jaké je hlavní město Česka?\n")
while hlmesto != "Praha":
    hlmesto = input("Jaké je hlavní město? ")
print("Správně")
