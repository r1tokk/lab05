from collections import deque
from collections.abc import Iterable, Iterator
from itertools import accumulate, islice
from typing import TypeVar

T = TypeVar("T")


def fib_stream() -> Iterator[int]:
    """Нескінченний генератор чисел Фібоначчі."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n: int, it: Iterable[T]) -> list[T]:
    """Матеріалізує перші n елементів ітератора у список."""
    return list(islice(it, n))


def drop(n: int, it: Iterable[T]) -> Iterator[T]:
    """Пропускає перші n елементів ітератора."""
    it_iter = iter(it)
    return islice(it_iter, n, None)


def sliding_window(it: Iterable[int], k: int) -> Iterator[tuple[int, ...]]:
    """Формує ковзне вікно розміру k з ітератора (ліниво)."""
    if k <= 0:
        return

    it_iter = iter(it)
    dq: deque[int] = deque(maxlen=k)

    for _ in range(k):
        try:
            dq.append(next(it_iter))
        except StopIteration:
            return  # Якщо елементів менше за k, нічого не віддаємо

    yield tuple(dq)

    for x in it_iter:
        dq.append(x)
        yield tuple(dq)


def moving_average(it: Iterable[int], k: int) -> Iterator[float]:
    """Обчислює рухоме середнє для вікон розміру k."""
    for window in sliding_window(it, k):
        yield sum(window) / k


def cumulative_sums(it: Iterable[int]) -> Iterator[int]:
    """Обчислює префіксні суми потоку (через accumulate)."""
    yield from accumulate(it)
