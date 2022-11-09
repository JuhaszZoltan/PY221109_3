# 'elemi' v. 'egyszerű' programozási tételek:
# INPUT: minden esetben egy sorozat
# OUTPUT: minden esetben egy érték

sorozat = [42, 11, 23, 32, 11, 87, 61, 50]
print(f'a sorozat elemei: {sorozat}')

# sorozatszámítás (összegzés)
osszeg = 0
for elem in sorozat:
    osszeg += elem
print(f'a sorozat elemeinek összege: {osszeg}')
print(f'a sorzat elemeinek átlaga: {osszeg / len(sorozat)}')

# megszámlálás:
# pl.: 50-nél kisebb elemek száma
darab = 0
for elem in sorozat:
    if elem < 50:
        darab += 1
print(f'50-nél kisebb elemek száma: {darab}')

# szélsőérték helyének meghatározása
# pl. a sorozat legnagyobb elemének helye
maxi = 0
for index in range(1, len(sorozat)):
    if sorozat[index] > sorozat[maxi]:
        maxi = index
print(f'legnagyobb elem indexe: {maxi}')
print(f'a legnagyobb elem értéke: {sorozat[maxi]}')