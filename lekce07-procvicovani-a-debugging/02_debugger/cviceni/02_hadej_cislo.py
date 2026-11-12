# Cvičení 2 – Debugger
# Spusť soubor (Run) a zahraj si pár her. Chyby jsou dvě a ta druhá
# se ukáže jen někdy. Najdi je debuggerem a oprav.
# Druhou nejsnáz uvidíš, až opravíš tu první: pak se schválně trefuj
# až pátým tipem – z nápověd už budeš vědět, kde číslo je.

# Hádání čísla znáš ze čtvrté lekce. Počítač si vylosuje číslo
# od 1 do 20 a ty hádáš. Po každém tipu napíše "Moc velké." nebo
# "Moc malé.". Když se trefíš, napíše "Trefa!". Když se netrefíš
# ani pátým tipem, prozradí číslo.

from random import randrange


def vylosuj_cislo():
    return randrange(1, 21)


def zeptej_se_na_tip():
    return int(input("Hádej číslo od 1 do 20: "))


def je_trefa(tip, hledane):
    return tip == hledane


def napoveda(tip, hledane):
    if tip > hledane:
        return "Moc velké."
    else:
        return "Moc malé."


pokusy = 0
hledane_cislo = vylosuj_cislo()

while True:
    tip = zeptej_se_na_tip()
    pokusy = pokusy + 1

   
    if je_trefa(tip, hledane_cislo):
        print("Trefa!")
        break
    elif pokusy < 5:
        print(napoveda(tip, hledane_cislo))
    elif pokusy == 5:
        print(f"Došly ti pokusy. Hledané číslo bylo {hledane_cislo}.")
        break
    


