# Cvičení 4 – Debugger
# Spusť soubor (Run). Výsledek je špatný. Najdi chybu debuggerem.

# Program spočítá cenu vstupenky podle věku:
#   do 6 let zdarma, do 18 let poloviční, do 65 let plná cena,
#   od 65 let sleva 30 %.
#
# Zkontroluj podle pravidel výš, jestli vypsaná cena sedí.

vek = 3
plna_cena = 250

if vek < 6:
    cena = 0
elif vek < 18:
    cena = plna_cena / 2
elif vek < 65:
    cena = plna_cena
else:
    cena = plna_cena * 0.7

print(f"Vstupenka pro {vek} let: {cena:.0f} Kč")
