kuud=['jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']

def mis_kuu(kuu):
    return kuud[kuu-1]

def kuupäev_nimega(kuuu=9,päev=17,aasta=2025):
    kuupäev=mis_kuu(kuuu)+' '+str(päev)+', '+str(aasta)
    return kuupäev


kodutöö_kuu=int(input('Mis on kodutöö tähtaja kuu number? '))
kodutöö_päev=int(input('Mis on kodutöö tähtaja kuu päev? '))
kodutöö_aasta=int(input('Mis on kodutöö tähtaja aasta? '))

print('Kodutöö tähtaeg on',kuupäev_nimega(kodutöö_kuu,kodutöö_päev,kodutöö_aasta))