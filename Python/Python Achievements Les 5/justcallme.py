import sys
import time

print("Name: " + sys.argv[1])
print("Nummer: " + sys.argv[2])
name = sys.argv[1]
try:
    int(nummer) = sys.argv[2]
    if not len(nummer) == 10:
    print()
    print("Telefoon nummer is niet goed")
    exit()
except ValueError:
    print("Dat is geen echt telefoon nummer.")
    exit()

print()
print()
print("Calling", name + "...")
time.sleep(3)

print(name + ": Hallo?")
time.sleep(1)
print("#: He ik ben het.")
time.sleep(1)
print(name + ": Oh hé, ehm..")
time.sleep(0.5)
print(name + ": Kan ik je later terug bellen?")
time.sleep(1)
print("#: Oke, is goed.")
time.sleep(0.3)
print("#: Doei!")
time.sleep(1)
print(name + ": Doei!")
time.sleep(1)
print("click...")