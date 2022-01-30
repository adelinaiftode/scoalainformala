lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(lista) #afisare lista

lista_asc = sorted(lista)
print(lista_asc) #afisare lista ascendenta

lista_asc.reverse()
print(lista_asc) #afisare lista descendenta

lista_asc.reverse()
lista_nr_pare = lista_asc[1::2]
print(lista_nr_pare) #afisare numere pare

lista_nr_impare = lista_asc[::2]
print(lista_nr_impare) #afisare numere impare

lista_multipli_3 = lista_asc[2::3]
print(lista_multipli_3)