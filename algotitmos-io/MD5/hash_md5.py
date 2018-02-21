import hashlib

def hashMD5 (password):
	masc = hashlib.md5()
	masc.update(password.encode('utf-8'))
	return masc.hexdigest()

def get_password ():
	password = input('Insira a frase que deseja mascarar: ')
	hash_pass = hashMD5(password)
	print(hash_pass)

get_password()

