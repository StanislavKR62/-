from django.db import models

# Модель для работы с записями БД
class Records (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField (max_length=250)
    day = models.CharField(max_length=12)