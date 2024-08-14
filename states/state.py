class AgentGraphState:
    def __init__(self):
        self.state_data = {}

    def update_state(self, key, value):
        """
        Atualiza o estado com uma nova chave e valor.
        Se a chave já existir, seu valor será atualizado.
        """
        self.state_data[key] = value

    def get_state(self, key):
        """
        Recupera o valor associado a uma chave específica no estado.
        Retorna None se a chave não existir.
        """
        return self.state_data.get(key)

    def remove_state(self, key):
        """
        Remove uma chave específica do estado, se ela existir.
        """
        if key in self.state_data:
            del self.state_data[key]

    def get_all_state(self):
        """
        Retorna todo o estado armazenado como um dicionário.
        """
        return self.state_data

    def clear_state(self):
        """
        Limpa todo o estado armazenado, removendo todas as chaves e valores.
        """
        self.state_data.clear()

    def merge_state(self, new_state):
        """
        Mescla outro dicionário de estado com o estado atual.
        Em caso de conflito de chave, o valor do novo estado prevalece.
        """
        self.state_data.update(new_state)





