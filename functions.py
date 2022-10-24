import json


def load_data_from_json(path):
    """
    Возвращает все данные из файла json
    """
    with open(path, 'r', encoding='utf-8') as file:     # открытие файла
        data = json.load(file)                          # загрузка данных

    return data


def search_posts(str_, posts):
    """
    Поиск постов по наличию строки str_ в поле "content"
    """
    # Инициализация пустого словаря
    subposts = []

    for post in posts:
        if str_.lower() in post["content"].lower():
            subposts.append(post)
            continue

    return subposts
