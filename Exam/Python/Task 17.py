import numpy as np

# Данные
T_prep = np.array([6, 5, 6, 1, 6, 8, 9])
Grade = np.array([19, 9, 10, 7, 8, 10, 101])

# Вычисление средних значений
mean_T_prep = np.mean(T_prep)
mean_Grade = np.mean(Grade)

# Вычисление выборочного коэффициента корреляции Пирсона
numerator = np.sum((T_prep - mean_T_prep) * (Grade - mean_Grade))
denominator_T_prep = np.sqrt(np.sum((T_prep - mean_T_prep) ** 2))
denominator_Grade = np.sqrt(np.sum((Grade - mean_Grade) ** 2))

correlation_coefficient = numerator / (denominator_T_prep * denominator_Grade)

# Округление ответа до сотых
correlation_coefficient_rounded = round(correlation_coefficient, 2)

print(correlation_coefficient_rounded)
