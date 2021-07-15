from django.contrib import admin
from .models import Wallet, Category, Income, Expense


# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'cash']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['category', 'wallet', 'amount', 'date']


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['category', 'wallet', 'amount', 'date']


admin.site.register(Category)
