# main.py
from Catalogo_Biblioteca import LibraryCatalog
from livro import Livro
from Interface_usuario import Interface
from usuario import Usuario
from pilha import ArrayStack
from fila import ArrayQueue
from listaEncadeada import DoublyLinkedListIterator

# Função Main
if __name__ == "__main__":
    # Criando uma pilha de histórico para um livro
    history_stack = ArrayStack()

    catalog = LibraryCatalog()

    #Fila para Fila de Espera
    reserve_queue = ArrayQueue()

    # Crie uma instância da classe Interface e chame o método executar
    interface = Interface(catalog)
    interface.executar()


    # # Exemplo Criando instâncias das estruturas de dados
    # library = LibraryCatalog()
    # book1 = Livro(1, "Python for Beginners", "John Smith", 2020,  "A", "A")
    # book2 = Livro(2, "Data Structures and Algorithms", "Alice Johnson",
    #               2019,"I", "I")

    # library.add_livro(book1)
    # library.add_livro(book2)

    # print(library.procurar_livro("Python for Beginners"))
    # print(library.remover_livro(book2))
    # print(library.remover_livro(book2))
