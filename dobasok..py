
def kozte(a, b, c):
    if b <= a and a <= c:
        return True
    
    else:
        return False
import random
db = 0
for i in range (150):
    szam = random.randint(1,12)
    if kozte(szam,4,8):
        db += 1

print(f"Ennyi esett 4 és 8 közé 150 számból :{db}")
atlag = (db/150)* 100
#atlag = round(db/150* 100, 2)
print(f"Etz az összes dobás {atlag: .2f} szazaleka")
