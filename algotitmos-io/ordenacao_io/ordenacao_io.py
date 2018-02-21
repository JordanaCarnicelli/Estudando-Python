lista_final = []
listaUm = []
listaDois = []

def ordena_lista(lista):

	return (lista.sort())

def limpa_duplicados(lista):

	for i in range(len(lista)):
		if i < len(lista) - 1:
			if lista[i] == lista[i + 1]:
				lista.pop(i)

def mescla_listas(lista1, lista2):
	for i in range (len(lista1)):
		if lista1[i] not in lista2:
			lista2.append(lista1[i])
	return lista2

def le_arquivo_e_cria_lista(endereco_l1, endereco_l2):

	lista1 = open(endereco_l1, "r")
	lista2 = open(endereco_l2, "r")

	# Codigo retirado de https://mail.python.org/pipermail/tutor/2002-May/014665.html
	#read line into array
	for line in lista1.readlines():
		# loop over the elemets, split by whitespace
		for i in line.split():
			# convert to integer and append to the list
			listaUm.append(int(i))

	for line in lista2.readlines():
		for i in line.split():
			listaDois.append(int(i))

def cria_arquivo_final(lista_final):

	listaFinal = open("big-data-study/algotitmos-io/ordenacao_io/ListaFinal.txt", "w")
	i = 0
	while i < len(lista_final):
		listaFinal.write(str(lista_final[i]))
		listaFinal.write(' ')
		i += 1

def main():

	le_arquivo_e_cria_lista("big-data-study/algotitmos-io/ordenacao_io/Lista1.txt", "big-data-study/algotitmos-io/ordenacao_io/Lista2.txt")
	lista_final = mescla_listas(listaUm, listaDois)
	ordena_lista(lista_final)
	limpa_duplicados(lista_final)
	cria_arquivo_final(lista_final)

main()