def mis_kuu(kuu_nr: int) -> str:
    """Võtab kuu numbri (1–12) ja tagastab kuu nime eesti keeles."""
    kuud = [
        "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
        "juuli", "august", "september", "oktoober", "november", "detsember"
    ]
    if 1 <= kuu_nr <= 12:
        return kuud[kuu_nr - 1]
    else:
        return "vigane kuu"


def kuupäev_nimega(kuu: int = 9, päev: int = 17, aasta: int = 2025) -> str:
    """Tagastab kuupäeva kujul '<kuunimi> <päev>, <aasta>'."""
    return f"{mis_kuu(kuu)} {päev}, {aasta}"


kuu = int(input("Mis on kodutöö tähtaja kuu number? "))
päev = int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta = int(input("Mis on kodutöö tähtaja aasta? "))

print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")

