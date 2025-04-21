from openai import OpenAI
from pathlib import Path
from typing import Literal
import inspect


class TestGenerator:
    def __init__(self, api_key: str = None, model: str = "gpt-4-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def _load_prompt(self, prompt_type: Literal["web", "api"]) -> str:
        with open(f"ai/prompts/{prompt_type}_tests.md", "r") as f:
            return f.read()

    def generate_test(
            self,
            description: str,
            test_type: Literal["web", "api"],
            context: str = None
    ) -> str:
        prompt_template = self._load_prompt(test_type)
        prompt = f"""
        {prompt_template}

        Контекст: {context}
        Описание теста: {description}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3  # Для меньшей креативности
        )
        return response.choices[0].message.content

    def generate_and_run(self, description: str, test_type: str):
        generated_code = self.generate_test(description, test_type)

        # Динамическое выполнение кода
        try:
            exec(generated_code, globals())
            print("✅ Тест успешно сгенерирован и выполнен")
        except Exception as e:
            print(f"❌ Ошибка в сгенерированном тесте: {e}")
            print(generated_code)