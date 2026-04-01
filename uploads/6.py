def mis_kuu(nr):
    if nr == 1:
        return 'jaanuar'
    elif nr == 2:
        return 'veebruar'
    elif nr == 3:
        return 'märts'
    elif nr == 4:
        return 'aprill'
    elif nr == 5:
        return 'mai'
    elif nr == 6:
        return 'juuni'
    elif nr == 7:
        return 'juuli'
    elif nr == 8:
        return 'august'
    elif nr == 9:
        return 'september'
    elif nr == 10:
        return 'oktoober'
    elif nr == 11:
        return 'november'
    elif nr == 12:
        return 'detsember'
    
def kuupäev_nimega(kuu = 9, päev = 17, aasta = 2025):
    kuu = mis_kuu(kuu)
    return (f"{kuu} {päev}, {aasta}")
    

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))

print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")





















