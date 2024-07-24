import timeit
import random
import pandas as pd
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from tim_sort import tim_sort

# Створимо функції для вимірювання часу виконання алгоритмів
def measure_time(func, arr):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}({arr})"
    times = timeit.repeat(stmt, setup=setup_code, repeat=3, number=10)
    return min(times)

# Генеруємо набори даних для тестування
def generate_test_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

def main():
    # Розміри масивів для тестування
    sizes = [10, 100, 1000, 10000, 50000]

    # Збираємо результати
    results = {"Sizes": sizes, "MergeSort": [], "InsertionSort": [], "Timsort": []}

    for size in sizes:
        data = generate_test_data(size)
        
        merge_sort_time = measure_time(merge_sort, data.copy())
        insertion_sort_time = measure_time(insertion_sort, data.copy())
        tim_sort_time = measure_time(tim_sort, data.copy())

        results["MergeSort"].append(merge_sort_time)
        results["InsertionSort"].append(insertion_sort_time)
        results["Timsort"].append(tim_sort_time)

    # Виводимо результати
    df = pd.DataFrame(results)
    print(df.to_markdown(index=False))

if __name__ == "__main__":
    main()