
def mis_kuu(kuu):
    if kuu == 1:
        return 'jaanuar'
    elif kuu == 2:
        return 'veebruar'
    elif kuu == 3:
        return 'märts'
    elif kuu == 4:
        return 'aprill'
    elif kuu == 5:
        return 'mai'
    elif kuu == 6:
        return 'juuni'
    elif kuu == 7:
        return 'juuli'
    elif kuu == 8:
        return 'august'
    elif kuu == 9:
        return 'september'
    elif kuu == 10:
        return 'oktoober'
    elif kuu == 11:
        return 'november'
    elif kuu == 12:
        return 'detsember'
    else:
        return "Sisesta õige kuu"

def kuupäev_nimega(kuu=9, päev=17, aasta=2025):
    kuu_nimi = mis_kuu(kuu)
    return f"{kuu_nimi} {päev}, {aasta}"

kuu = int(input('Mis on kodutöö tähtaja kuu number? '))
päev = int(input('Mis on kodutöö tähtaja kuu päev? '))
aasta = int(input('Mis on kodutöö tähtaja aasta? '))

# Вывод результата
print(f"Kodutöö tähtaeg on {kuupäev_nimega(kuu, päev, aasta)}")