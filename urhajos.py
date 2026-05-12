class Urhajos:
    def __init__(self,nev,orszag,nem,szulev,urido):
        self.nev = nev
        self.orszag = orszag
        self.nem = nem
        self.szulev = int(szulev)
        self.urido = int(urido)
fajl =open ("urhajos.txt", "r", encoding="utf-8")
fajl.readline()
urhajosok = []
for sor in fajl:
        adatok = sor.strip().split(";")
        uj = Urhajos(adatok[0], adatok[1], adatok[2], adatok[3], adatok[4])
        urhajosok.append(uj)

fajl.close()

#3.4 feladat
print(f"Ennyi urhajos adata van benne: {len(urhajosok)}")

#3.5 feladadt
van = False
for u in urhajosok:
    if u.orszag == "ITA":
        van = True
        break
if van:
     print("VAn olasz")
else:
     print("Nincs olasz")
#3.6 feladat
osszeg = 0
darab = 0
for u in urhajosok:
     if u.nem == "N":
          osszeg += u.urido
          darab += 1
atlag = osszeg / darab
print(f"Ennyi idot toltttek a nok az urbe atlagosan: {atlag}")

#3.7
legfiatalabb = urhajosok[0]
for u in urhajosok:
    if u.szulev > legfiatalabb.szulev:
     legfiatalabb = u     

print(f"neve:{legfiatalabb.nev}")