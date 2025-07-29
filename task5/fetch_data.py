import requests

# Адрес API для запросов
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Отправляем GET-запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        print("Статус-код ответа:", response.status_code)

        # Распечатываем содержимое ответа в формате JSON
        data = response.json()
        print("\nПолученные данные:")
        for key, value in data.items():
            print(f"{key}: {value}")

    else:
        print("Ошибка при выполнении запроса. Статус-код:", response.status_code)
except Exception as e:
    print("Произошла ошибка:", str(e))