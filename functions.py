import json
from json import load


def load_data_from_json(path):
    """
    Возвращает все данные из файла json
    """
    with open(path, 'r', encoding='utf-8') as file:     # открытие файла
        data = load(file)                               # загрузка данных

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


def save_picture(pict):
    """
    Сохранение картинки к посту на диск
    """
    name = pict.filename
    ext = name.split('.')
    ext = ext[-1]

    if ext in ['bmp', 'jpg', 'jpeg', 'png']:
        pict.save(f'./uploads/images/{name}')
        return f'uploads/images/{name}'
    else:
        return


def save_post(post, posts, path):
    """
    Сохранение нового поста
    """
    posts.append(post)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return posts
