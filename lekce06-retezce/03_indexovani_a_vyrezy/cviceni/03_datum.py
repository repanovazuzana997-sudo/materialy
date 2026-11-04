# Cvičení 3 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# V proměnné datum je text ve tvaru rok-měsíc-den. Vypiš ho česky,
#    tedy ve tvaru:  17. 10. 2026

datum = "2026-10-17"

den = datum[-2:]
mesic = datum[-5:-4]
rok = datum[0:4]

print(den + "." + mesic + "." + rok)
print(f"{den}.{mesic}.{rok}")