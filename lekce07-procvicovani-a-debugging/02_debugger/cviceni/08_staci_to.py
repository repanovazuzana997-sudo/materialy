# Cvičení 8 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program se zeptá, kolik máš korun a kolik stojí vstupenka,
# a řekne, jestli ti to stačí.
#
# Zadej 1000 a 250.

castka = int(input("Kolik korun máš? "))
cena = int(input("Kolik stojí vstupenka? "))

if castka > cena:
    print("Stačí.")
else:
    print("Nestačí.")
