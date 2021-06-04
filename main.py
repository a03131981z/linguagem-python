import SGL_usuario
import SGL_menu
import SGL_livros
import SGL_emprestimos
import SGL_devolucao

SGL_menu.titulo()

opcao = ""
while opcao != "x":
	SGL_menu.menu_principal()
	opcao = str.lower(input("\n>> Digite Sua Opção: "))
	if opcao == "1":
		SGL_menu.print_titulo("Cadastrar Usuário")
		login = str.capitalize(input("\nLogin: "))
		senha = str.lower(input("Senha: "))
		confirmaSenha = str.lower(input("\nInforme a Senha Novamente: "))
		if confirmaSenha == senha:
			print("\nUsuário Cadastrado Com Sucesso!")
		while confirmaSenha != senha:
			print("\nAs Senhas Não Conferem!")
			confirmaSenha = str(input("\nInforme Novamente Sua Senha: "))
			if confirmaSenha == senha:
				print("\nUsuário Cadastrado Com Sucesso!")

		SGL_usuario.cad_usuario(login,senha)

	elif opcao == "2":
		SGL_menu.print_titulo("Entrar no Sistema")
		login = str.capitalize(input("\nLogin: "))
		senha = str.lower(input("Senha: "))
		existe = SGL_usuario.verifica_usuario(login,senha)
		if existe == True:
			print("\nSeja Bem Vindo(a)",login+"!")

			novaOpcao = ""
			while novaOpcao != "x":
				SGL_menu.menu_secundario()
				novaOpcao = str.lower(input("\n>> Digite Sua Opção: "))

				if novaOpcao == "1":
					SGL_menu.print_titulo("Cadastrar Livro")
					SGL_livros.cad_livro()
					print("\nLivro Cadastrado Com Sucesso!")
					
				elif novaOpcao == "2":
					SGL_menu.print_titulo("Listar Livros")
					SGL_livros.listar_livros()

				elif novaOpcao == "3":
					SGL_menu.print_titulo("Pesquisar Livro")
					if SGL_livros.persquisar_livro() == True:
						print("\nLivro Cadastrado No Sistema!")
					else:
						print("\nLivro Não Cadastrado No Sistema!")
						opcao = str.lower(input("\nDeseja Cadastrá-lo? [s/n] "))
						if opcao == "s":
							SGL_menu.print_titulo("Cadastrar Livro")
							SGL_livros.cad_livro()
						elif opcao == "n":
							print("\nVoltando Ao Menu...")

				elif novaOpcao == "4":
					SGL_menu.print_titulo("Realizar Empréstimo")
					nomeLivro = str.capitalize(input("\nDigite o Nome do Livro: "))
					existe = SGL_livros.existe_livro(nomeLivro)
					if existe == True:
						if SGL_emprestimos.verifica_emprestimo(nomeLivro) == True:
							nomePessoa = str.capitalize(input("Nome de Quem Receberá: "))
							livros = SGL_livros.retorna_livros()
							SGL_emprestimos.realizar_emprestimo(nomeLivro,nomePessoa,livros)
							print("\nEmpréstimo Realizado Com Sucesso!")
						else:
							print("\nO Livro Já  Está Emprestado!")
					else:
						print("\nEsse Livro Não Existe!")

				elif novaOpcao == "5":
					SGL_menu.print_titulo("Listar Empréstimos")
					SGL_emprestimos.listar_emprestimos()

				elif novaOpcao == "6":
					SGL_menu.print_titulo("Realizar Devoluções")
					nomeLivro = str.capitalize(input("\nDigite o Nome do Livro: "))
					existe = SGL_livros.existe_livro(nomeLivro)
					if existe == True:
						emprestado = SGL_emprestimos.verifica_emprestimo(nomeLivro)
						if emprestado == False:
							nomePessoa = str.capitalize(input("Nome da Pessoa: "))
							livros = SGL_livros.retorna_livros()
							SGL_devolucao.realizar_devolucao(nomeLivro,nomePessoa,livros)
							print("\nDevolução Realizada Com Sucesso!")
						else:
							print("\nO Livro Já Está Emprestado!")

					else:
						print("\nEsse Livro Não Existe!")

				elif novaOpcao == "7":
					SGL_menu.print_titulo("Listar Devoluções")
					SGL_devolucao.listar_devolucoes()

				elif novaOpcao == "8":
					SGL_menu.print_titulo("Excluir Livro")
					nomeLivro = str.capitalize(input("\nDigite o Nome do Livro: "))
					existe = SGL_livros.existe_livro(nomeLivro)
					if existe == True:
						livros = SGL_livros.retorna_livros()
						livros = SGL_livros.excluir_livro(nomeLivro,livros)
						SGL_livros.atualiza_lista(livros)
						print("\nLivro Excluído Com Sucesso!")
					else:
						print("\nO Livro Não Existe!")
					
				elif novaOpcao == "x":
					print("\nVoltando Ao Menu Inicial...")

				else:
					print("\nOpção Inválida!")

		elif existe == False:
			print("\nUsuário Ou Senha Inválidos!")

	elif opcao == "x":
		print("\nObrigado Por Testar Nosso Sistema!\nAté Mais!")

	else:
		print("\nOpção Inválida!")