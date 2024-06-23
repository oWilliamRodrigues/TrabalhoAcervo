# IMPLEMENTAÇÃO DA FILA 

class ArrayQueue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self._data[0]

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma fila de reserva para um livro
    reserve_queue = ArrayQueue()

    # Adicionando usuários à fila de reserva
    reserve_queue.enqueue("Usuário A")
    reserve_queue.enqueue("Usuário B")
    reserve_queue.enqueue("Usuário C")

    # Verificando o próximo usuário na fila de reserva
    print("Próximo usuário na fila de reserva:", reserve_queue.first())

    # Removendo o próximo usuário da fila de reserva após a notificação
    next_user = reserve_queue.dequeue()
    print("Usuário notificado e removido da fila de reserva:", next_user)
