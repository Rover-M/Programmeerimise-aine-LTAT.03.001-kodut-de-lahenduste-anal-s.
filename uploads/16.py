def mis_kuu(kuu: int) -> str:
    kuud = ("jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember" )
    return kuud [kuu - 1]
def kuupäev_nimega(kuu: int = 9, päev: int = 17, aasta: int = 2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtajaaasta? "))

print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")
