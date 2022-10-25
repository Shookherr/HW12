from json import load, dump, JSONDecodeError


def load_data_from_json(path):
    """
    Возвращает все данные из файла json
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:     # открытие файла
            data = load(file)                               # загрузка данных
    except FileNotFoundError:
        print(f'ERROR: Not file {path} found.')
        return None
    except JSONDecodeError:
        print(f'ERROR: File {path} not JSON format.')
        return None
    else:
        return data


def save_data_to_json(path, data):
    """
    Запись данных в файл json
    """
    with open(path, 'w', encoding='utf-8') as file:
        dump(data, file)
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
    ext = ext[-1].lower()

    if ext in ['bmp', 'jpg', 'jpeg', 'png']:
        pict.save(f'./uploads/images/{name}')
        return f'uploads/images/{name}'
    else:
        return None


def save_post(post, posts, path):
    """
    Сохранение нового поста
    """
    posts.append(post)

    save_data_to_json(path, posts)

    return posts

