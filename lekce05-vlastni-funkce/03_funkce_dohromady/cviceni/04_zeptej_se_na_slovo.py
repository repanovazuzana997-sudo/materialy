# Cvičení 4 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zeptej_se_na_slovo(), která se ptá tak dlouho,
#    dokud uživatel nezadá slovo aspoň o třech písmenech, a slovo vrátí.
#    Zavolej ji a výsledek pošli do funkce nadpis, která je připravená níž.

def nadpis(text):
    print(text)
    print("-" * len(text))

def zeptej_se_na_slovo():
    slovo = input("Zadej slovo:")
    while len(slovo) <= 3:
        print("moc krátké")
        slovo = input("Zadej slovo:")
    return slovo

nadpis(zeptej_se_na_slovo())
