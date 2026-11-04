# Cvičení 2 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na slovo a vypiš jeho poslední tři znaky. Když je slovo
#    kratší než tři znaky, vypiš místo toho, že je moc krátké.
#
#    Délku změříš len() z lekce 3, rozhodneš se podmínkou z lekce 2.

slovo = input("Zadej slovo:\n")

if len(slovo) < 3:
    print("Slovo je moc krátké.")
print(slovo[-3:])