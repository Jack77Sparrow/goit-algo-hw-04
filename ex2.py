from pathlib import Path



def get_cats_info(path: Path):
    """
    Читає файл з даними про котів та повертає список словників.

    Параметри:
        path (Path): шлях до текстового файлу з котами.
                    Формат: id,ім'я,вік

    Повертає:
        list[dict[str, str]] або повідомлення про помилку.
    """
    cats = []

    try:
        # відкриваємо файл у режимі читання
        with open(path, 'r', encoding='utf-8') as file:
            raw_lines = file.readlines()
    except FileNotFoundError as e:
        return f"File {path.name} not found: {e}"
    except OSError as e:
        return f"Error reading file {path.name}: {e}"
    
    # перевіряємо чи файл не порожній
    if not raw_lines or all(not line.strip() for line in raw_lines):
        return []

    # формуємо список словників з даних файлу
    for line in raw_lines:
        try:
            cat_id, cat_name, cat_age = line.strip().split(',')
            cats.append({'id': cat_id, 'name': cat_name, 'age': cat_age})
        except ValueError:
            continue  # пропускаємо некоректні рядки
    
    return cats


# приклад використання
path_to_cats = Path(__file__).parent
cats_info = get_cats_info(path_to_cats / 'data/cats_ex2.txt')
print(cats_info)