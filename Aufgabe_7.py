# Ticket Preise

Kinder = 8
Jugendliche = 12 
Erwachsene = 16
Senioren = 10

print(f"""
Kinder (unter 12):      CHF      8.00
Jugendliche (12–17):    CHF     12.00
Erwachsene (18–64):     CHF     16.00
Senioren (ab 65):       CHF     10.00

Am Dienstag gibt es 20% Rabatt für alle. 
      
""")
Alter = int(input("Bitte geben Sie Ihren alter an: "))

# Frage nach Wochentag mit Button
Wochentag = input("Bitte geben Sie den Wochentag an: ").title()
if Wochentag == "Dienstag":
    Kinder_R = Kinder * 0.2
    Jugendliche_R = Jugendliche * 0.2
    Erwachsene_R = Erwachsene * 0.2
    Senioren_R = Senioren * 0.2


# Kindeer
if Alter <= 12:
    if Wochentag == "Dienstag":
        print(f"Dein Preis: {Kinder - Kinder_R} CHF")
    else:
        print(f"Dein Preis: {Kinder} CHF")

# Jugendliche
if Alter > 12 and Alter <= 17:
    if Wochentag == "Dienstag":
        print(f"Dein Preis {Jugendliche - Jugendliche_R}") 
    else:   
        print(f"Dein Preis: {Jugendliche} CHF")
    
# Erwachsene
if Alter >= 18 and Alter <= 64:
    if Wochentag == "Dienstag": 
        print(f"Dein Preis: {Erwachsene - Erwachsene_R} CHF")
    else:   
        print(f"Dein Preis: {Erwachsene} CHF")

# Senioren
if Alter >= 65:
    if Wochentag == "Dienstag":
        print(f"Dein Preis: {Senioren - Senioren_R} CHF")
    else:   
        print(f"Dein Preis: {Senioren} CHF")