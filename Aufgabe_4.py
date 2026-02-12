noten = (float(input("Note 1.0 - 6.0: ")))

if noten < 1.0 or noten > 6.0: 
    print("Ungültige Note. Bitte Note zwischen 1.0 und 6.0 eingeben.")


elif noten == 6.0: 
    print("Bravo")

elif noten >= 5.0:
    print("Gut")

elif noten >= 4.0:
    print("Genügend")

else:
    print("Ungenügend") 

