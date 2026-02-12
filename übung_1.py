# Benutzer Informieren

print ("Hallo Benutzer! Wir erstellen für dich eine Zusammenfassung über dein Gesamtkosten.")

# Benutzereingaben abfragen

name = input("Gib deinen Namen ein: ")

# Preise definieren
Erwachsene = 2000

Kinder = 250

# Anzahl der Kinder abfragen
kinderzahl = input("Wie viele Kinder hast du? ")
kinderzahl = int(kinderzahl) * Kinder

# Gesamtkosten berechnen

print ("In moment kosten deine Gesamtkosten für deine Familie " + str(Erwachsene + kinderzahl) + "CHF")