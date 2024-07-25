# Порівняльний аналіз алгоритмів сортування

## Опис завдання

Порівняння трьох алгоритмів сортування: злиттям, вставками та Timsort за часом виконання. Аналіз підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних.

## Алгоритми

1. **Merge Sort** - сортування злиттям
2. **Insertion Sort** - сортування вставками
3. **Timsort** - використання вбудованої функції `sorted` в Python

## Результати

|   Sizes |   MergeSort |   InsertionSort |     TimSort |
|--------:|------------:|----------------:|------------:|
|      10 |  4.9459e-05 |     1.18751e-05 | 2.79187e-06 |
|     100 |  0.000769   |     0.000836541 | 2.89169e-05 |
|    1000 |  0.010485   |     0.0989288   | 0.000501917 |
|   10000 |  0.139185   |     9.93467     | 0.00777154  |
|   50000 |  0.784036   |   248.861       | 0.0427542   |

## Висновки

InsertionSort є досить ефективним на невеликих наборах данних, але на масивах більше 1000, показує гірший результат ніж MergeSort.
Timsort є набагато ефективнішим, ніж сортування злиттям або вставками на великих наборах даних. Це підтверджується результатами тестування на різних розмірах масивів. Гібридний підхід Timsort, що поєднує сортування злиттям і вставками, забезпечує високу продуктивність, що робить його оптимальним вибором для вбудованих функцій сортування в Python.