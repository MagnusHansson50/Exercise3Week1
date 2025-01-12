x = input("Ange ett heltal: ")
print(int(x))
y = input("Ange ännu ett heltal: ")
print(f"Summan av talen är: {int(x) + int(y)}")

def attBetala(rabattSats, pris):
    rabattSumma = pris * (rabattSats / 100)
    slutSumma = pris - rabattSumma
    return slutSumma

jacka = 2000
rabatt = input("Vilken rabattsats är det på jackan? ")

print("Jackan kostar: " + str(attBetala(int(rabatt), jacka)) + " kronor med " + str(rabatt) + " % rabatt.")

jacka = 2000
rabatt = input("Vilken rabattsats är det på jackan? ")
rabattSumma = jacka * (int(rabatt) / 100)
slutSumma = jacka - rabattSumma

print("Jackan kostar: " + str(slutSumma) + " kronor med " + str(rabatt) + " % rabatt.")