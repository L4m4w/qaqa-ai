from unittest.mock import Mock
from ai.adapters.openai import OpenAITestGenerator


def test_openai_generation(monkeypatch):
    mock_response = Mock()
    mock_choice = Mock()
    mock_message = Mock()

    mock_message.content = 'def test_sample(): assert True'
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]

    monkeypatch.setattr(
        'openai.ChatCompletion.create',
        lambda *args, **kwargs: mock_response
    )

    # generator = OpenAITestGenerator(api_key="fake-key")
    generator = OpenAITestGenerator(api_key="fake-key")
    code = generator.generate_test(
        description="Test description",
        prompt_type="web/test",
        context="Additional context"
    )

    assert "def test_sample(): assert True" in code
    mock_response.assert_called_once()

    # Проверяем, что prompt_type был использован
    called_prompt = mock_response.call_args[1]['messages'][0]['content']
    assert "Test description" in called_prompt
    assert "Additional context" in called_prompt