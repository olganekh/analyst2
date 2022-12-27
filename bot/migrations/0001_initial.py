# Generated by Django 4.1.4 on 2022-12-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_verification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50, verbose_name='ID пользователя из телеграма')),
                ('activating_bot', models.CharField(max_length=50, verbose_name='Активация бота: True - есть цели, False - нет целей')),
            ],
        ),
    ]