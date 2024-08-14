from models.openai_models import get_open_ai
from states.state import AgentGraphState

from crewai import Agent


class promptVerifier:
     def __init__(self, state: AgentGraphState, model=None, server=None, temperature=0, tools=None):
        self.state = state
        self.model = model
        self.server = server
        self.temperature = temperature
        self.tools = tools or []
        self.llm = self.get_llm()

     def get_llm(self):
        if self.server == 'openai':
            return get_open_ai(model=self.model, temperature=self.temperature)
        else:
            raise ValueError(f"Servidor {self.server} não suportado.")
        
     #def invoke():

     def update_state(self, key, value):
        # Atualiza o estado compartilhado
        self.state = {**self.state, key: value}   
    
