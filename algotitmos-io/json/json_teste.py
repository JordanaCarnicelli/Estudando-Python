import json
import itertools as it

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

#Criando um dictionary com o conteudo do JSON
grace_hopper = json.load(open("big-data-study/algotitmos-io/json/pessoa2.json"))

#Criando uma string com o conteudo do JSON (manualmente)
grace_hopper2 = json.dumps({"primeiro_nome": "Grace","nome_meio": "Murray","ultimo_nome": "Hopper","dt_nascimento": "09/12/1906","cidade_nascimento": "Nova Iorque","profissoes": ["analista de sistemas", "almirante"],"contribuicoes": ["mae do COBOL", "termo BUG", "uma das primeiras programadoras do Harvard Mark"]}, separators=(',',':'))

#Validando os tipos
print(type(grace_hopper)) #Dicionario
print(type(grace_hopper2)) #String

#Vendo o JSON ou STRING
print(grace_hopper)
print(grace_hopper2)

#Vericando se dt_nascimento esta no dicionario
valor = 'dt_nascimento' in grace_hopper
print(valor)

#Verificando o tamanho do dicionario
print(len(grace_hopper)) #Tamanho inicial = 7
print(len(grace_hopper2)) #Tamanho inicial = 277

#Alterando valores manualmente
grace_hopper['dt_nascimento'] = '10/11/1912'
print(grace_hopper)
grace_hopper['dt_nascimento'] = '09/12/1906'

#Incluindo contribuicao
grace_hopper['contribuicoes'].append('mulher com alto posto militar')

#Criando uma copia com copy
new_grace = grace_hopper.copy()

#Criando uma copia com fromkeys
new_grace2 = grace_hopper.fromkeys(grace_hopper.keys())


#Iterando sobre os elementos que compoem o JSON/dictionary
for key, values in grace_hopper.items(): #Python 2 - iteritems() | Python 3 - items()
	print (grace_hopper[key])

#Iterando sobre itens das listas que compoem o JSON/dictionary
for key, value in grace_hopper.items():
	for element in value:
		#Identificando as listas (as Strings terao char's como elementos e portanto, tamanho = 1)
		if len(element) > 1:
			if value.index(element) == 0:
				print('Chave: ' + key)
			print('Valor: ' + element)
			print(value.index(element))

#Testando utilizar a lib itertools
for key, values in (it.chain([(k, v) for k, v in grace_hopper.items()])):
	print (grace_hopper[key])

#Contem erro
'''for key, values in (it.chain.from_iterable([(k, v) for k, v in grace_hopper.items()])):
	print (grace_hopper[key])'''

#Testando demais funcoes
print(grace_hopper.get('primeiro_nome'))
print(grace_hopper.get('contribuicoes'))

#Testando decoders e encoders:
