import SGL_livros
from datetime import datetime

def verifica_emprestimo(livro):
	livro = str.capitalize(livro)
	livros = SGL_livros.retorna_livros()
	for i in range(len(livros)):
		if (livros[i][0] == livro):
			if (livros[i][5] == 0):
				return True
	return False

def realizar_emprestimo(nomeLivro,nomePessoa,livros):
	arquivo = open("livros.txt","w")
	now = datetime.now()
	data = ("%d/%d/%d" % (now.day, now.month, now.year)) 
	hora = ("%d:%d:%d" % (now.hour, now.minute, now.second))
	emprestimos = []
	for i in range(len(livros)):
		if (nomeLivro == livros[i][0]):
			livros[i][5] = 1
	for i in range(len(livros)):
		arquivo.write("%s;%s;%i;%s;%s;%i\n" % (str(livros[i][0]),str(livros[i][1]),int(livros[i][2]),str(livros[i][3]),str(livros[i][4]),int(livros[i][5])))
	arquivo.close()
	emprestimos.append([nomeLivro,nomePessoa,data,hora])
	arq = open("emprestimos.txt","a")
	arq.write("%s;%s;%s;%s\n"%(nomeLivro,nomePessoa,data,hora))
	arq.close()

def retorna_emprestimos():
	arquivo = open("emprestimos.txt","r")
	linhas = arquivo.read().splitlines()
	emprestimos = []
	for linha in linhas:
		emprestimos_txt = linha.split(";")
		nomeLivro = emprestimos_txt[0]
		nomePessoa = emprestimos_txt[1]
		data = emprestimos_txt[2]
		hora = emprestimos_txt[3]
		emprestimos.append([nomeLivro,nomePessoa,data,hora])
	arquivo.close()
	return emprestimos

def listar_emprestimos():
	emprestimos = retorna_emprestimos()
	for i in range(len(emprestimos)):
		print("\n■ Nome do Livro:",emprestimos[i][0])
		print("■ Está Com:",emprestimos[i][1])
		print("■ Data:",emprestimos[i][2])
		print("■ Hora:",emprestimos[i][3])

