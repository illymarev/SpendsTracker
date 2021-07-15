from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm, ExpenseForm
from .models import Wallet
import datetime


# Create your views here.
def display_wallets(request):
    if request.user.is_authenticated:
        wallets = Wallet.objects.filter(user=request.user)
    else:
        wallets = None

    context = {
        'wallets': wallets,
    }
    return render(request, 'wallets/display_wallets.html', context)


@login_required
def create_new_wallet(request):
    if request.method == "POST":
        name = request.POST.get('name')
        wallet = Wallet.objects.create(name=name, user=request.user)
        wallet.save()
        return redirect(reverse('display_wallets'))
    return render(request, 'wallets/create_new_wallet.html')


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST, user=request.user)
        if form.is_valid():
            income = form.cleaned_data.get('amount')
            wallet_name = form.cleaned_data.get('wallet')
            form.save()
            wallet = Wallet.objects.get(user=request.user, name=wallet_name)
            wallet.cash += income
            wallet.save()
            return redirect(reverse('display_wallets'))
    else:
        form = IncomeForm(user=request.user)

    context = {
        'form': form,
    }

    return render(request, 'wallets/add_income.html', context)


@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user)
        if form.is_valid():
            expense = form.cleaned_data.get('amount')
            wallet_name = form.cleaned_data.get('wallet')
            form.save()
            wallet = Wallet.objects.get(user=request.user, name=wallet_name)
            wallet.cash -= expense
            wallet.save()
            return redirect(reverse('display_wallets'))
    else:
        form = ExpenseForm(user=request.user)

    context = {
        'form': form,
    }

    return render(request, 'wallets/add_expense.html', context)


@login_required
def month_detailed_expenses(request, pk):
    wallet = Wallet.objects.get(id=pk)
    context = {
        'wallet': wallet,
    }
    return render(request, 'wallets/detailed_expenses.html', context)


@login_required
def month_detailed_income(request, pk):
    wallet = Wallet.objects.get(id=pk)
    context = {
        'wallet': wallet,
    }
    return render(request, 'wallets/detailed_income.html', context)


@login_required
def wallet_details(request, pk):
    wallet = Wallet.objects.get(id=pk)
    if request.method == "POST":
        month = request.POST.get('month')
        year = datetime.datetime.now().year
        if int(month) == 13:
            wallet_income = wallet.income_set.all()
            wallet_expense = wallet.expense_set.all()
        else:
            wallet_income = wallet.income_set.filter(date__month=int(month), date__year=int(year))
            wallet_expense = wallet.expense_set.filter(date__month=int(month), date__year=int(year))
    else:
        wallet_income = wallet.income_set.all()
        wallet_expense = wallet.expense_set.all()
    context = {
        'wallet': wallet,
        'wallet_income': wallet_income,
        'wallet_expense': wallet_expense,
    }
    return render(request, 'wallets/wallet_details.html', context)


@login_required
def delete_wallet(request, pk):
    wallet = Wallet.objects.get(id=pk)
    if request.method == "POST":
        wallet.delete()
        return redirect(reverse('display_wallets'))
    context = {
        'wallet': wallet,
    }
    return render(request, 'wallets/delete_wallet.html', context)
