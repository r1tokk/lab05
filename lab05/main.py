from streams import (
    cumulative_sums,
    drop,
    fib_stream,
    moving_average,
    sliding_window,
    take,
)


def main() -> None:
    print("Демонстрація лінивих обчислень (Варіант 1)")

    print("Пропустити перші 5 чисел Фібоначчі і взяти 10:")
    stream = fib_stream()
    dropped = drop(5, stream)
    result_1 = take(10, dropped)
    print(f"Результат: {result_1}\n")

    print("Ковзні вікна (k=3) для наступних 5 чисел Фібоначчі:")
    stream2 = fib_stream()
    windows = sliding_window(stream2, 3)
    result_2 = take(5, windows)
    for w in result_2:
        print(f"  {w}")
    print()

    print("Рухоме середнє (k=3) для наступних 5 чисел Фібоначчі:")
    stream3 = fib_stream()
    m_avg = moving_average(stream3, 3)
    result_3 = take(5, m_avg)
    for avg in result_3:
        print(f"  {avg:.2f}")
    print()

    print("Префіксні суми перших 8 чисел Фібоначчі:")
    stream4 = fib_stream()
    sums = cumulative_sums(stream4)
    result_4 = take(8, sums)
    print(f"Результат: {result_4}")


if __name__ == "__main__":
    main()
