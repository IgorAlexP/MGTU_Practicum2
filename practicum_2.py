import pandas as pd
from sqlalchemy import create_engine

# Создание подключения к базе данных SQLite
engine = create_engine('sqlite:///mydatabase.db') 

# Загрузка исходных данных из файла Excel
raw_data = pd.read_excel('C:\\Users\\clic\\OneDrive\\Рабочий стол\\Study\\MGTU2\\data2.xlsx')

# Добавляем префикс к именам столбцов
prefix = 'dwh_'
raw_data.columns = [prefix + col for col in raw_data.columns]

# Сохраняем данные в стейджинговой таблице
staging_table_name = 'staging_table'
raw_data.to_sql(staging_table_name, engine, if_exists='replace', index=False)

# Читаем данные из таблицы
result_data = pd.read_sql(f'SELECT * FROM {staging_table_name}', con=engine)

print(result_data)