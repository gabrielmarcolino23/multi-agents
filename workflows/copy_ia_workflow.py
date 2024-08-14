from tasks.promptVerifier_task import create_planner_task
from agents.promptVerifier import PlannerAgent
from states.state import AgentGraphState
from crewai import Crew

'''

def marketing_campaign_flow():
    # Inicializar o estado compartilhado
    state = AgentGraphState()

    # Criar o PlannerAgent
    planner_agent = PlannerAgent(state=state, model='gpt-4', server='openai', temperature=0.7)

    # Criar a tarefa do PlannerAgent
    planner_task = create_planner_task(planner_agent)

    # Criar a equipe com a tarefa
    crew = Crew(agents=[planner_agent], tasks=[planner_task])

    # Executar a equipe
    crew.execute()
'''