with open("servisi.csv", mode="w", encoding="utf-8-sig", newline="") as f:
rakstitajs = csv.writer(f)
rakstitajs.writerow(["Serviss", "Kļūdas"])
for serviss, klūdas in skaits.items():
rakstitajs.writerow([serviss, klūdas])

print("Dati ierakstīti")
