def cad_livro():
	nome = str.capitalize(input("\nNome: "))
	autor = str.capitalize(input("Autor(a): "))
	ano = int(input("Ano: "))
	genero = str.capitalize(input("Gênero: "))
	descricao = str.capitalize(input("Descrição: "))
	emprestimo = 0
	arquivo = open("livros.txt","a")
	arquivo.write("%s;%s;%i;%s;%s;%i\n" % (nome,autor,ano,genero,descricao,emprestimo))
	arquivo.close()
	
def retorna_livros():
	arquivo = open("livros.txt","r")
	linhas = arquivo.read().splitlines()
	livros = []
	for linha in linhas:
		livros_txt = linha.split(";")
		nome = livros_txt[0]
		autor = livros_txt[1]
		ano = livros_txt[2]
		genero = livros_txt[3]
		descricao = livros_txt[4]
		emprestimo = int(livros_txt[5])
		livros.append([nome,autor,ano,genero,descricao,emprestimo])
	arquivo.close()
	return livros

def listar_livros():
	livros = retorna_livros()
	for i in range(len(livros)):
		print("\n■ Nome:",livros[i][0])
		print("■ Autor(a):",livros[i][1])
		print("■ Ano:",livros[i][2])
		print("■ Gênero:",livros[i][3])
		print("■ Descrição:",livros[i][4])

		if int(livros[i][5]) == 1:
			print("■ Emprestado: Sim")
		else:
			print("■ Emprestado: Não")

def persquisar_livro():
	pesquisa = str.capitalize(input("\nDigite O Nome do Livro: "))
	livros = retorna_livros()
	for i in range(len(livros)):
		if livros[i][0] == pesquisa:
			print("\n■ Nome:",livros[i][0])
			print("■ Autor(a):",livros[i][1])
			print("■ Ano:",livros[i][2])
			print("■ Gênero:",livros[i][3])
			print("■ Descrição:",livros[i][4])
			if int(livros[i][5]) == 1:
				print("■ Emprestado: Sim")
			else:
				print("■ Emprestado: Não")
			return True
	return False

def existe_livro(nome):
	nome = str.capitalize(nome)
	existe = False
	livros = retorna_livros()
	for i in range(len(livros)):
		if livros[i][0] == nome:
			existe = True
	return existe

def excluir_livro(nomeLivro,livros):
	arquivo = open("livros.txt","w")
	for i in range(len(livros)):
		if nomeLivro == livros[i][0]:
			livros.remove(livros[i])
	return livros

def atualiza_lista(livros):
	arquivo = open("livros.txt","w")
	for i in range(len(livros)):
		arquivo.write("%s;%s;%i;%s;%s;%i\n" % (str(livros[i][0]),str(livros[i][1]),int(livros[i][2]),str(livros[i][3]),str(livros[i][4]),int(livros[i][5])))
	arquivo.close()



