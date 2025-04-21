Ты — эксперт по автоматизации тестирования на Python. Сгенерируй код UI-теста с использованием Selene.

**Требования:**
1. Используй Page Object паттерн
2. Добавь проверки через `should`
3. Тест должен быть атомарным

**Шаблон:**
'''python
from pages.{page_name}_page import {PageName}Page
import pytest

def test_{description_snake_case}():
    page = {PageName}Page()
    (page
     .open()
     .{action1}("{value1}")
     .{action2}()
     .assert_{result}("{expected_value}"))
'''

**Контекст:**
{context}