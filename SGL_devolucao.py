import SGL_livros
from datetime import datetime

def realizar_devolucao(nomeLivro,nomePessoa,livros):
	arquivo = open("devolucoes.txt","a")
	arq = open("livros.txt","w")
	now = datetime.now()
	data = ("%d/%d/%d" % (now.day, now.month, now.year)) 
	hora = ("%d:%d:%d" % (now.hour, now.minute, now.second))
	arquivo.write("%s;%s;%s;%s\n" % (nomeLivro, nomePessoa, data, hora))
	for i in range(len(livros)):
		if (nomeLivro == livros[i][0]):
			livros[i][5] = 0
	for i in range(len(livros)):
		arq.write("%s;%s;%i;%s;%s;%i\n" % (str(livros[i][0]),str(livros[i][1]),int(livros[i][2]),str(livros[i][3]),str(livros[i][4]),int(livros[i][5])))

	arquivo.close()
	arq.close()

def retorna_devolucoes():
	arquivo = open("devolucoes.txt","r")
	linhas = arquivo.read().splitlines()
	devolucoes = []
	for linha in linhas:
		devolucoes_txt = linha.split(";")
		nomeLivro = devolucoes_txt[0]
		nomePessoa = devolucoes_txt[1]
		data = devolucoes_txt[2]
		hora = devolucoes_txt[3]
		devolucoes.append([nomeLivro,nomePessoa,data,hora])
	arquivo.close()
	return devolucoes

def listar_devolucoes():
	devolucoes = retorna_devolucoes()
	for i in range(len(devolucoes)):
		print("\n■ Nome do Livro:",devolucoes[i][0])
		print("■ Devolvido Por:",devolucoes[i][1])
		print("■ Data:",devolucoes[i][2])
		print("■ Hora:",devolucoes[i][3])



