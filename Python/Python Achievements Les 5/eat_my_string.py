import time
def eetertje(eeter, lengtestring):
    eeter = eeter[0:len(eeter)-1]
    print(eeter)
    time.sleep(0.5)
    lengte = len(eeter)
    if not eeter == "":
        eetertje(eeter, lengte)
    else:
        return eeter


woord = input("Geef me je string!! ")
eetertje(woord, len(woord))