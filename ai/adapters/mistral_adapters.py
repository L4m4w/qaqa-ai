from mistralai import Mistral
import os
from pathlib import Path

from ai.core.generator import AITestGenerator
from config import settings

class MistralAITestGenerator(AITestGenerator):
    def __init__(self, api_key, model: str = "mistral-tiny"):
        base_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
        super().__init__(prompts_dir=base_dir / "prompts")
        self.client = Mistral(api_key=api_key)
        self.model = model

    def load_prompt(self, prompt_type: str) -> str:
        """Загружает шаблон из ai/prompts/"""
        # Добавляем .md, если нет расширения
        if not prompt_type.endswith('.md'):
            prompt_type += '.md'

        prompt_path = self.prompts_dir / prompt_type

        if not prompt_path.exists():
            # Покажем все доступные файлы для отладки
            available = list(self.prompts_dir.glob('**/*.md'))
            raise FileNotFoundError(
                f"Prompt '{prompt_type}' not found in {self.prompts_dir}.\n"
                f"Available prompts: {[p.relative_to(self.prompts_dir) for p in available]}"
            )

        return prompt_path.read_text(encoding='utf-8')

    def generate_test(self, description: str, prompt_type: str, context: str = None) -> str:
        prompt = self.load_prompt(prompt_type).format(
            description=description,
            context=context or ""
        )

        chat_response = self.client.chat.complete(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        print(self.clean_code_response(chat_response.choices[0].message.content))

        return self.clean_code_response(chat_response.choices[0].message.content)

    def clean_code_response(self, response: str) -> str:
        """Удаляет Markdown-разметку кода"""
        if response.startswith("```python") and response.endswith("```"):
            return response[9:-3].strip()
        elif response.startswith("```") and response.endswith("```"):
            return response[3:-3].strip()
        return response