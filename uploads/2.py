'''
def hinne(punktid):
    if punktid >= 90:
        return "A"
    if punktid >= 80:
        return "B"
    if punktid >= 70:
        return "C"
    if punktid >= 60:
        return "D"
    if punktid >= 50:
        return "E"
    else: 
        return "F"

print(hinne(78))

import math 

def koogi_hind(nimi, mõõt):
    if mõõt <= 0:
        return -1
    
    nimi = nimi.lower()
    ringi_pindala = math.pi * (mõõt ** 2)
    ruudu_pindala = mõõt ** 2
    
    if nimi == "napoleoni kook":
        return round(0.08 * ruudu_pindala, 2)
    elif nimi == "šokolaadikook":
        return round(0.05 * ringi_pindala, 2)
    elif nimi == "ploomikook":
        return round(0.04 * ringi_pindala, 2)
    else:
        return -1

nimi = input("Sisesta koogi nimi: ")
mõõt = float(input("Sisesta koogi mõõt: "))
hind = koogi_hind(nimi, mõõt)

if hind != -1:
    print(f"Selle koogi hind {hind} eurot. ")
else:
    print("Sellist kooki pagarikoda ei valmista.")



c = 299792.458

def summa(u, v):
    w = (u + v) / (1 + (u * v) / c ** 2)
    return w
    
def summa2(w, x):
    z = (w + x) / (1 + (w * x) / c ** 2)
    return z
    
def summa3(z, y):
    q = (z + y) / (1 + (z * y) / c ** 2)
    return q


u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))

w = summa(u, v)
z = summa(w, x)
kogu_summa = summa3(z, y)

print(f"Kiiruste summa on {kogu_summa} km/s")
'''


def mis_kuu(kuu_number):
    if kuu_number == 1:
        return "jaanuar"
    elif kuu_number == 2:
        return "veebruar"
    elif kuu_number == 3:
        return "märts"
    elif kuu_number == 4:
        return "aprill"
    elif kuu_number == 5:
        return "mai"
    elif kuu_number == 6:
        return "juuni"
    elif kuu_number == 7:
        return "juuli"
    elif kuu_number == 8:
        return "august"
    elif kuu_number == 9:
        return "september"
    elif kuu_number == 10:
        return "oktoober"
    elif kuu_number == 11:
        return "november"
    elif kuu_number == 12:
        return "detsember"
    else:
        return None
    
def kuupäev_nimega(kuu=9, päev=17, aasta=2025):
    kuu_nimi = mis_kuu(kuu)
    return f"{kuu_nimi} {päev}, {aasta}"

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))

tähtaeg = kuupäev_nimega(kuu, päev, aasta)

print(f"Kodutöö tähtaeg on {tähtaeg}")