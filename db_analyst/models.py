from django.db import models
from datetime import datetime


class User_verification(models.Model):
    """Таблица Аутентификации пользователя"""
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(verbose_name='ID пользователя из телеграма')
    name = models.CharField(blank=True, verbose_name='Имя пользователя', max_length=50, )
    activating_bot = models.CharField(max_length=50, verbose_name='Активация бота')
    date = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        verbose_name = 'Аутентификации пользователя'
        verbose_name_plural = 'Аутентификации пользователя'

    def __str__(self):
        return f'@{self.name}' if self.name is not None else f'{self.user_id}'


class Purpose(models.Model):
    """Выбор цели"""
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)
    machine = models.CharField(blank=True, max_length=50, verbose_name='купить машину')
    apartment = models.CharField(blank=True, max_length=50, verbose_name='купить квартиру')
    vacation = models.CharField(blank=True, max_length=50, verbose_name='съездить в отпуск')
    another_target = models.CharField(blank=True, max_length=50, verbose_name='другие траты')

    class Meta:
        verbose_name = 'Цели'
        verbose_name_plural = 'Цели'


    # def str(self):
    #     return f' Расход {self.id} {self.machine} {self.apartment} {self.vacation} {self.things} {self.another_target}

class Price(models.Model):
    """Стоимость"""
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимость'


class Income(models.Model):
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)
    income = models.IntegerField(verbose_name='Доход')

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доход'


class Data_purchase(models.Model):
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)
    data_purchase = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return {self.data_purchase}

    class Meta:
        verbose_name = 'Дата покупки'
        verbose_name_plural = 'Дата покупки'


class Result(models.Model):
    verification = models.ForeignKey('User_verification', on_delete=models.CASCADE, null=True)
    result = models.IntegerField(verbose_name='Итог')

    def __str__(self):
        return {self.result}

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результат'