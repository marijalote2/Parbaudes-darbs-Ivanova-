import sys

with open("sistema.log", encoding="utf-8") as f:
for rinda in f:
dalas = rinda.split()
if len(dalas) > 2 and dalas[2] == meklejamais:
skaits += 1
atlasitās_rindas.append(rinda)

print("Atrasts:", skaits)

iznākuma_fails = f"{meklejamais.lower()}_rindas.log"
with open(iznākuma_fails, "w", encoding="utf-8") as f:
f.writelines(atlasitās_rindas)
