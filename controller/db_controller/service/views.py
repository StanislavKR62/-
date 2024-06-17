from django.shortcuts import render
from django.http import HttpResponse
import service.db_func as db_func
import json
# проверочная функция
def index(requets):
    return HttpResponse("<h1>Сервис контроллера данных</h1>")

# функция получения записей
def get_records(requets, day):
    result = db_func.get_records(day)
    return HttpResponse(json.dumps(result))

# функция добавления записей
def add_records(requets, day, value):
    result = db_func.add_records(day,value)
    print('day', day)
    return HttpResponse(result)
