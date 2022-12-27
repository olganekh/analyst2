from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(User_verification)
class User_verificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'activating_bot', 'name')
    pass


@admin.register(Purpose)
class PurposeAdmin(admin.ModelAdmin):
    list_display = ['machine', 'apartment', 'vacation',  'another_target']
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['price']
    pass


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['income']
    pass


@admin.register(Data_purchase)
class Data_purchaseAdmin(admin.ModelAdmin):
    list_display = ['data_purchase']
    pass


@admin.register(Result)
class ResulteAdmin(admin.ModelAdmin):
    list_display = ['result']
    pass
