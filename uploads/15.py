c = int(input("Mis on kodutöö tähtaja kuu number? "))
y = int(input("Mis on kodutöö tähtaja kuu päev? "))
z = int(input("Mis on kodutöö tähtaja aasta? "))

def mis_kuu(c):
    if (c == 1):
        k = "jaanuar"
    elif (c == 2):
        k = "veebruar"
    elif (c == 3):
        k = "märts"
    elif (c == 4):
        k = "aprill"
    elif (c == 5):
        k = "mai"
    elif (c == 6):
        k = "juuni"
    elif (c == 7):
        k = "juuli"
    elif (c == 8):
        k = "august"
    elif (c == 9):
        k = "september"
    elif (c == 10):
        k = "oktoober"
    elif (c == 11):
        k = "november"
    elif (c == 12):
        k = "detsember"
    else:
        k = "september"
    return k

def kuupäev_nimega(c=9, y=17, z=2025):
    
    if (1 <= y <= 31):
        päev = y
    else:
        päev = 17
    aasta = z
    return (f"{mis_kuu(c)} {päev}, {aasta}")


print(f"Kodutöö tähtaeg on {kuupäev_nimega(c, y, z)}")



