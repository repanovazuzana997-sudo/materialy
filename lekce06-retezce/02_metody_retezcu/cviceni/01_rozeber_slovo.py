# Cvičení 1 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na slovo a vypiš o něm čtyři řádky:
#    - slovo velkými písmeny,
#    - slovo malými písmeny,
#    - kolik má znaků,
#    - kolikrát je v něm písmeno "a".
#
#    Délku umí len() z lekce 3, zbytek jsou metody z výkladu.

slovo = input("Zadej slovo:")
acek = slovo.count("a")

print(f"Velkými: {slovo.upper()}")
print(f"Malými: {slovo.lower()}")
print(f"Délka slova: {len(slovo)}")
print(f"Počet \"a\": {acek}")