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
        return "tundmatu kuu"
    


def kuupäev_nimega(kuu = 9, päev = 17, aasta = 2025):
    return mis_kuu(kuu) + " " + str(päev) + ", " + str(aasta)

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))

print("Kodutöö tähtaeg on", kuupäev_nimega(kuu, päev, aasta))