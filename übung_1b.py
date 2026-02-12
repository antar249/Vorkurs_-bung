Vorname = input("Hallo, ")

Geburtsjahr = 2026 - int(input("In welchem Jahr bist du geboren? "))

Körpergrösse = input ("Wie gross bist du in cm? ")

Führerschein = input ("Hast du einen Führerschein? (ja/nein) ")




if Führerschein == "ja" and Geburtsjahr >=18 :
    Führerschein = True
    true=("Führerschein: Ja, du darfst Auto fahren.")
else:   
    false = ("Führerschein: Nein, du darfst kein Auto fahren.")


print (Vorname)

print (Geburtsjahr)

print (Körpergrösse)

if Führerschein == True:
    print (true)
else:
    print (false)   


