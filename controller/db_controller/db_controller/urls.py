
from django.contrib import admin
from django.urls import path
from service.views import index
from service.views import get_records
from service.views import add_records

urlpatterns = [
    path("admin/", admin.site.urls),
    # проверочная страница
    path('', index, name='index'),
    # получение записей на определенный день
    path('record/get/<str:day>', get_records, name='get_records'),
    # добавить запись
    path('record/add/<str:day>/<str:value>', add_records, name='add_records'),

]
