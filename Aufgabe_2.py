# Währung
CHF = 1.00 
EUR = 0.95

# Fragen ob EUR/CHF

ask = input("EUR / CHF: ")
if ask == "EUR":

# In CHF Umrechnen
    CHF_umrechnen = (float(input("Betrag in Euro: "))) * CHF 

elif ask == "CHF":
# In Euro Umrechnen
    EUR_umrechnen = (float(input("Betrag in CHF: "))) * EUR

else:
    print("PLS ENTER EUR OR CHF")

if ask == "EUR":

    print (f"""
Betrag in CHF: {CHF_umrechnen:.2f}
       """)
    
elif ask == "CHF":

    print (f"""
Betrag in EUR: {EUR_umrechnen:.2f}

        """)