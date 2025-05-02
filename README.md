# QA-AI Framework 🚀

**Умный генератор автотестов с AI-ассистентом**  
*Ускорьте создание тестов в 3 раза с помощью искусственного интеллекта*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-brightgreen)](https://pydantic.dev)
[![License](https://img.shields.io/badge/License-MIT-purple)](LICENSE)

# Умная валидация:
 - Проверка синтаксиса
 - Контроль наличия assert-проверок
 - Автоисправление простых ошибок

# Интеграция с популярными инструментами:

graph LR
  A[QA-AI] --> B(pytest)
  A --> C(Allure)
  A --> D(GitLab CI)

# Архитектура

graph TD
    A[Описание теста] --> B{AI-генератор}
    B --> C[Код на Python]
    C --> D[Валидация]
    D --> E[Запуск через Pytest]
    E --> F[Allure-отчет]

## 🌟 Ключевые возможности

- **AI-генерация тестов** из описания на естественном языке
- **Поддержка всех видов тестирования**:
```python
# UI (Selene), API (Requests), Mobile (Appium)
generator.generate_test("Проверка логина", type="web")
```
## 🛠 Быстрый старт
*Установка*
bash
```bash
pip install qa-ai-framework
```
**Пример использования**
```python

from qa_ai import OpenAITestGenerator

generator = OpenAITestGenerator(api_key="your_key")
test_code = generator.generate_test(
    description="Проверить корзину с 2 товарами",
    prompt_type="web/ecommerce"
)

exec(test_code)  # или сохраните в файл
```
# 📂 Структура проекта
```
.
├── ai/                  # AI-компоненты
├── autotests/           # Сгенерированные тесты
├── config/              # Настройки
└── docs/                # Примеры и руководства
```
# 🔧 Настройка
1. Создайте .env в корне проекта:

```ini
AI_OPENAI_API_KEY=your_key_here
AI_MODEL=gpt-4-turbo
```
2. Добавьте шаблоны в ai/prompts/:

```markdown
# web/login.md
Сгенерируй тест для: {description}
Требования:
- Используй PageObject
- Добавь 3 проверки
```
# 🤖 Поддерживаемые AI-провайдеры
```markdown
| Провайдер | Модели | Требования |
|-------------|-------------|
| OpenAI | GPT-3.5/4 | API-ключ |
| Llama.cpp | Llama 3/Mistral | 8+ GB RAM |
| Anthropic | Claude | Доступ по invite | 
```