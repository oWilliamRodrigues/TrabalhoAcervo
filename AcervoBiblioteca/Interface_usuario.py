from Status import Status
from usuario import Usuario
from fila import ArrayQueue

class Interface:
    def __init__(self, catalog):
        # Inicializa a interface com o catálogo de livros
        self.catalog = catalog

    def exibir_opcoes(self):
        # Exibe as opções disponíveis no menu
        print("**************************")
        print("Opções:")
        print("1 - PROCURAR")
        print("2 - CHECAR A LISTA DE ESPERA")
        print("3 - EMPRESTAR")
        print("4 - DEVOLVER")
        print("5 - EXIBIR CATÁLOGO")
        print("6 - SAIR")
        print("**************************")

    def executar(self):
        # Executa a interface do usuário
        while True:
            self.exibir_opcoes()
            opcao = input("Escolha uma opção (1/2/3/4/5/6): ")

            if opcao == "1":
                self.buscar_livro()
            elif opcao == "2":
                self.checar_fila_espera()
            elif opcao == "3":
                self.emprestar_livro()
            elif opcao == "4":
                self.devolver_livro()
            elif opcao == "5":
                self.exibir_catalogo()
            elif opcao == "6":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def buscar_livro(self):
        # Procura por um livro no catálogo pelo título
        titulo = input("Digite o título do livro: ")
        for livro in self.catalog:
            if livro.title.lower() == titulo.lower():
                print(f"Livro '{livro.title}' encontrado!")
                print(f"Autor: {livro.author}")
                print(f"Ano: {livro.year}")
                print(f"Editora: {livro.publisher}")
                return
        print("Livro não encontrado.")

    def checar_fila_espera(self):
        # Verifica a fila de espera de um livro pelo título
        titulo = input("Digite o título do livro: ")
        livro = next((l for l in self.catalog if l.title.lower() == titulo.lower()), None)

        if livro:
            if livro.reserve_queue:
                print(f"Livro '{livro.title.lower()}' tem {len(livro.reserve_queue)} pessoas na fila de espera.")
            else:
                print(f"Livro '{livro.title.lower()}' não tem ninguém na fila de espera.")
        else:
            print("Livro não encontrado.")

    def emprestar_livro(self):
        # Empresta um livro para um usuário
        titulo = input("Digite o título do livro a ser emprestado: ")
        livro = next((l for l in self.catalog if l.title.lower() == titulo.lower()), None)

        if livro:
            if livro.status == Status.EMPRESTADO:
                print("Livro não disponível no momento.")
            else:
                usuario = input("Digite o nome do usuário: ")
                usuario = Usuario(usuario)

                livro.reserve_queue.enqueue((livro, usuario))
                livro.status = Status.EMPRESTADO
                print(f"Livro '{livro.title}' emprestado para '{usuario.name}'.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self):
        # Devolve um livro que estava emprestado
        titulo = input("Digite o título do livro a ser devolvido: ")
        livro = next((l for l in self.catalog if l.title.lower() == titulo.lower()), None)

        if livro:
            if livro.status == Status.EMPRESTADO:
                livro.reserve_queue.dequeue()
                livro.status = Status.ATIVO
                print(f"Livro '{livro.title}' devolvido.")
            else:
                print("Livro não emprestado no momento.")
        else:
            print("Livro não encontrado.")

    def exibir_catalogo(self):
        # Exibe o catálogo de livros
        print("Tentei exibir o catálogo")
        # Criar um iterador do catálogo de livros
        iterator = self.catalog.iterator()
        print("Iterador passou")
        # Verificar se o catálogo de livros está vazio
        if self.catalog.is_empty():
            print("Catálogo de livros está vazio.")
            return

        # Exibir o catálogo de livros
        print("**************************")
        print("Catálogo:")

        # Loop através do catálogo de livros
        while iterator.nextNode():
            current_node = iterator.iterator
            print(f"Título: {current_node.data.title}")
            print(f"Autor: {current_node.data.author}")
            print(f"Ano: {current_node.data.year}")
            print(f"Editora: {current_node.data.publisher}")
            print("**************************")
