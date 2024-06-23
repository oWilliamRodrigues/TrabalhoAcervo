from Status import Status
from fila import ArrayQueue


# Implementação da Classe Livro:
class Livro:

    def __init__(self, id, title, author, year, publisher, Status):
        # Inicializa os atributos do livro
        self.id = id  # Identificador único do livro
        self.title = title  # Título do livro
        self.author = author  # Autor do livro
        self.year = year  # Ano de publicação do livro
        self.publisher = publisher  # Editora do livro
        self.status = Status  # Status de disponibilidade do livro (emprestado ou ativo)
        self.reserve_queue = ArrayQueue()  # Fila de espera para o livro
