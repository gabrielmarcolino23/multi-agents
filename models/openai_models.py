import openai

# Dicionário que mapeia os nomes dos modelos básicos para os IDs ou nomes das versões fine-tuned
FINE_TUNED_MODELS = {
    "gpt-4o-mini": {
        "default": "gpt-4o-mini-2024-07-18",
        "version_2": "gpt-4o-mini-finetuned-5678"
    },
}

class OpenAIModel:
    def __init__(self, model_name, version="default", temperature=0.5, max_tokens=1000, api_key=None):
        self.model_name = model_name
        self.version = version
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key or self._load_api_key()
        self.fine_tuned_model = self._get_fine_tuned_model()

    def _load_api_key(self):
        # Carregar a chave da API de uma variável de ambiente ou de um arquivo seguro
        import os
        return os.getenv('OPENAI_API_KEY')

    def _get_fine_tuned_model(self):
        # Recupera o modelo fine-tuned correspondente ao nome e versão especificados
        if self.model_name in FINE_TUNED_MODELS:
            return FINE_TUNED_MODELS[self.model_name].get(self.version)
        else:
            raise ValueError(f"Modelo {self.model_name} não tem fine-tuning disponível.")

    def invoke(self, messages):
        # Utiliza o modelo fine-tuned se estiver disponível
        model_to_use = self.fine_tuned_model if self.fine_tuned_model else self.model_name
        
        # Interagir com a API da OpenAI para gerar uma resposta
        response = openai.ChatCompletion.create(
            model=model_to_use,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            api_key=self.api_key
        )
        return response.choices[0].message  # Retorna a primeira mensagem gerada

# Função para obter um modelo específico com fine-tuning
def get_open_ai(model='gpt-4o-mini', version="default", temperature=0.5):
    return OpenAIModel(model_name=model, version=version, temperature=temperature)

# Função para obter um modelo específico com fine-tuning para JSON
def get_open_ai_json(model='gpt-4o-mini', version="default", temperature=0.5):
    return OpenAIModel(model_name=model, version=version, temperature=temperature, max_tokens=1500)
