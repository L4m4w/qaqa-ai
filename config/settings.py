from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pathlib import Path

def find_project_root():
    current = Path(__file__).parent
    while not (current / ".git").exists() and not (current / "pyproject.toml").exists():
        if current.parent == current:
            return Path.cwd()  # Fallback
        current = current.parent
    return current

PROJECT_ROOT = find_project_root()

class AISettings(BaseSettings):
    openai_api_key : SecretStr = None
    openai_model: str = "gpt-3.5-turbo"

    mistral_api_key : SecretStr = None
    mistral_model : str = "mistral-large-latest"

    local_model_path: str = "models/llama-3-8b.gguf"

    class Config:
        env_file = PROJECT_ROOT / ".env"
        env_prefix = "AI_"

class TestSettings(BaseSettings):
    base_url: str = "https://demoqa.com"
    headless: bool = True

settings = AISettings()
test_settings = TestSettings()