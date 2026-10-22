# Cvičení 3 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Pak vypiš "Odemčeno!".

# while protože nevím, jak dlouho bude uživatel zadávat

pin = input("Zadej PIN: \n")
while pin !="1234":
    print("Špatný pin.")
    pin = input("Zadej PIN: \n")
print("Odemčeno")
    

    