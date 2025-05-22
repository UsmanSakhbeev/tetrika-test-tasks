# Тестовые задания для компании «Тетрика»

Репозиторий содержит решения трёх независимых задач, выполненных в рамках технического отбора. Каждая задача располагается в собственной директории вместе с условием реализацией и тестами.

---

## Структура проекта

```
.
├── pyproject.toml        # метаданные проекта
├── requirements.txt      # зафиксированные зависимости
├── README.md             # данное описание
├── task1/ ─ task3/       # решения задач
│   ├── taskX.md          # формулировка
│   ├── solution.py       # решение
│   └── tests/            # pytest‑тесты
└── ...
```

---

## Требования

* **Python ≥ 3.9**

---

## Быстрый старт

1. **Склонировать** репозиторий:

   ```bash
   git clone https://github.com/UsmanSakhbeev/tetrika-test-tasks
   cd tetrika-test-tasks
   ```
2. **Создать и активировать** виртуальное окружение (рекомендуется):

   ```bash
   python -m venv venv         # python3 на Linux/macOS
   source venv/bin/activate    # Windows: venv\Scripts\activate
   ```
3. **Установить зависимости**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Запустить автотесты** и убедиться, что всё работает:

   ```bash
   pytest -q
   ```

---
