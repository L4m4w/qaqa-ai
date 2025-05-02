import os
from pathlib import Path

from openai import OpenAI
from qa_ai.core.generator import AITestGenerator

class OpenAITestGenerator(AITestGenerator):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        base_dir = Path(os.path.dirname(os.path.abspath(__file__))).parent
        super().__init__(prompts_dir=base_dir / "prompts")
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def load_prompt(self, prompt_type: str) -> str:
        """Загружает шаблон из qa_ai/prompts/"""
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

        response = self.client.chat.completions.create(
            model = self.model,
            messages=[{'role': "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content