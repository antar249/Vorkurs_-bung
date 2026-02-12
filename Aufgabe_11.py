# Multipliation von 1 - 10 

zahl1 = int(input("To multi pick a NR between 1-10: "))

while zahl1 not in range(1,11):
    print("Invalid, pls chose the NR between 1-10")
    zahl1 = int(input("To multi pick a NR between 1-10: "))

for Multi in range(1,11):
    Answer= zahl1 * Multi
    print(
f"""
{zahl1} x {Multi} = {Answer}
""")
