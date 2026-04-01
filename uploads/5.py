def mis_kuu(kuu):
    kuud = ("jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember")
    if 1 <= kuu <= 12:
        return kuud[kuu -1]
    else:
        return "puudub"
def kuupäev_nimega(kuu=9, päev=17, aasta=2025):  
    kuu_nimi = mis_kuu(kuu)
    return f"{kuu_nimi} {päev}, {aasta}"

def main():
    kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
    päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
    aasta = int(input("Mis on kodutöö tähtaja aasta? "))
    tahtaeg = kuupäev_nimega(kuu, päev, aasta)
    print(f"Kodutöö tähtaeg on {tahtaeg}")

main()