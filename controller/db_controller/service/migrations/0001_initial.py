# Generated by Django 5.0.6 on 2024-06-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Records",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=250)),
                ("day", models.CharField(max_length=12)),
            ],
        ),
    ]
