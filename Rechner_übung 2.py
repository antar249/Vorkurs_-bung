zahl1 = float(input("Erste Zahl: ")) 
operator= input("Operator (+, -, *, /): ")
while operator not in ["+", "-", "*", "/"]:
    print("Ungültiger Operator, bitte (+, -, *, /) eingeben")
    operator = input("Operator (+, -, *, /): ")
else: print("Ungültige Operator, bitte (+, -, *, /) eingeben")
zahl2 = float(input("Zweite Zahl: "))

# Ergebnis 
if operator == "+":
        ergebnis= zahl1 + zahl2
elif operator == "-":
        ergebnis= zahl1 - zahl2
elif operator == "*":
        ergebnis= zahl1 * zahl2
elif operator == "/":
        ergebnis= zahl1 / zahl2

while operator not in ["+", "-", "*", "/"]:
    print("Ungültiger Operator, bitte (+, -, *, /) eingeben")
    operator = input("Operator (+, -, *, /): ")
else: print("Ungültige Operator, bitte (+, -, *, /) eingeben")

print(f"{zahl1} {operator} {zahl2} = {ergebnis}")
