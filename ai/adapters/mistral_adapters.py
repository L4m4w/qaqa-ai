from mistralai.client import MistralClient

from ai.core.generator import AITestGenerator
from config import settings

class OpenAITestGenerator(AITestGenerator):
    client = MistralClient(api_key=settings.settings.mistral_api_key)  # Регистрация на https://mistral.ai
    response = client.chat(
        model="mistral-tiny",
        messages=[{"role": "user", "content": "Сгенерируй тест..."}]
)