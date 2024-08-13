# Importar a classe principal do state.py
from .state import AgentGraphState

# Definir o que será exportado quando o pacote states for importado
__all__ = ['AgentGraphState']

# Exemplo de uso para fins de debug ou setup
def initialize_state():
    """
    Função para inicializar e retornar um estado padrão.
    Pode ser estendida para configurar estados iniciais específicos.
    """
    return AgentGraphState()
