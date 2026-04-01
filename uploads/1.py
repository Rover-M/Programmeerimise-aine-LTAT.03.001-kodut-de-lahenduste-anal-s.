
def mis_kuu (kuu):
    if kuu == 1:
        return "jaanuar"
    if kuu == 2:
        return "veebruar"
    if kuu == 3:
        return "märts"
    if kuu == 4:
        return "aprill"
    if kuu == 5:
        return "mai"
    if kuu == 6:
        return "juuni"
    if kuu == 7:
        return "juuli"
    if kuu == 8:
        return "august"
    if kuu == 9:
        return "september"
    if kuu == 10:
        return "oktoober"
    if kuu == 11:
        return "november"
    if kuu == 12:
        return "detsember"
    
def kuupäev_nimega (kuu=9, päev=17, aasta=2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

kuu=int(input("Mis on kodutöö tähtaja kuu number? "))
päev=int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta=int(input("Mis on kodutöö tähtaja aasta? "))

print("Kodutöö tähtaeg on ", kuupäev_nimega(kuu, päev, aasta))
