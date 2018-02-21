# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:07:06 2018

@author: jordana.arruda
"""

tab = []
cont = 0
players = []

def recebe_nomes():

	players.append([])
	players[0] = input('Insira o nome do primeiro usuario: ')
	players.append([])
	players[1] = input('Insira o nome do segundo usuario: ')

def recebe_tam_tab():

	n_tab = input('Insira a quantidade de linhas do tabuleiro desejado: ')
	print('O tabuleiro terá o tamanho do valor inserido (ex: 3x3, 4x4, etc)')

	return (n_tab)

def pede_pos(player):

	print(player)
	pos = input('Insira a posicao desejada: ')

	return (pos)

def cria_tab(n_tab):

	n_tab = int(n_tab)

	for i in range(n_tab):
		tab.append([])
		for j in range(n_tab):
			tab[i].append(" ")

	mostra_pos(n_tab, n_tab)
	return tab

def imprime_tab():

	for i in range(len(tab)):
		line = " "
		for j in range(len(tab[i])):
			line += tab[i][j]
			if j != len(tab[i])-1:
				line += " |"
		print (line)
	print('\n')

def troca_jogador(jogador):

	if jogador == players[0]:
		return players[1]
	else:
		return players[0]

def mostra_pos(lin, col):

	global cont
	print('Essas sao as posicoes disponiveis para o seu jogo:')
	for i in range(lin):
		vet = []
		for j in range(col):
			vet.append(str(cont))
			cont += 1
		print (vet)

def valida_pos(jogada):

	jogada = int(jogada)
	#Verifica se dentro do tabuleiro
	if jogada > cont or jogada < 0:
		return 1
	else:
		return 0

def realiza_jogada(pos, jogador, tam):

	pos = int(pos)
	tam = int(tam)
	valida = valida_pos(pos)
	retorno = 0
	if valida == 0:
		resto = pos % tam
		resto = int(resto)
		quociente = pos/tam
		quociente = int(quociente)
		if tab[quociente][resto] == " ":
			retorno = aux_jogada(jogador, quociente, resto, tam)
		else:
			retorno = 1
			print('Posicao ocupada!')
	else:
		retorno = 1
		print('Jogada invalida!')

	return retorno

def aux_jogada(jogador, quociente, resto, tam):

	quociente = int(quociente)
	resto = int(resto)

	if jogador is players[0]:
		tab[quociente][resto] = 'X'
	else:
		tab[quociente][resto] = 'O'

	comp = tab[quociente][resto]
	registro = 0
	# Valida vitoria na horizontal
	for j in range(len(tab[quociente])):
		if tab[quociente][j] == comp:
			registro += 1
	if registro == tam:
		return 2
	else:
		i = 0
		registro = 0
		#Valida vitoria na vertical
		while(i < len(tab)):
			if tab[i][resto] == comp:
				registro += 1
			i += 1
		if registro == tam:
			return 2
		# Valida diagonal principal
		else:
			registro = 0
			for i in range (len(tab)):
				for j in range (len(tab)):
					if i == j and tab[i][j] == comp:
						registro += 1
			if registro == tam:
				return 2
			# Ainda falta validar a diagonal nao principal (secundaria)
			return 0

def jogo_teste():

	recebe_nomes()
	tabuleiro = recebe_tam_tab()
	cria_tab(tabuleiro)
	aux = cont
	jogador = players[0]
	while aux > 0:
		pos = pede_pos(jogador)
		resposta = realiza_jogada(pos, jogador, tabuleiro)
		imprime_tab()
		if resposta == 2:
			print('Parabéns ' + jogador + '! Você ganhou!')
			break
		if resposta == 0:
			aux -= 1
			jogador = troca_jogador(jogador)


jogo_teste()