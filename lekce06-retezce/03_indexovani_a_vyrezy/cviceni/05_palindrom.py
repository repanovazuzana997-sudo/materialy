# Cvičení 5 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na slovo a vypiš, jestli se čte stejně zepředu i pozpátku.
#    Na velikosti písmen ať nezáleží, takže "Oko" projde taky.

slovo = input("Zadej slovo:").strip().lower()
slovo_pozadu = slovo[::-1]

if slovo == slovo_pozadu:
    print(f"Slovo \"{slovo}\" je palindrom.")
else:
    print(f"Slovo \"{slovo}\" není palindrom.")