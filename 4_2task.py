def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

    return cats


# Виклик:
result = get_cats_info("cats.txt")
print(result)