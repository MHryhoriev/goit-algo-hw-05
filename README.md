# Висновки щодо продуктивності алгоритмів пошуку

## 1. Час виконання для статті 1 з існуючим пошуковим шаблоном:
- **Rabin-Karp:** 0.034021 сек.
- **Knuth-Morris-Pratt:** 0.018770 сек.
- **Boyer-Moore:** 0.009349 сек.

## 2. Час виконання для статті 1 з не існуючим пошуковим шаблоном:
- **Rabin-Karp:** 0.033349 сек.
- **Knuth-Morris-Pratt:** 0.017935 сек.
- **Boyer-Moore:** 0.008812 сек.

## 3. Час виконання для статті 2 з існуючим пошуковим шаблоном:
- **Rabin-Karp:** 0.015003 сек.
- **Knuth-Morris-Pratt:** 0.010668 сек.
- **Boyer-Moore:** 0.009414 сек.

## 4. Час виконання для статті 2 з не існуючим пошуковим шаблоном:
- **Rabin-Karp:** 0.038756 сек.
- **Knuth-Morris-Pratt:** 0.028942 сек.
- **Boyer-Moore:** 0.009176 сек.

## Основні висновки:
- **Алгоритм Боєра-Мура** показав **найшвидший час виконання** в усіх тестах, як для існуючих, так і для відсутніх пошукових шаблонів. Це пояснюється його ефективною роботою з довгими рядками та частими стрибками при невідповідностях.
  
- **Алгоритм Кнута-Морріса-Пратта** стабільно працював швидше, ніж Рабіна-Карпа, але поступався Boyer-Moore. Його перевага полягає в передобчисленні підрядка, що зменшує кількість порівнянь.
  
- **Алгоритм Рабіна-Карпа** був **найповільнішим** серед трьох, особливо для статті 2 з відсутнім шаблоном. Алгоритм добре підходить для випадків, коли хеші збігаються, але його продуктивність може страждати через багаторазові перерахунки хеш-значень.
  
- Для коротших або менших текстів усі три алгоритми працюють відносно швидко. Проте зростання розміру тексту та частота невідповідностей може впливати на продуктивність, особливо для алгоритму Rabin-Karp.