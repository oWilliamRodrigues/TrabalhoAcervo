# # acervo.py
# from enum import Enum
# from listaEncadeada import DoublyLinkedListIterator
#
# class Status(Enum):
#     ATIVO = 'A'
#     INATIVO = 'I'
#
# # Implementação da Classe Livro:
# class Livro:
#     def __init__(self, title, author, year, publisher, Status):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.year = year
#         self.publisher = publisher
#         self.status = Status
#
#     def __str__(self):
#         return f"{self.title} ({self.year}) - {self.author}, {self.publisher}, {self.status}"
#
# # Implementação do Catálogo da Biblioteca:
# class LibraryCatalog:
#     def __init__(self):
#         self.livro_list = DoublyLinkedListIterator()
#
#     def add_livro(self, livro):
#         self.livro_list.addNode(livro)
#
#     def remover_livro(self, livro):
#         current_node = self.livro_list.firstNode
#         while current_node:
#             if current_node.data == livro:
#                 self.livro_list.iterator = current_node
#                 self.livro_list.elimNode()
#                 return True
#             current_node = current_node.nextNode
#         return False
#
#     def procurar_livro(self, title):
#         print('procurou')
#         current_node = self.livro_list.firstNode
#         print('Current Node', current_node)
#         while current_node:
#             print('é igual? ', current_node.data.title == title)
#             if current_node.data.title == title:
#                 print('Current_Node Data', current_node.data)
#                 return current_node.data
#             current_node = current_node.nextNode
#         return None
#
#
# # # Código para testar a função de carregamento do catálogo
# # def converterDataAc(catalog):
# #  for livro in catalog:
# #          if len(livro['year']) > 4:
# #            primeiraLetra = int(livro['year'][0])
# #            ano = str((int(primeiraLetra) * -100) - 1000)
# #            livro['year'] = ano
# #          else:
# #            livro['year'] = str(int(livro['year']))
# #  return catalog
#
#  #Implementação do Carregamento do Catálogo:
# def load_catalog(filename, catalog):
#      with open(filename, 'r', encoding='utf-8') as file:
#          for line in file:
#              data = line.strip().split(",")
#              if len(data) == 4:
#                  title, author, year, publisher = map(str.strip, data)
#                  catalog.add_livro(Livro(title, author, year, publisher,Status))
#                  # catalog = converterDataAc(catalog)
#              else:
#                  print("Ignorando linha mal formatada:", line)
#
# # Código para carregar o catálogo quando este arquivo for importado
#
# catalog = LibraryCatalog()
# print(catalog)
# load_catalog('acervo.txt', catalog)