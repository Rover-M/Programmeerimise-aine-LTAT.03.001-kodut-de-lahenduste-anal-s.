def mis_kuu (kuu_number):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[kuu_number - 1]

def kuupäev_nimega(kuu=9, päev=17, aasta=2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

kuu = int(input("Sisesta kuu number: "))
päev = int(input("Sisesta päev: "))
aasta = int(input("Sisesta aasta: "))

print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")