def mis_kuu(mitmes_kuu):
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    return kuud[mitmes_kuu - 1]
    
def kuupäev_nimega(kuu=9, päev=17, aasta=2025):
    kuu_nimi = mis_kuu(kuu)
    return kuu_nimi + " " + str(päev) + ", " + str(aasta)

kuu= int(input("Mis on kodutöö tähtaja kuu number? "))
päev= int(input("Mis on kodutöö tähtaja kuu päev? "))
aasta= int(input("Mis on kodutöö tähtaja aasta? "))

tähtaeg = kuupäev_nimega(kuu, päev, aasta)

print("Kodutöö tähtaeg on", tähtaeg)