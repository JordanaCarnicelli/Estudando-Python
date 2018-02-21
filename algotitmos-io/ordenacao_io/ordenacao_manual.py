# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:22:23 2018

@author: jordana.arruda
"""

lista1 = [10, 2, 5, 3, 8, 5, 4, 6, 0]
lista2 = [8, 9, 3, 3, 10, 11, 7, 4, 1]
lista_final = []

def separa (lista, pivo, r):

	c = lista[pivo]
	i = pivo + 1
	j = r

	while i <= j :
		if lista[i] <= c :
			i += 1
		elif c < lista[j] :
			j -= 1
		else :
			t = lista[i]
			lista[i] = lista[j]
			lista[j] = t
			i += 1
			j -= 1

	lista[pivo] = lista[j]
	lista[j] = c
	return j

def quicksort (lista, pivo, r):

	while pivo < r :
		j = separa(lista, pivo, r)
		quicksort(lista, pivo, j-1)
		pivo = j + 1

def ordena_lista(lista):

	pivo = 0
	r = len(lista)-1
	quicksort(lista, pivo, r)

def limpa_duplicados(lista):

	for i in range(len(lista)):
		if i < len(lista) - 1:
			if lista[i] == lista[i + 1]:
				lista.pop(i)

def unifica_lista(lista1, lista2):

	i = 0
	j = 0

	while i < len(lista1) : #Depois é necessário consumir o restante da lista2
		if lista1[i] > lista2[j] :
			lista_final.append(lista2[j])
			j += 1
		elif lista1[i] < lista2[j] :
			lista_final.append(lista1[i])
			i += 1
		else :
			lista_final.append(lista1[i])
			i += 1
			j += 1

	if j < len(lista2):
		while j < len(lista2):
			lista_final.append(lista2[j])
			j += 1


ordena_lista(lista1)
print(lista1)
limpa_duplicados(lista1)
print(lista1)
ordena_lista(lista2)
print(lista2)
limpa_duplicados(lista2)
print(lista2)
unifica_lista(lista1, lista2)
print(lista_final)