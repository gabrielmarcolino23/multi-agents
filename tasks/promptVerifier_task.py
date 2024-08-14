from crewai import Task
from agents.promptVerifier import promptVerifier

def create_planner_task(agent: promptVerifier):
    """
    Cria uma tarefa específica para o PlannerAgent, utilizando uma ferramenta de leitura de PDF.
    """
    # Descrição da tarefa
    description = "Planejar a estratégia de marketing para o próximo trimestre."

    # Ferramentas que o PlannerAgent usará durante essa tarefa
    pdf_tool = PDFReaderTool(pdf_path="caminho/para/seu/arquivo.pdf")

    # Esperado que o PlannerAgent produza um plano de marketing detalhado
    expected_output = "Plano de marketing detalhado para o próximo trimestre."

    # Cria a tarefa, associando-a ao agente e às ferramentas
    planner_task = Task(
        description=description,
        agent=agent,
        tools=[pdf_tool],  # Associar a ferramenta PDFReaderTool à tarefa
        expected_output=expected_output
    )

    return promptVerifier_task