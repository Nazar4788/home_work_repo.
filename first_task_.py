

from datetime import datetime
# Створюємо функцію
def get_days_from_today(date):
    try:
        # Перетворюємо str на datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримуємо поточну дату 
        today_date = datetime.today().date()
        # Різниця в днях
        delta_days = (input_date - today_date).days
        return delta_days
    except ValueError:
        print("Помилка: неправильний формат дати, очікується 'РРРР-ММ-ДД'")
        return None

# Частина коду для самостійного введення дати
date_input = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
result = get_days_from_today(date_input)
if result is not None:
    print(f"Різниця в днях: {result}")