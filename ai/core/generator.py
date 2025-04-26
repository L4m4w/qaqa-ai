import ast
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Tuple


class AITestGenerator(ABC):
    def __init__(self, prompts_dir = 'prompts'):
        self.prompts_dir = Path(prompts_dir)

    def load_prompt(self, prompt_type: str) -> str:
        prompt_file = self.prompts_dir/f'{prompt_type}.md'
        return prompt_file.read_text(encoding='utf-8')

    def validate_code(self, code: str) -> Tuple[bool, str]:
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return False, f"Syntax error: {e}"

        # Check func existence
        functions = [
            node for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ]
        if not functions:
            return False, "No functions, add at least one"

        # Check assert existence
        has_assert = any(
            isinstance(node, ast.Assert)
            for node in ast.walk(tree)
        )

        # Check .should() (for Selene) existence
        has_should = any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "should"
            for node in ast.walk(tree)
        )

        if not (has_assert or has_should):
            return False, "Code doesn't has any checks (assert/should)"

        return True, "Code is valid"

    def generate_and_validate(self, description: str, context: str = None) -> Tuple[str, bool, str]:
        code = self.generate_test(description, context)
        is_valid, message = self.validate_code(code)
        return code, is_valid, message

    @abstractmethod
    def generate_test(self, description: str, context: str = None) -> str:
        pass