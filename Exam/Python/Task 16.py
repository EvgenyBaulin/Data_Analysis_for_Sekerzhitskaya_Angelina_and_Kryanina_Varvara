# Исходные данные
T_real = [13, 4, 5, 7, 6, 5, 81]
T_predicted = [12, 4, 4, 8, 6, 4, 7]

# Вычисление средней абсолютной ошибки (MAE)
n = len(T_real)
mae = sum(abs(T_real[i] - T_predicted[i]) for i in range(n)) / n

# Вывод результата с округлением до сотых долей
print(round(mae, 2))
