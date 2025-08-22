from pathlib import Path

def total_salary(path: Path):
    '''
    Обчислює середню та загальну суму заробітної плати в викляді кортежу

    Параметри:
    path: Path -> шлях до файлу з заробітними платами

    Повертає:
    tuple: Кортеж з загальною та середньою сумою зарплат
    '''
    total_salary = 0
    
    #ловимо виключення коли ми не можемо знайти даний файл
    try:
        # відкриваємо файл в режимі читання
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        return f'File {path.name} not found, exception {e}'
    except OSError as e:
        return f'Error reading file {path.name}: {e}'
    
    # перевіряємо чи файл не пустий
    if not lines:
        return f"File is empty"

    # ітеруємось по списку з даними 
    for item in lines:

        try:
            money = item.strip().split(',')[1]
            # обчислюємо загальгу зарплату для всіх робітників
            total_salary += int(money)
        except (ValueError, IndexError):
            # Пропускаємо не коректні рядки
            continue
    
    # обчислюємо середню заробітню плату
    try:

        average_salary = total_salary/len(lines)
    except ZeroDivisionError:
        print('не можна ділити на 0')


    return total_salary, average_salary



path = Path(__file__).parent
salary = total_salary(path / 'data/salary_ex1'
'.txt')
print(salary)