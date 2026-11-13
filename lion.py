from collections import Counter
import docx
import pandas as pd
import matplotlib.pyplot as plt
doc = docx.Document('lion.docx') # Читает файл и сразу переводим все буквы в маленькие
text = ' '.join([p.text for p in doc.paragraphs]).lower() # склеиваем все строки в одну большую, разделяя их пробелами и делаем все буквы маленькими
znaki = '.,!?;:"()[]{}«»—–-' # Убираем знаки препинания
for z in znaki: # меням все знаки на пробелы
    text = text.replace(z, ' ')
slova = text.split() # Считаем слова
ss = Counter(slova) # считаем сколько раз повторяются слова
vsego_slov = len(slova)
tablica = [] # Готовим данные для таблицы (округляем проценты до 2 знаков)
for slovo, kol in ss.most_common():
    procent = round((kol / vsego_slov) * 100, 2) # считаем процент
    tablica.append([slovo, kol, procent])
df = pd.DataFrame(tablica, columns=['Слово', 'Частота встречи, раз', 'Частота встречи в %']) # Сохраняем в Excel с точными названиями столбцов из задания
df.to_excel('slova.xlsx', index=False)
a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
buk = [b for b in text if b in a] #  оставляем только русские буквы
sb = Counter(buk) # считаем сколько раз повторяются буквы
plt.bar(sb.keys(), sb.values()) # Рисуем график
plt.xlabel('Буквы')
plt.ylabel('Количество')
plt.show()