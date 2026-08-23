 
 
 Установить пакет

 ```bash
 npm i -g @anthropic-ai/claude-code
 ```

 В папке "".claude" в файле "settings.local.json" стартовые настройки:

 ```json
 {
    "env": {
        "IS_DEMO": "1"
    }
 }
 ```
 IS_DEMO - включает режим демо

 ## Команды
 /usage - проверить лимиты
 
 клавиша Esc - выйти из /usage

 /model - выбор модели ИИ:
 sonnet - средний (рекомендуется)
 opus - самый мощный
 haiku - самый слабый, самый быстрый

 Контекстное окно - ...

 .claudeignore

 /init - читает все файлы проекта и составляет описание в файл .md

 /clear - очистить контек окно, создаст новую сессию. Новую инфу будет давать на основе созданных md-файлов с описанием проекта
 /resume - выбрать из списка старую сессию, чтобы вернуться к ней
 /compact - сожмет контекстное окно, выбрав из него самое важное
 /memory - ?

 Нужно помогать нейросети, давая абсолютный путь к конкретному файлу после @

==============================================
## DeepSeek

platform.deepseek.com

settings.local.json в папке ".claude":
```json
{
    "hasCompletedOnboarding": true,
    "env": {
        "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
        "ANTHROPIC_AUTH_TOKEN": "YOUR_DEEPSEEK_TOKEN_HERE",
        "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
        "IS_DEMO": "1"
    }
}

```
Если есть ошибки с подключением, то можно попробовать в settings.json добавить "skipWebFetchPreflight": true
Добавка может выглядеть так

```json
{
    "hasCompletedOnboarding": true,
    "skipWebFetchPreflight": true
    "env": {
        "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
        "ANTHROPIC_AUTH_TOKEN": "YOUR_DEEPSEEK_TOKEN_HERE",
        "ANTHROPIC_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
        "CLAUDE_CODE_DISABLENONESSENTIAL_TRAFFIC": "1",
    }
}

```

/status - команда покажет куда мы подключаемся
/model - сомотреть или переключить модель нейросети
/init

### Уровни хранения инструкций

~/.claude/CLAUDE.md         - Глобальная (Общие инструкции для всех проектов)
/project-root/CLAUDE.md     - Проект (Стек, архитектура и т.п. в конкретном проекте)

Оба файла загружаются при старте сессии и соединяются — не заменяют друг друга.

