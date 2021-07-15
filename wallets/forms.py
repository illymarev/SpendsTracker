from django import forms
from .models import Income, Expense, Category, Wallet


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['category', 'wallet', 'amount', 'comment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(is_income=True)
        self.fields['wallet'].queryset = Wallet.objects.filter(user=user)


class ExpenseForm(forms.ModelForm):
    trans_from = forms.ModelMultipleChoiceField
    class Meta:
        model = Expense
        fields = ['category', 'wallet', 'amount', 'comment']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(is_income=False)
        self.fields['wallet'].queryset = Wallet.objects.filter(user=user)