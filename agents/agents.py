import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from crewai_tools.tools import PDFConsultTool
from langgraph import Graph, Node

# Carregar as variáveis de ambiente
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Inicializar a ferramenta de consulta ao PDF
pdf_tool = PDFConsultTool(pdf_path="curso_copy.pdf")

# Definição dos agentes com diferentes modelos fine-tuned
class Agentes:
    def agente_verificacao_prompt(self):
        # Modelo fine-tuned para verificação de prompt
        # llm_verificacao = ChatOpenAI(api_key=api_key, model="gpt-4o-mini-verificacao-prompt")
        return Agent(
            role='Agente de Verificação de Prompt',
            goal='Verificar se o prompt está correto e dentro dos padrões esperados. Se estiver, passar o prompt para o próximo agente.',
            backstory='Responsável por garantir que os prompts recebidos sejam de alta qualidade antes de prosseguir.',
            llm='gpt-4o-mini-2024-07-18'
        )

    def agente_geracao_copy(self):
        # Modelo fine-tuned para geração de copy
        # llm_geracao = ChatOpenAI(api_key=api_key, model="gpt-4o-mini-geracao-copy")
        return Agent(
            role='Agente de Geração de Copy',
            goal='Criar copys com base no prompt recebido, utilizando boas práticas de copywriting.',
            backstory='Especialista em criar textos persuasivos utilizando um modelo GPT-4o-mini com fine-tuning e consulta a um curso de copywriting.',
            tools=[pdf_tool],
            llm='gpt-4o-mini-2024-07-18'
        )

    def agente_analista_copy(self):
        # Modelo fine-tuned para análise de copy
        # llm_analise = ChatOpenAI(api_key=api_key, model="gpt-4o-mini-analise-copy")
        return Agent(
            role='Agente Analista de Copy',
            goal='Verificar se a copy está dentro dos padrões esperados. Se estiver, aprovar a copy como output; se não, solicitar uma nova.',
            backstory='Garantidor da qualidade final das copys, assegurando que atendam aos padrões exigidos.',
            llm='gpt-4o-mini-2024-07-18'
        )

# Instanciar os agentes
agentes = Agentes()
agente_verificacao_prompt = agentes.agente_verificacao_prompt()
agente_geracao_copy = agentes.agente_geracao_copy()
agente_analista_copy = agentes.agente_analista_copy()

# Criar o workflow de interação entre os agentes usando langgraph
workflow = Graph()

# Adicionar nós ao workflow
workflow.add_node(Node("Agente de Verificação de Prompt", agent=agente_verificacao_prompt))
workflow.add_node(Node("Agente de Geração de Copy", agent=agente_geracao_copy))
workflow.add_node(Node("Agente Analista de Copy", agent=agente_analista_copy))

# Conectar os nós (definindo a sequência de trabalho)
workflow.add_edge("Agente de Verificação de Prompt", "Agente de Geração de Copy")
workflow.add_edge("Agente de Geração de Copy", "Agente Analista de Copy")

# Criar as tarefas
task_verificacao_prompt = Task(
    description="Verificar o prompt recebido e encaminhar ao próximo agente se estiver correto.",
    expected_output='Prompt verificado.',
    agent=agente_verificacao_prompt
)

task_geracao_copy = Task(
    description="Criar a copy com base no prompt, utilizando boas práticas de copywriting.",
    expected_output='Copy gerada com sucesso.',
    agent=agente_geracao_copy
)

task_analise_copy = Task(
    description="Verificar se a copy gerada está dentro dos padrões e aprovar ou solicitar uma nova.",
    expected_output='Copy final aprovada ou rejeitada.',
    agent=agente_analista_copy
)

# Criar a equipe para gerenciar a execução das tarefas
crew = Crew(
    agents=[agente_verificacao_prompt, agente_geracao_copy, agente_analista_copy],
    tasks=[task_verificacao_prompt, task_geracao_copy, task_analise_copy],
    graph=workflow,
    verbose=True
)

# Iniciar a execução das tarefas
resultados = crew.kickoff()

# Exibir os resultados
print("######################teste")
for resultado in resultados:
    print(resultado)
