"""Лекция 5 (МФТИ, Т. Хирьянов): декомпозиция «сверху вниз».

Каркас функции draw_house(): сначала контракт (docstring), потом реализация.
Пока вместо графики — print(): программа всегда запускается
(консистентное состояние), а параметры можно «прозвонить» глазами.
Когда интерфейсы проверены, print() заменяется вызовами pygame.draw.*.
"""

ROOF_SHARE = 0.3        # доля высоты дома, занятая крышей
FOUNDATION_SHARE = 0.1  # доля высоты дома, занятая фундаментом


def draw_foundation(x: float, y: float, width: float, height: float) -> None:
    """Нарисовать фундамент.

    Опорная точка (x, y) — левый верхний угол фундамента.
    Ось y направлена вниз (как в Pygame). Размеры — в пикселях.
    """
    print(f"draw_foundation: {x=}, {y=}, {width=}, {height=}")


def draw_walls(x: float, y: float, width: float, height: float) -> None:
    """Нарисовать стены. Опорная точка (x, y) — левый верхний угол стен."""
    print(f"draw_walls: {x=}, {y=}, {width=}, {height=}")


def draw_roof(x: float, y: float, width: float, height: float) -> None:
    """Нарисовать крышу. Опорная точка (x, y) — левый верхний угол
    прямоугольника, в который вписан треугольник крыши."""
    print(f"draw_roof: {x=}, {y=}, {width=}, {height=}")


def draw_house(x: float, y: float, width: float, height: float) -> None:
    """Нарисовать дом целиком.

    Опорная точка (x, y) — левый верхний угол прямоугольника,
    описанного вокруг всего дома (крыша + стены + фундамент).
    Ось y направлена вниз. Размеры — в пикселях.
    Пропорции по высоте: крыша 30 %, фундамент 10 %, остальное — стены.
    """
    roof_height = height * ROOF_SHARE
    foundation_height = height * FOUNDATION_SHARE
    walls_height = height - roof_height - foundation_height

    draw_roof(x, y, width, roof_height)
    draw_walls(x, y + roof_height, width, walls_height)
    draw_foundation(x, y + roof_height + walls_height, width, foundation_height)


if __name__ == "__main__":
    draw_house(x=100, y=50, width=200, height=300)
