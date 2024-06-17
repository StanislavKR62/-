from django.shortcuts import render
from django.http import HttpResponse
import json
import service.logical_func as logical_func

# проверочная функция
def index(requets):
    return HttpResponse("<h1>Сервис бизнес-логики</h1>")
    
# функция чтения записей на текущий день
def get_all(requets):
    db_task = logical_func.get_all_task()
    return HttpResponse((db_task))

# функция добавления нового упражнения
def add_task(requets, title):
    res = logical_func.add_task(title)
    return HttpResponse(res)