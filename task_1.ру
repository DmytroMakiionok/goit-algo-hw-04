def total_salary(path):
    total_salary_sum = 0
    num_developers = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:  # перевірка, щоб упевнитися, що рядок містить прізвище та зарплату
                    salary = int(parts[1])
                    total_salary_sum += salary
                    num_developers += 1
    # Обробка винятків і помилок               
    except FileNotFoundError: 
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None
    
    if num_developers == 0:
        print("Файл порожній або не містить правильних даних.")
        return None, None
    
    average_salary =int(total_salary_sum / num_developers)
    return total_salary_sum, average_salary

# Приклад використання 
total, average = total_salary("salary_file.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
