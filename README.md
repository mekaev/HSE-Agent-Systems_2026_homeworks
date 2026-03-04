# HSE Agent Systems

Репозиторий курса по агентным системам в НИУ ВШЭ.

## Требования

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) — быстрый менеджер пакетов и виртуальных окружений для Python

## Установка uv

### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Или через **winget**:

```powershell
winget install --id=astral-sh.uv -e
```

### macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Или через **Homebrew**:

```bash
brew install uv
```

### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

После установки перезапустите терминал, чтобы `uv` стал доступен в `PATH`.

Проверить установку:

```bash
uv --version
```

## Настройка проекта

### 1. Клонировать репозиторий

```bash
git clone <url-репозитория>
cd HSE-Agent-Systems_2026
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
uv sync
```

Эта команда автоматически:
- создаст виртуальное окружение в папке `.venv`
- установит все зависимости из `pyproject.toml`

### 3. Настроить переменные окружения

В корне проекта есть файл `.env.example` с шаблоном необходимых переменных окружения. Скопируйте его в `.env` и заполните своими значениями:

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

Затем откройте `.env` и укажите свои ключи:

```dotenv
GIGACHAT_API_KEY=ваш-ключ
GIGACHAT_SSL_VERIFY=false

POLZA_AI_API_KEY=ваш-ключ

GITHUB_TOKEN=ваш-токен
```

Если у вас чего то нет, то просто оставьте поле пустым

> **Важно:** файл `.env` содержит секреты и не должен попадать в git. Убедитесь, что он добавлен в `.gitignore`.

### 4. Активация окружения (опционально)

`uv run` автоматически использует окружение проекта, но если нужно активировать его вручную:

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

## Управление зависимостями

### Добавить новую библиотеку

```bash
uv add <имя-пакета>
```

Пример:

```bash
uv add requests
```

### Удалить библиотеку

```bash
uv remove <имя-пакета>
```

### Обновить все зависимости

```bash
uv sync --upgrade
```


## Структура проекта

```
├── src/             # Исходный код (конфиги, утилиты, агенты)
├── lectures/        # Материалы лекций (практики и домашние задания)
└── pyproject.toml   # Конфигурация проекта и зависимости
```
