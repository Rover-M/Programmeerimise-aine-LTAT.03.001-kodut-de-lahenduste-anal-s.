def mis_kuu(kuunumber):
    kuud = ["jaanuar", "veebruar", "märts", "aprill",
            "mai", "juuni", "juuli", "august",
            "september", "oktoober", "november", "detsember"]
    if 1 <= kuunumber <= 12:
        return kuud[kuunumber - 1]

def kuupäev_nimega(kuu= 9, päev=17, aasta=2025):
    kuunimi = mis_kuu(kuu)
    return f"{kuunimi} {päev}, {aasta}"

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))

kuupäev = kuupäev_nimega(kuu, päev, aasta)

print(f"Kodutöö tähtaeg on {kuupäev}")
