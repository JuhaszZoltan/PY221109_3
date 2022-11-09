import random
szamok = []
for x in range(10):
    szamok.append(random.randint(10, 99))
print(f'a lista elemei kiindulási állapotban: {szamok}')

i:int = int(input('hányas indexű számot akarod törölni? '))
if i >= len(szamok) or i < 0:
    print('nincs ilyen indexű elem')
else:
    print(f'töröltem a {szamok[i]} elemet a listáról!')
    szamok.pop(i)
    print(f'a lista elemei a törlés után: {szamok}')