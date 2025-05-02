import pytest
from qa_ai.core.generator import AITestGenerator
from qa_ai.adapters.openai_adapter import OpenAITestGenerator

class MockGenerator(AITestGenerator):
    """
    Mock test for basic class
    """
    def generate_test(self, description: str, context: str = None) -> str:
        return "def test_sample(): assert 1 == 1"

def test_code_validation_success():
    generator = MockGenerator()
    code = "def test(): assert 1 == 1"
    is_valid, msg = generator.validate_code(code)
    assert is_valid is True

def test_code_validation_failure():
    generator = MockGenerator()
    code = "def test(: pass"
    is_valid, msg = generator.validate_code(code)
    assert is_valid is False
    assert "Syntax error" in msg

def test_code_validation_failure_on_assert_existence():
    generator = MockGenerator()
    code = "def test(): pass"
    is_valid, msg = generator.validate_code(code)
    assert is_valid is False
    assert "Code doesn't has any checks" in msg