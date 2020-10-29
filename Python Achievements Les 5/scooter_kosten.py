invoer = ""
def kosten(km):
    verzekering = 23
    benzine = 1.54
    liter_per_km = 0.2
    maandkosten = 0
    maandkosten = (benzine * liter_per_km * km) + verzekering
    return maandkosten
while not isinstance(invoer, float):
    try:
        invoer = input("Hoe veel kliometer heb je gereden deze maand? ")
        invoer = float(invoer)
        kosten = kosten(invoer)
        print("Je moet " + str(kosten) + " euro betalen deze maand.")
    except ValueError:
        print(invoer, "is geen goed getal")