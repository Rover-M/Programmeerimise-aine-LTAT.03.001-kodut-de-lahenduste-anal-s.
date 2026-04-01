def mis_kuu(kuu_nr):
    kuud = [
        "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "detsember"
    ]
    return kuud[kuu_nr - 1]

def kuupäev_nimega(kuu = 9, päev = 17, aasta = 2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))
print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")