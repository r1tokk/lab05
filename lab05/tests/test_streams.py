import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from collections.abc import Iterator

from streams import (
    cumulative_sums,
    drop,
    fib_stream,
    moving_average,
    sliding_window,
    take,
)


def test_fib_stream() -> None:
    """Перевірка перших значень стріму Фібоначчі."""
    assert take(10, fib_stream()) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_take_drop() -> None:
    """Перевірка роботи конвеєра drop + take."""
    stream = fib_stream()
    dropped = drop(5, stream)
    assert take(3, dropped) == [5, 8, 13]


def test_sliding_window_basic() -> None:
    """Перевірка формування вікон на простому списку."""
    xs = [1, 2, 3, 4, 5]
    windows = list(sliding_window(xs, 3))
    assert windows == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]


def test_sliding_window_edge_cases() -> None:
    """Перевірка граничних випадків для вікон."""

    assert list(sliding_window([], 3)) == []

    assert list(sliding_window([1, 2], 3)) == []

    assert list(sliding_window([1, 2, 3], 0)) == []
    assert list(sliding_window([1, 2, 3], -1)) == []


def test_moving_average() -> None:
    """Перевірка обчислення рухомого середнього."""
    xs = [2, 4, 6, 8]

    assert list(moving_average(xs, 2)) == [3.0, 5.0, 7.0]


def test_cumulative_sums() -> None:
    """Перевірка префіксних сум."""
    assert list(cumulative_sums([1, 2, 3, 4])) == [1, 3, 6, 10]


def test_laziness() -> None:
    """Тест на підтвердження лінивості (не матеріалізує зайве)."""
    counter = 0

    def mock_stream() -> Iterator[int]:
        nonlocal counter
        while True:
            counter += 1
            yield counter

    stream = mock_stream()

    take(5, stream)
    assert counter == 5

    stream2 = mock_stream()
    counter = 0
    list(take(2, sliding_window(stream2, 3)))
    assert counter == 4
