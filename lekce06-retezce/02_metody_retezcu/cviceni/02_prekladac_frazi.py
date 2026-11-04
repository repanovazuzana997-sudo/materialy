# Cvičení 2 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Věta z firemní prezentace je plná frází. Vyměň je za srozumitelná
#    slova a výsledek vypiš:
#
#        proaktivně     -> včas
#        implementovat  -> zařídit
#        synergie       -> spolupráci
#
#    Výměny dělej po krocích, ať se řádky dají přečíst.

veta = "Musíme proaktivně implementovat synergie napříč týmy."

opravena = veta.replace("proaktivně", "včas")
opravena = opravena.replace("implementovat", "zařídit")
opravena = opravena.replace("synergie", "spolupráci")

print(opravena)