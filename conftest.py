import pytest
from ai.test_generator import TestGenerator

@pytest.fixture(scope="session")
def ai_tester():
    return TestGenerator(api_key="your-api-key")

def pytest_generate_tests(metafunc):
    if "ai_test_description" in metafunc.fixturenames:
        # Генерация тестов на лету по описанию
        descriptions = [
            "Проверить логин с валидными данными",
            "Проверить ошибку при пустом пароле"
        ]
        metafunc.parametrize("ai_test_description", descriptions)