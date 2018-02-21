import json

# JSON utilizado:
'''{
	"primeiro_nome": "Grace",
	"nome_meio": "Murray",
	"ultimo_nome": "Hopper",
	"dt_nascimento": "09/12/1906",
	"cidade_nascimento": "Nova Iorque",
	"profissoes": ["analista de sistemas", "almirante"],
	"contribuicoes": ["mae do COBOL", "termo BUG", "uma das primeiras programadoras do Harvard Mark"]
}'''

#Cria um dictionary com o conteudo do JSON
def carrega_json(path):
	return (json.load(open(path)))

#Valida os tipos
def valida_tipo(dado):
	print("O parametro informado eh do tipo:")
	print(type(dado))

#Ve o dado
def visualiza_dado(dado):
	print(dado)

#Imprime mensagens na tela, concatenando com o dado informado
def imprime(texto, dado):
	print(texto + dado)

#Verifica se uma determinada chave esta no dicionario
def busca_chave(dict, chave):
	return (chave in dict)

#Verifica o tamanho do dado (dicionario)
def verifica_tamanho(dict):
	return (len(dict))

#Funcao auxiliar para a alteracao do valor de uma chave
def auxilia_troca_valor(dict, chave, novo_valor):
	#Esse if inicial garante que nao seja possivel passar uma lista como novo valor para uma chave contendo String
	if type(dict.get(chave)) is type(novo_valor):
		dict[chave] = novo_valor
		return 0
	#Esse elif garante que sempre que houver uma lista, o novo valor sera incluido como novo elemento dessa lista
	#(mantendo-se os anteriores)
	elif type(dict.get(chave)) is list:
		dict[chave].append(novo_valor)
		return 0
	#Qualquer outro caso deve gerar erro
	else:
		return 1

#Altera o valor de uma chave
def altera_valor(dict, chave, novo_valor):
	if auxilia_troca_valor(dict, chave, novo_valor) == 0:
		visualiza_dado(dict)
		valida_dict(dict)
	else:
		raise Exception ("Erro! Sugestao: Verifique se o valor inserido eh do mesmo tipo que o valor anterior para a chave indicada.")

#Substitui o valor de uma chave
def substitui_valor(dict, chave, novo_valor):
	dict[chave] = novo_valor
	valida_dict(dict)

#Cria uma copia do dictionary usando copy()
def cria_novo_dict_cp(dict):
	return (dict.copy())

#Cria uma copia do dictionary usando fromkeys(). Por default, os valores sao todos nulos
def cria_novo_dict_fk(dict):
	novo_dict = dict.fromkeys(dict.keys())
	valida_dict(novo_dict)
	return (novo_dict)

#Valida os valores do JSON/dictionary. Se houver campo com valor nulo, gera excecao
def valida_dict(dict):
	for chave, valor in dict.items():
		if dict.get(chave) == None:
			raise Exception ("Nao devem existir valores vazios!")

#Itera sobre os elementos mais externos que compoem o JSON/dictionary
def itera_dict(dict):
	for chave, valor in dict.items(): #Python 2 - iteritems() | Python 3 - items()
		pass

#Itera sobre itens das listas que compoem o JSON/dictionary
def itera_elementos_dict(dict):
	for chave, valor in dict.items():
		for elemento in valor:
			#Identificando as listas (as Strings terao char's como elementos e portanto, tamanho = 1)
			if len(elemento) > 1:
				if valor.index(elemento) == 0:
					print('Chave: ' + chave)
				print('Valor: ' + elemento)
				print(valor.index(elemento))

#Itera sobre elementos de uma chave especificada presente no JSON/dictionary
def itera_elemento_espec(dict, chave_buscada):
	try:
		for elemento in dict.get(chave_buscada):
			print(chave_buscada + '[' + str(dict.get(chave_buscada).index(elemento)) + ']')
			print(elemento)
	except TypeError:
		print("Parece que a chave buscada nao pertence ao dado")
	except:
		print("Ops! Esse erro eu nao previ.")

def inicio():
	path = "big-data-study/algotitmos-io/json/pessoa2.json"
	pessoa_json = carrega_json(path)
	valida_tipo(pessoa_json)
	visualiza_dado(pessoa_json)
	imprime("A chave primeiro_nome esta presente no json? ", str(busca_chave(pessoa_json, 'primeiro_nome')))
	imprime("A chave cidade_atual esta presente no json? ", str(busca_chave(pessoa_json, 'cidade_atual')))
	imprime("O JSON informado tem tamanho: ", str(verifica_tamanho(pessoa_json)))
	altera_valor(pessoa_json, 'dt_nascimento', '10/11/1912')
	altera_valor(pessoa_json, 'contribuicoes', 'mulher com alto posto militar')
	altera_valor(pessoa_json, 'dt_nascimento', '09/12/1906')
	#Esperada mensagem de erro ao executar a linha abaixo
	#altera_valor(pessoa_json, 'primeiro_nome', ['Ana', 'Joana', 'Margarida'])
	#Alterando o valor da chave contribuicoes (NULL)
	cp1_pessoa_json = cria_novo_dict_cp(pessoa_json)
	#Esperada mensagem de erro ao executar a linha abaixo
	#cp2_pessoa_json = cria_novo_dict_fk(pessoa_json)
	valida_tipo(cp1_pessoa_json)
	#Esperada mensagem de erro ao executar a linha abaixo
	#substitui_valor(cp1_pessoa_json, 'contribuicoes', None)
	itera_dict(cp1_pessoa_json)
	itera_elementos_dict(cp1_pessoa_json)
	itera_elemento_espec(pessoa_json, 'contribuicoes')
	itera_elemento_espec(pessoa_json, 'chave_nao_existente')

inicio()