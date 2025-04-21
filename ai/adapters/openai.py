from openai import OpenAI
from ai.core.generator import AITestGenerator

class OpenAITestGenerator(AITestGenerator):
    def __init__(self, api_key: str, model: str = "gpt-4-turbo"):
        super().__init__()
        self.client = OpenAI(api_key=api_key)
        self.model = model

        def generate_test(self, description: str, prompt_type: str, context: str = None) -> str:
            prompt = self.load_prompt(prompt_type).format(
                description=description,
                context=context or ""
            )