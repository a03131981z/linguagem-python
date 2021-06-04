def titulo():
	print("╔═══════════════════════════════════╗")
	print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
	print("║░░ ╔══════ ░░ ╔══════ ░░ ║       ░░║")
	print("║░░ ║       ░░ ║       ░░ ║       ░░║")
	print("║░░ ╚═════╗ ░░ ║   ══╗ ░░ ║       ░░║")
	print("║░░       ║ ░░ ║     ║ ░░ ║       ░░║")
	print("║░░ ══════╝ ░░ ╚═════╝ ░░ ╚══════ ░░║")
	print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
	print("╚═══════════════════════════════════╝")
	print(" SISTEMA DE GERENCIAMENTO DE LIVROS")

def menu_principal():
	print("\n-----------MENU-----------")
	print("| [1] Cadastrar Usuário  |")
	print("| [2] Entrar No Sistema  |")
	print("| [x] Sair               |")
	print("--------------------------")

def menu_secundario():
	print("\n------------MENU-------------")
	print("| [1] Cadastrar Livro       |")
	print("| [2] Listar Livros         |")
	print("| [3] Pesquisar Livro       |")
	print("| [4] Realizar Empréstimo   |")
	print("| [5] Listar Empréstimos    |")
	print("| [6] Realizar Devolução    |")
	print("| [7] Listar Devoluções     |")
	print("| [8] Excluir Livro         |")
	print("| [x] Sair                  |")
	print("-----------------------------")

def print_titulo(msg):
	tam = len(msg)
	linha = "═"*tam;
	print("")
	print("╔═════"+linha+"═════╗")
	print("║░░░░ "+msg+" ░░░░║")
	print("╚═════"+linha+"═════╝")
