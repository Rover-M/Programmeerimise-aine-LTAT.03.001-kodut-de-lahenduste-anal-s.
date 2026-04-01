kuud = [
'jaanuar', 'feebruar', 'märts', 'april', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktober', 'november', 'detsember'
]


def mis_kuu(kuu_number):
   if kuu_number >= 1 and kuu_number <= 12:
       return kuud[kuu_number - 1]
   else:
       return 'Tundmatu kuu'

def kuupäev_nimega(kuu=9, päev=17, aasta=2025):
    kuu_nimi = mis_kuu(kuu)
    return f'{kuu_nimi} {päev}, {aasta}'
        

kuu_number = int(input('Mis on kodutöö tähtaja kuu number? '))
päev = int(input('Mis on kodutöö tähtaja kuu päev? '))
aasta = int(input('Mis on kodutöö tähtaja aasta? '))

tähtaeg = kuupäev_nimega(kuu_number, päev, aasta)

print(f'Kodutöö tähtaeg on {tähtaeg}')