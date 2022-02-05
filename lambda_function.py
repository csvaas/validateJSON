import json


def depth(x):
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0


error = 0

# JSON einlesen
# f = open("deep.json")       #Fehler nicht zweidimensional
# f = open("test.json")       #Fehler nicht valide
f = open("testdata.json")  # Korrekt

# Prüfen, ob JSON korrekt ist
try:
    jfile = json.load(f)
except ValueError as e:
    error = 1
if error == 0:
    # Prüfen, ob JSON eine tiefe von 2 hat
    if depth(jfile) != 2:
        error = 2

# Ergebnis ausgeben
if error == 0:
    print("JSON ist korrekt")
elif error == 1:
    print("JSON ist nicht valide")
elif error == 2:
    print("JSON darf nur zweidimensional sein")
