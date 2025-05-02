from ai.adapters.openai_adapter import OpenAITestGenerator

from config import settings

print(settings.settings.mistral_api_key)
print(settings.settings.openai_api_key)


# Создаём генератор тестов
generator = OpenAITestGenerator(
    api_key=settings.settings.openai_api_key,  # Ключ OpenAI
    model=settings.settings.openai_model# Модель ИИ
)

# Описываем тест на естественном языке
test_code = generator.generate_test(
    description="Проверить логин с валидными данными",
    prompt_type="web/login",  # Использует шаблон из ai/prompts/web/login.md
    context="LoginPage: #username, #password, #submit"
)

print(test_code)

# Динамическое выполнение сгенерированного кода
exec(test_code)

# Или сохранение в файл
with open("autotests/test_login.py", "w") as f:
    f.write(test_code)
