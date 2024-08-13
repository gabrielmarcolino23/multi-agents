from models.openai_models import get_open_ai


class PromptVerifier:
    def __init__(self):
        self.openai_model = get_open_ai()