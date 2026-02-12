# Passwort Liste
password_set = []


# Einfügen
password_input = input("1. Passwort eingeben: ")


while True:
    # Check password
    if len(password_input) >= 8:
        continue
    else: print("Es ist zu kurz")
    password_input = input("1. Passwort eingeben: ")
    # Put in List
    password_set.append(password_input)
    print(password_set)
    # Eingeben
    passwort_right = input("Passwort: ")

    if passwort_right == password_set[0]:
        print("corecct")
    else: 
        while passwort_right != password_set[0]:
            print("Not correct")
            passwort_right = input("Passwort: ")
        else: print("Correct")