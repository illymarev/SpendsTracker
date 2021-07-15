from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cash = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def this_month_expenses_detailed(self):
        now = datetime.datetime.now()
        month_now = now.month
        year_now = now.year
        return self.expense_set.filter(date__month=month_now, date__year=year_now)

    def this_month_expenses(self):
        overall = 0
        for i in self.this_month_expenses_detailed():
            overall += i.amount
        return overall

    def this_month_income_detailed(self):
        now = datetime.datetime.now()
        month_now = now.month
        year_now = now.year
        return self.income_set.filter(date__month=month_now, date__year=year_now)

    def this_month_income(self):
        overall = 0
        for i in self.this_month_income_detailed():
            overall += i.amount
        return overall

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_income = models.BooleanField()  # If income = False - then it is a category for expenses, if True - for income.

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Expense(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Income(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField()
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
