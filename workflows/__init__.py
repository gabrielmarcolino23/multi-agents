from .copy_ia_workflow import copy_ai_workflow

# Definir o que será exportado quando o pacote workflows for importado
__all__ = ['marketing_campaign_flow']

# Função auxiliar para inicializar todos os fluxos de trabalho, se necessário
def initialize_workflows():
    """
    Função para inicializar e executar todos os fluxos de trabalho.
    Pode ser personalizada para incluir lógica de inicialização adicional.
    """
    copy_ai_workflow()