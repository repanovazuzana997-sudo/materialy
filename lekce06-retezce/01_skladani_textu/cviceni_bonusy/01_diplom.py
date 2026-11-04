# Bonus 1 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš diplom v rámečku z hvězdiček:
#
#    **************************
#    * Anna Nováková          *
#    * Python pro začátečnice *
#    **************************
#
#    Rámeček musí být přesně tak široký, jak je potřeba. Když jméno
#    nebo název kurzu vyměníš za delší, musí se přizpůsobit sám –
#    šířku tedy spočítej, nepiš ji natvrdo.

jmeno = "Anna Nováková"
kurz = "Python pro začátečnice a pro pokročilé"

delka_jmena = len(str(jmeno))
delka_kurzu = len(str(kurz))

if delka_jmena > delka_kurzu:
    delka = delka_jmena + 2
else:
    delka = delka_kurzu + 2
    
print(f"""{delka * "*"}
*{jmeno}*
*{kurz}*
{delka * "*"}""")

