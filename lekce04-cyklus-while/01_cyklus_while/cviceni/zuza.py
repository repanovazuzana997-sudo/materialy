# pocet = 0
# for cislo in range(1, 21):
# if cislo % 2 == 0:
# pocet = pocet + 1
# print(cislo, pocet)

# slovo = "karambol"
# samohlasky = 0
# hlasky = 0
# for pismeno in slovo:
#     if pismeno in "aeiou":
#         samohlasky = samohlasky + 1
#         hlasky = len(slovo )- samohlasky
# print("samohlasek je:", samohlasky,",", "hlásek je:", hlasky)

# slovo = "Ahoj"
# for pisemeno in slovo:
#     print(pisemeno)

# jmeno = input(str("Napiš svoje jméno:\n"))
# for pismeno in jmeno:
#     print(pismeno, "?")

# for kolo in range(1, 5):
#     print("kolo", kolo)
#     for pokus in range (1, 4):
#         print("pokus", pokus)

# for tyden in range (1, 4):
#         for day in range(1, 8):
#             print("den",day, end=" ")
#         print()

# soucet = 0
# for cislo in range(0, 5):
#     soucet = soucet + 1
# print(soucet)

# pocet = 0
# for cislo in range(10):
#     pocet = pocet + 1
# print("cyklus proběhl", pocet, "krát")

# soucin = 1
# for cislo in range(1, 5)
#     soucin = soucin * cislo
# print(soucin)

delka = 1000
strihnuti = 0
while delka > 1:
    delka = delka / 2
    strihnuti = strihnuti + 1
    print("střihnutí", strihnuti, "- délka:", delka, "cm")
print("počet střihnutí:", strihnuti)