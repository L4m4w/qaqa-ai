from unittest.mock import Mock, patch
from ai.adapters.openai_adapter import OpenAITestGenerator


def test_openai_generation():

    mock_response = Mock()
    mock_message = Mock()
    mock_message.content = "def test_sample(): assert True"
    mock_choice = Mock()
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]

    # 2. Мокаем именно то место, где импортируется OpenAI
    with patch('ai.adapters.openai_adapter.OpenAI') as mock_openai:
        # 3. Настраиваем мок-клиент
        mock_client = Mock()
        mock_openai.return_value = mock_client
        mock_client.chat.completions.create.return_value = mock_response

        generator = OpenAITestGenerator(api_key="fake-key")
        code = generator.generate_test(
            description="Test",
            prompt_type="web/test",
            context="Test context"
        )

        assert "def test_sample(): assert True" in code
        mock_client.chat.completions.create.assert_called_once()