dag = int(input("Cijfer van dag: "))

week = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

if week[dag] == week[0] or week[dag] == week[1] or week[dag] == week[2] or week[dag] ==week[3] or week[dag] == week[4]:
    print("Je moet naar school vandaag")
elif week[dag] == week[6]:
    print("Je moet naar de zondags school")
else:
    print("Je hoeft niet naar school vandaag")
