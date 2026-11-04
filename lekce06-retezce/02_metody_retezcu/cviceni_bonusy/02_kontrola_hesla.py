# Bonus 2 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na heslo a zkontroluj tři věci:
#    je aspoň osm znaků dlouhé, je v něm aspoň jedna číslice
#    a je v něm aspoň jedno velké písmeno.
#
#    Ke každé podmínce vypiš, jestli prošla. Na konec vypiš, jestli
#    je heslo přijaté – to je, jen když prošly všechny tři.
#
#    Na číslici se zeptáš průchodem přes znaky: cyklus for z lekce 3
#    a isdigit() na každý znak.
#    Na velké písmeno stačí porovnat heslo se sebou samým po lower().
#    Jde to ale i cyklem jako u číslice – každého znaku se tam zeptáš
#    metodou isupper().

heslo = input("Zadej heslo:")

dost_dlouhe = len(heslo) >= 8

ma_velke = heslo != heslo.lower()

for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break

print(f"Aspoň osm znaků:  {dost_dlouhe}")
print(f"Obsahuje číslici: {ma_cislici}")
print(f"Velké písmeno:    {ma_velke}")

if dost_dlouhe and ma_cislici and ma_velke:
    print("Heslo je přijato.")
else:
    print("Heslo nevyhovuje.")