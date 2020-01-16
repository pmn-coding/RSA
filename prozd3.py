import itertools as it

def isprim(a):
    x = 2
    if a == 0 or a == 1:
        return False
    elif a == 2:
        return True
    else:
        while x < a:
            if a % x == 0:
                return False
            x += 1
    return True
 
y = int(input("Untergrenze: "))
eingabe = int(input("Obergrenze: "))
file = open("prim.txt", "w")

liste = []
while y <= eingabe:
    if isprim(y):
        liste.append(str(y))
        y += 1
    else:
        y += 1
r = "\n".join(liste)
file.write(r)
file.close()
