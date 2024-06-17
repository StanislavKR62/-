"""
URL configuration for task_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from service.views import index
from service.views import get_all
from service.views import add_task

urlpatterns = [
    path("admin/", admin.site.urls),
    # проверочная страница
    path('', index, name='index'),

    # получение всех задач на дату
    path("task/get_all", get_all),
    # получение всех задач на дату
    path("task/add/<str:title>", add_task),

    #path("user/register/<str:name>/<str:surname>/<int:old>/<str:sex>/<str:hobby>/<str:sity>/<str:password>", views.register),
    # user/get/{id}
    #path("user/get/<int:id>", views.getuser),
]
