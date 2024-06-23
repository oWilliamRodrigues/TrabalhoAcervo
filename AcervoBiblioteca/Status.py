from enum import Enum

# Definição da Enumeração Status:
class Status(Enum):
    # Enumera os possíveis estados de um livro
    ATIVO = 'A'  # Livro está ativo (disponível para empréstimo)
    INATIVO = 'I'  # Livro está inativo (não disponível)
    EMPRESTADO = 'E'  # Livro está emprestado
    DISPONIVEL = 'D'  # Livro está disponível para empréstimo
