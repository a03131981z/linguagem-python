def cad_usuario(login,senha):
	arquivo = open("login.txt","a")
	arquivo.write("%s;%s\n" % (login,senha))
	arquivo.close()

def retorna_listaUsuario():
	usuarios = []
	arquivo = open("login.txt","r")
	linhas = arquivo.read().splitlines()		
	for linha in linhas:
		login_txt = linha.split(";")
		login = login_txt[0]
		senha = login_txt[1]
		usuarios.append([login,senha])
	arquivo.close()
	return usuarios

def verifica_usuario(login,senha):
	usuarios = retorna_listaUsuario()
	if usuarios[0][0] == login:
		if usuarios[0][1] == senha:
			return True
	return False




