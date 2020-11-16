import random
def woorden(woord):
    radomwoord = ''.join(random.sample(woord, len(woord)))
    return radomwoord

woord1 = woorden("Hallo")
woord2 = woorden("Goedendag")
woord3 = woorden("Welkom")
print(woord1, woord2, woord3)