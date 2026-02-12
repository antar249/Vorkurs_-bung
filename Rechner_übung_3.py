operator = 1
ergebnis = 0
while operator != 0:
    print (f"""
Einfache Taschenrechner: <3lich Willkommen
Ausgabe 1: Addidition
Ausgabe 2: Subtraktion
Ausgabe 3: Multiplikation
Ausgabe 4: Division
Ausgabe 5: Modulo
Ausgabe 0: Ende """)
    operator = int(input("Was möchten sie tun: "))
    if operator != 0:
        zahl1 = float(input("1. Zahl: "))
        zahl2 = float(input("2. Zahl: "))
        if operator == 1:
            ergebnis = zahl1 + zahl2
        elif operator == 2:
            ergebnis = zahl1 - zahl2
        elif operator == 3:
            ergebnis = zahl1 * zahl2
        elif operator == 4:
            if operator == 0:
                print("Division / 0 Geht nicht!")
                continue
            ergebnis = zahl1 / zahl2
        elif operator == 5:
            ergebnis = zahl1 % zahl2
        else: print("Unvalid")
        
        print(f"{ergebnis}")
print ("Auf Wiedersehen!")
