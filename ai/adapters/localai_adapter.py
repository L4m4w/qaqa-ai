from llama_cpp import Llama
from ai.core.generator import AITestGenerator


class LocalAITestGenerator(AITestGenerator):
    def __init__(self):
        super().__init__()
        self.llm = Llama(
            model_path="llama-3-8b-instruct.Q5_K_M.gguf",  # Скачать с HuggingFace
            n_ctx=2048
        )

    def generate_test(self, description: str, context: str = None) -> str:
        prompt = f"Сгенерируй тест на Python для: {description}"
        response = self.llm.create_chat_completion(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response['choices'][0]['message']['content']