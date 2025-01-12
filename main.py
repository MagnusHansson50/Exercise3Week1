x = input("Ange ett heltal: ")
print(int(x))
y = input("Ange ännu ett heltal: ")
print(f"Summan av talen är: {int(x) + int(y)}")

def attbetala(rabattsats, pris):
    rabattsumma = pris * (rabattsats / 100)
    slutsumma = pris - rabattsumma
    return slutsumma

jacka = 2000
rabatt = input("Vilken rabattsats är det på jackan? ")

print("Jackan kostar: " + str(attbetala(int(rabatt), jacka)) + " kronor med " + str(rabatt) + " % rabatt.")

jacka = 2000
rabatt = input("Vilken rabattsats är det på jackan? ")
rabattSumma = jacka * (int(rabatt) / 100)
slutSumma = jacka - rabattSumma

print("Jackan kostar: " + str(slutSumma) + " kronor med " + str(rabatt) + " % rabatt.")