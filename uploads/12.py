kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

def mis_kuu(n: int):
    return kuud[n - 1]

def kuupäev_nimega(kuu: int = 9, päev: int = 17, aasta: int = 2025):
    return f"{mis_kuu(kuu)} {päev}, {aasta}"

k = int(input("Mis on kodutöö tähtaja kuu number?"))
p = int(input("Mis on kodutöö tähtaja kuu päev?"))
a = int(input("Mis on kodutöö tähtaja aasta?"))

print(f"Kodutöö tähtaeg on {kuupäev_nimega(k, p, a)}")