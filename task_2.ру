def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:  # перевірка, щоб упевнитися  чи  рядок містить усі потрібні нам  дані
                    cat_info = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat_info)
                    
    # Обробка винятків і помилок               
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []
    
    return cats_info

# Приклад використання 
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
