import pandas as pd
import numpy as np

# Создаем "грязный" набор данных
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eve', 'Grace', 'Hannah', 'John', 'Mike', np.nan],
    'Age': [25, 30, np.nan, 22, 35, 40, 25, np.nan, 29, 33],
    'Salary': [50000, 60000, 55000, 45000, np.nan, 70000, 65000, 48000, 72000, 50000],
}

df = pd.DataFrame(data)

# Сохраняем в CSV, чтобы проверить, как это выглядит
df.to_csv('dirty_data.csv', index=False)

# Выводим набор данных
print("Изначальные данные:")
print(df)
