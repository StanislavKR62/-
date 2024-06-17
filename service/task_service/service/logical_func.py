import requests
import datetime
date = datetime.date.today()
weeks = {
    '1':'Monday',
    '2':'Tuesday',
    '3':'Wednesday',
    '4':'Thursday',
    '5':'Friday',
    '6':'Saturday',
    '7':'Sunday',
    }

# функции бизнес-логики

# Получить перечень упражнений из БД
def get_all_task():
    # определим текущий день недели
    nday = weeks[str(date.isoweekday())]
    # Обратимся к контроллеру БД
    res = requests.get("http://localhost:9000/record/get/"+nday)
    return res

# добавить запись о новом упражнении в БД для текущего дня
def add_task(title):
    # Обратимся к контроллеру БД
    res = requests.get("http://localhost:9000/record/add/"+weeks[str(date.isoweekday())]+"/"+title)
    return True

