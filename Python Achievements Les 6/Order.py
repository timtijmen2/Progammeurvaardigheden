import time
stuff = ['c',5645,9393.77,"hello", True, False, "Good morning",88, -90, 777.777, 90,665.33,"F"]
strings = []
integers = []
floats = []
booleans = []
while True:
    if stuff == []:
        break
    if type(stuff[0]) == str:
        strings.append(stuff[0])
        stuff.remove(stuff[0])
    elif type(stuff[0]) == int:
        integers.append(stuff[0])
        stuff.remove(stuff[0])
    elif type(stuff[0]) == float:
        floats.append(stuff[0])
        stuff.remove(stuff[0])
    elif type(stuff[0]) == bool:
        booleans.append(stuff[0])
        stuff.remove(stuff[0])
    print("stuff:", stuff)
    print("strings:", strings)
    print("ints", integers)
    print("floats", floats)
    print("bools", booleans)
    time.sleep(0.3)
