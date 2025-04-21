from abc import ABC, abstractmethod
from pathlib import Path

class AITestGenerator(ABC):
    def __init__(self, prompts_dir: str = 'prompts'):
        self.prompts_dir = Path(prompts_dir)

    def load_prompt(self, prompt_type: str) -> str:
        prompt_file = self.prompts_dir/f'{prompt_type}.md'
        return prompt_file.read_text(encoding='utf-8')

