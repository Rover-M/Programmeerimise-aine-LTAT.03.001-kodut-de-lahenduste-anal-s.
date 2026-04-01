def mis_kuu(number):
    if number==1:
        return "jaanuar"
    elif number==2:
        return "veebruar"
    elif number==3:
        return"märts"
    elif number==4:
        return"aprill"
    elif number==5:
        return"mai"
    elif number==6:
        return"juuni"
    elif number==7:
        return"juuli"
    elif number==8:
        return"august"
    elif number==9:
        return"september"
    elif number==10:
        return"oktoober"
    elif number==11:
        return"november"
    else:
        return"detsember"
    
def kuupäev_nimega(kuu=9,päev=17,aasta=2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"
kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))
print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu,päev,aasta)}")