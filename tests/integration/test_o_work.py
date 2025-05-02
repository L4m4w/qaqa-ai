from pathlib import Path

from ai.adapters.mistral_adapters import MistralAITestGenerator

from config import settings

print(settings.settings.mistral_api_key)
print(settings.settings.mistral_model)


# Создаём генератор тестов
generator = MistralAITestGenerator(
    api_key=settings.settings.mistral_api_key,  # Ключ OpenAI
    model=settings.settings.mistral_model# Модель ИИ
)

# Описываем тест на естественном языке
test_code = generator.generate_test(
    description="Проверить логин с валидными данными",
    prompt_type="web/login",  # Использует шаблон из ai/prompts/web/login.md
    context="LoginPage: #username, #password, #submit"
)

print(test_code)
PROJECT_ROOT = Path(__file__).parent.parent
# Динамическое выполнение сгенерированного кода
exec(test_code)
try:
    exec(test_code)
except SyntaxError as e:
    test_file = Path(PROJECT_ROOT / "autotests/test_login.py")

    test_file.parent.mkdir(parents=True, exist_ok=True)
    print(e)
    # Или сохранение в файл
    with open(test_file, "w") as f:
        f.write(test_code)
