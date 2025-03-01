import requests
import json


# Функция для чтения токена из файла config.json
def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config.get("token")


# Функция для получения информации о пользователе
def get_user_info(token):
    url = "https://gitlab.skillbox.ru/api/v4/user"
    headers = {
        "PRIVATE-TOKEN": token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при обращении к API: {response.status_code} - {response.text}")


# Функция для сохранения информации о пользователе в файл
def save_user_info_to_file(user_info, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Информация о пользователе:\n\n")
        file.write(f"ID: {user_info['id']}\n")
        file.write(f"Имя: {user_info['name']}\n")
        file.write(f"Username: {user_info['username']}\n")
        file.write(f"Email: {user_info.get('email', 'Нет данных')}\n")
        file.write(f"Ссылка: {user_info['web_url']}\n")
        file.write(f"Создан: {user_info['created_at']}\n")
        file.write(f"Обновлен: {user_info['last_sign_in_at']}\n")
        file.write(f"Текущие роли: {', '.join(user_info.get('roles', []))}\n")
        file.write("\n--- Конец информации ---\n")


# Основная логика программы
def main():
    token = read_token_from_file('config.json')

    try:
        user_info = get_user_info(token)
        save_user_info_to_file(user_info, 'user_info.txt')
        print("Информация о пользователе успешно сохранена в user_info.txt")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()