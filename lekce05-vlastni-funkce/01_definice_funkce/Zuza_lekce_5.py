# def vypis_cisla_do_x_hodnoty(max_hodnota, jmeno_volani, ukaz_caru):
#     for aktualni_cislo in range(1, max_hodnota):
#         print(jmeno_volani, aktualni_cislo)
#     if ukaz_caru:
#         print("-"*30)
# vypis_cisla_do_x_hodnoty(6, "Volani A", True)
# vypis_cisla_do_x_hodnoty(11, "Volani B", True)
# vypis_cisla_do_x_hodnoty(16, "Volani C", False)


# def vypis_cisla_do_x_hodnoty(max_hodnota, jmeno_volani, ukaz_caru = True):
#     for aktualni_cislo in range(1, max_hodnota):
#         print(jmeno_volani, aktualni_cislo)
#     if ukaz_caru:
#         print("-"*30)
# vypis_cisla_do_x_hodnoty(6, "Volani A")
# vypis_cisla_do_x_hodnoty(11, "Volani B")
# vypis_cisla_do_x_hodnoty(16, "Volani C", False)

# def cena_mhd(vek):
#     print("počítám cenu lístku pro věk", vek)

#     if vek < 6:
#         return 0
#     elif vek < 18:
#         return 39
#     elif vek < 65:
#         return 50

# zustatek_uctu = 100
# cena_jizdenky = cena_mhd(80)
# print("Výsledná cena jízdenky je", cena_jizdenky)
# zustatek_uctu = zustatek_uctu - cena_jizdenky
# print("Zůstatek na účtu je:", zustatek_uctu)

# def vypis_dph(cena):
#     print(cena * 1.21)

# def spocitej_dph(cena):
#     return cena * 1.21

# vysledek_vypisu = vypis_dph(100)
# vysledek_vypoctu = spocitej_dph(100)
# print("z vypis_dph:", vysledek_vypisu)
# print("ze spocitej_dph:", vysledek_vypoctu)

def pozdrav_a_vrat(jmeno):
    print("Zdravím,", jmeno)
    return "hotovo"
    print("Tenhle řádek se nikdy nevypíše.")

print(pozdrav_a_vrat("Anno"))