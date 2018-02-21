# Criar um método que receba dois sets, adicione 1 elemento novo em cada um, remove outro elemento de cada um e faça um join
# e retorne o resultado

set1 = {'Elemento1', 'Elemento2', 'Elemento3'}
set2 = {'Elemento4', 'Elemento5', 'Elemento6'}

def brinca_sets(set1, set2):
	set1.add('NovoElemento')
	set2.add('MaisUmElemento')
	set1.remove('Elemento1')
	print(set1)
	set2.remove('MaisUmElemento')
	print(set2)
	set_final = set1 | set2
	print(set_final)

brinca_sets(set1, set2)