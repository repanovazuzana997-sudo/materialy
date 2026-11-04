# Cvičení 1 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na podstatné jméno, sloveso a přídavné jméno. Všechna tři
#    slova pak f-stringem dosaď do jedné věty. Čím nesmyslnější věta
#    vyjde, tím líp. Třeba:
#
#    Dneska jsem viděla fialový rohlík, jak programuje.

pods_jm = str(input("Napiš mi podstatné jméno:\n"))
sloveso = str(input("Napiš mi sloveso:\n"))
pridavne_jm = str(input("Napiš mi přídavné jméno:\n"))

print(f"Včera jsem viděla jak {pridavne_jm} {pods_jm} {sloveso}.")