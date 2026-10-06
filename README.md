# Практикум по Python: Эрик Мэтиз и лекции МФТИ (Т. Хирьянов)

Практический дневник изучения Python: решения упражнений по книге, код и конспекты лекций.
Цель — пройти путь от базового синтаксиса до инженерного уровня: чистый код,
архитектура, тестирование, культура работы с git.

Два независимых блока:

1. **Книга:** Эрик Мэтиз, *«Изучаем Python»* (*Python Crash Course*) — задачи по главам.
2. **Курс МФТИ:** *«Практика программирования на Python 3»* (2020), лектор Тимофей Хирьянов —
   [плейлист на YouTube](https://www.youtube.com/playlist?list=PLRDzFCPr95fIDJUvFxvzWxg-V9BmZlMMe).

## Прогресс

| Блок | Сделано | Дальше |
|------|---------|--------|
| Мэтиз | главы 2–8 | главы 9–11: классы, файлы и исключения, тестирование |
| МФТИ | лекции 1–5 | лекция 6 |

## Структура репозитория

```text
.
├── 01_python_crash_course_eric_matthes/
│   ├── chapter_02_variables_and_simple_data_types/
│   ├── chapter_03_introducing_lists/
│   ├── chapter_04_working_with_lists/
│   ├── chapter_05_if_statements/
│   ├── chapter_06_dictionaries/
│   ├── chapter_07_user_input_and_while_loops/
│   └── chapter_08_functions/               # в каждой главе: примеры + exercise/
├── 02_mfti_khiryanov_lectures/
│   ├── lecture1/    # 01_loops.py, 02_nested_for.py
│   ├── lecture2/    # 03_gold_found_inPython.py, 04_function.py, 05_tuple.py
│   ├── lecture3/    # 06_set_and_dict.py, 07_function_locality_of_names.py
│   ├── lecture4/
│   └── lecture5/    # NOTES.md, house.py — декомпозиция и top-down проектирование
├── 03_extras/
│   ├── side_files/  # лямбда-функции и вспомогательные скрипты
│   └── zen_python/  # эксперименты с PEP 20
├── docs/
│   └── SOURCES.md   # источники для изучения до уровня Senior
├── .gitignore
├── README.md
└── requirements.txt
```

## Что внутри

### Блок 1. Эрик Мэтиз

| Глава | Темы |
|-------|------|
| 2 | строки, f-строки, регистр (`title()`, `lower()`), числа, `strip()` |
| 3 | индексация списков, `append/insert/pop/remove`, `sort/sorted/reverse` |
| 4 | цикл `for`, `range()`, `min/max/sum`, срезы, генераторы списков |
| 5 | булева логика, `in / not in`, `if-elif-else` |
| 6 | словари, вложенные структуры, `keys/values/items`, `get()` |
| 7 | `input()`, `while`, флаги, `break` / `continue`, заполнение словарей вводом |
| 8 | функции, позиционные и именованные аргументы, `return`, `*args`, `**kwargs` |

### Блок 2. Лекции МФТИ (Т. Хирьянов)

| Лекция | Темы |
|--------|------|
| 1 | циклы, логические условия, вложенные циклы |
| 2 | алгоритмы поиска, функции, области видимости, кортежи |
| 3 | множества и словари (хеш-таблицы), локальность имён |
| 5 | декомпозиция, top-down проектирование, консистентные состояния, docstring-контракты, атомарные коммиты |

### Ключевые идеи лекции 5

- **Декомпозиция сверху вниз:** сначала интерфейс (`draw_house(...)`), потом подпрограммы.
- **Всегда рабочий код:** на промежуточных этапах функции-заглушки (`pass` / `print()`).
- **Борьба с «призраками»:** опорные точки, единицы и системы координат описаны в docstring до написания тела функции.
- **Атомарные коммиты:** один коммит — один законченный логический шаг, без «сломанных» состояний.

Подробнее: [`lecture5/NOTES.md`](02_mfti_khiryanov_lectures/lecture5/NOTES.md).

## Установка и запуск (Manjaro / Arch)

```bash
sudo pacman -S --needed git python python-pip
git clone https://github.com/Ramazan101/python-foundations-matthes-mipt.git
cd python-foundations-matthes-mipt

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt     # если в нём нет pygame: pip install pygame
```

В Arch/Manjaro системный `pip` защищён (PEP 668), поэтому зависимости ставятся только в виртуальное окружение.

Запуск скриптов:

```bash
# Мэтиз
python 01_python_crash_course_eric_matthes/chapter_08_functions/formatted_name.py

# МФТИ
python 02_mfti_khiryanov_lectures/lecture1/01_loops.py
python 02_mfti_khiryanov_lectures/lecture5/house.py
```

## Окружение

- Python 3.12+
- Manjaro Linux (Wayland / Hyprland)
- PyCharm Professional
- Стиль кода: PEP 8, docstrings по PEP 257

## Roadmap до уровня Senior

- [x] Базовый синтаксис, управляющие конструкции, функции
- [x] Структуры данных: списки, словари, множества, кортежи
- [x] Процедурная декомпозиция и top-down проектирование (лекция 5)
- [ ] ООП: классы, наследование, dunder-методы, dataclasses
- [ ] Файлы, исключения, тестирование (`pytest`)
- [ ] Алгоритмы и структуры данных: сложность, рекурсия, сортировки, графы, ДП
- [ ] Типизация (`typing`, `mypy`), линтеры (`ruff` / `flake8`), форматирование (`black`)
- [ ] Модель данных Python и внутреннее устройство CPython (GIL, память, байт-код)
- [ ] Асинхронность: `asyncio`, потоки, процессы
- [ ] Архитектура: SOLID, паттерны, чистая архитектура
- [ ] Инфраструктура: Docker, CI/CD (GitHub Actions), PostgreSQL, SQLAlchemy

Список источников для каждого пункта: [`docs/SOURCES.md`](docs/SOURCES.md).
