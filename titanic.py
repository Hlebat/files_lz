import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_parquet('titanic.parquet')
data.to_csv('titanic.csv', index=False) # сохраняем эту таблицу в titanic.csv
print("Файл сохранен в формат CSV.")
data_csv = pd.read_csv('titanic.csv')
t = data_csv.groupby(['Pclass', 'Survived']).size().unstack() # группируем по классу и статусу
t.columns = ['Не выжил', 'Выжил']
t.plot(kind='bar', color=['red', 'green']) # Красный для погибших, зеленый для выживших
plt.title('Выживаемость пассажиров Титаника в зависимости от класса билета') # Подпись и вывод графика
plt.xlabel('Класс билета')
plt.ylabel('Количество пассажиров')
plt.xticks(rotation=0) # Чтобы цифры классов (1, 2, 3) стояли ровно
plt.legend(title='Статус')
plt.show()