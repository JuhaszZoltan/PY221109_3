#          0   1   2   3  4    5
szamok = [11, 42, 72, 11, 6, 103]
print(f'szamok lista elemei: {szamok}')
print(f'szamok lista 2-es indexű eleme: {szamok[2]}')
print(f'szamok lista elemeinek száma: {len(szamok)}')

szamok[3] = int(input('a szamok[3] új értéke: '))
print(f'a lista elemei mostmár: {szamok}')

uj:int = int(input('új elem a lista végére: '))
szamok.append(uj)
print(f'a lista elemei ismét: {szamok}')

uj:int = int(input('új elem a listába valahová: '))
index:int = int(input(f'hová szeretnéd beszúrni a {uj}-t? '))

szamok.insert(index, uj)
print(f'a lista elemei már megint: {szamok}')

elt:int = int(input('melyik elemet szeretnéd törölni a listáról? '))
szamok.remove(elt)
print(f'a lista elemei...: {szamok}')

index:int = int(input('honnan szeretnél törölni a listából? '))
szamok.pop(index)

print(f'a lista elemei: {szamok}')

print('minden elem duplája: ')
# [11, 42, 72, 10, 6, 103, 10]
for szam in szamok:
    print(szam * 2)

allatok:list[str] = ['kutya', 'cica', 'pingvin', 'ló']