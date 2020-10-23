print("Wat wil je eten vanavond?")
print()
while True:
    print("1. Patat")
    print("2. Nasi")
    print("3. Aardapples")
    print("4. Pizza")
    print("5. Lasagna")
    choise = input()
    if choise == "1":
        print()
        print("Goed we eten patat.")
        break
    elif choise == "2":
        print()
        print("Goed dan eten we nasi.")
        break
    elif choise == "3":
        print()
        print("Gatverdame aardapplen, vooruit wat jij wil.")
        break
    elif choise == "4":
        print()
        print("Lekker, komt er aan.")
        break
    elif choise == "5":
        print()
        print("Oke lekker")
        break
    else:
        print()
        print("Als u er nog even over na wil denken dan kan dat.")
        
while True:
    print()
    print("Met de auto of  met de fiets?")
    choise = input()
    
    if choise.lower() == "auto":
        print("oke we gaan met de auto")
        break
    elif choise.lower() == "fiets":
        print("Dan gaan we met de fiets.")
        break
    else:
        print("Sorry waat zei je?")
while True:
    print()
    print("Wekker aan of wekker uit?")
    choise = input()
    
    if choise.lower() == "aan":
        print("Je doet je wekker aan.")
        break
    elif choise.lower() == "uit":
        print("Je laat je wekker uit.")
        break
    else:
        print("Je moet echt kiezen.")

while True:
    print()
    print("Blijven of weg gaan?")
    choise = input()
    
    if choise.lower() == "blijven":
        print("Leuk.")
        break
    elif choise.lower() == "weg gaan":
        print("jammer doei")
        break
    else:
        print("Wat zeg je?")
while True:
    print()
    print("Lopen of fietsen?")
    choise = input()
    
    if choise.lower() == "lopen":
        print("Je gaat lopen.")
        break
    elif choise.lower() == "fietsen":
        print("Je gaat fietsen.")
        break
    else:
        print("Wat zeg je?"
        )