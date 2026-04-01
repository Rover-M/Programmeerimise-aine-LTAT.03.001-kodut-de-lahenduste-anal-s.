#Inimese ekraani osa
kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev?"))
aasta = int(input("Mis on kodutöö tähtaja aasta?"))


#Funktsiooni osa

def mis_kuu(kuu_number):
    kuud = [
        "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"
    ]
    if 1 <= kuu_number <= 12:
        return kuud[kuu_number - 1]
    else:
        return "Tundamatu kuu"

def kuupäev_nimega(kuu= 9, päev=17, aasta=2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

print("Kodutöö tähtaeg on", kuupäev_nimega(kuu, päev, aasta))

#Esimese korraga kood 67/100, muttsin def kuupäev_nimega(kuu= 9, päev=17, aasta=2025)