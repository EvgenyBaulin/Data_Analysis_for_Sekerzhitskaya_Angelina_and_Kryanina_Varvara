# Исходные данные
T_heat = [1, 6, 8, 9]
Dur_sleep = [7, 8, 10, 10]

# Рассчитываем средние значения
mean_T_heat = sum(T_heat) / len(T_heat)
mean_Dur_sleep = sum(Dur_sleep) / len(Dur_sleep)

# Рассчитываем суммы для оценки коэффициентов
SSX = sum((T - mean_T_heat) ** 2 for T in T_heat)
SP = sum((T_heat[i] - mean_T_heat) * (Dur_sleep[i] - mean_Dur_sleep) for i in range(len(T_heat)))

# Вычисляем коэффициенты
w1 = SP / SSX
w0 = mean_Dur_sleep - w1 * mean_T_heat

# Вывод результатов с округлением до сотых долей
print(round(w0, 2), round(w1, 2))
