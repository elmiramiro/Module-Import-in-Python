import random
from datetime import datetime

# Генерация случайного числа от 1 до 100
random_number = random.randint(1, 100)

# Получение текущей даты и времени
current_date_time = datetime.now()

# Вывод результата
print("Случайное число:", random_number)
print("Текущая дата и время:", current_date_time.strftime("%Y-%m-%d %H:%M:%S"))