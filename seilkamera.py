import math

x = input("Gebe die Breite des Stadions ein")
y = input("Gebe die Länge des Stadions ein")

x1 = input("Gebe die jetzige x Koordinate der Kamera an")
y1 = input("Gebe die jetzige y Koordinate der Kamera an")

x2 = input("Gebe die zukünftige x Koordinate der Kamera an")
y2 = input("Gebe die zukünftige y Koordinate der Kamera an")

p = input("Gib eine Prozentanzahl an")

x = int(x)
y = int(y)
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
p = int(p)

s11 = math.sqrt((x-x1)**2 + (y-y1)**2)
s12 = math.sqrt(x1**2 + (y-y1)**2)
s13 = math.sqrt(x1**2 + y1**2)
s14 = math.sqrt((x-x1)**2 + y1**2)

s21 = math.sqrt((x-x2)**2 + (y-y2)**2)
s22 = math.sqrt(x2**2 + (y-y2)**2)
s23 = math.sqrt(x2**2 + y2**2)
s24 = math.sqrt((x-x2)**2 + y2**2)

vs1 = (s21 - s11)*p/100
vs2 = (s22 - s12)*p/100
vs3 = (s23 - s13)*p/100
vs4 = (s24 - s14)*p/100

print("Die Länge von Seil 1 ist " + str(s11))
print("Die Länge von Seil 2 ist " + str(s12))
print("Die Länge von Seil 3 ist " + str(s13))
print("Die Länge von Seil 4 ist " + str(s14))

print("Die Länge von Seil 1 soll sein " + str(s21))
print("Die Länge von Seil 2 soll sein " + str(s22))
print("Die Länge von Seil 3 soll sein " + str(s23))
print("Die Länge von Seil 4 soll sein " + str(s24))

print("Die Geschwindigkeit der Kamera 1 soll " + str(vs1) + " m/s sein")
print("Die Geschwindigkeit der Kamera 2 soll " + str(vs2) + " m/s sein")
print("Die Geschwindigkeit der Kamera 3 soll " + str(vs3) + " m/s sein")
print("Die Geschwindigkeit der Kamera 4 soll " + str(vs4) + " m/s sein")
