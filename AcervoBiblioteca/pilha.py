# IMPLEMENTAÇÃO DA PILHA 

class Activity:
    def __init__(self, activity_type, date, user):
        self.activity_type = activity_type
        self.date = date
        self.user = user

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._data.pop()

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma pilha de histórico para um livro
    history_stack = ArrayStack()

    # Registrando uma atividade de empréstimo
    history_stack.push(Activity("Empréstimo", "2024-04-17", "Usuário A"))

    # Registrando uma atividade de devolução
    history_stack.push(Activity("Devolução", "2024-04-18", "Usuário B"))

    # Verificando a última atividade registrada
    print("Última atividade registrada:", history_stack.top().activity_type)
    print("Data:", history_stack.top().date)
    print("Usuário:", history_stack.top().user)

    # Removendo a última atividade registrada
    last_activity = history_stack.pop()
    print("Atividade removida:", last_activity.activity_type)
    print("Data:", last_activity.date)
    print("Usuário:", last_activity.user)