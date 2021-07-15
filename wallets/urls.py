from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_wallets, name='display_wallets'),
    path('create_new_wallet', views.create_new_wallet, name='create_new_wallet'),
    path('add_income', views.add_income, name='add_income'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('this_month_expenses_detailed/<int:pk>', views.month_detailed_expenses, name='month_detailed_expenses'),
    path('this_month_income_detailed/<int:pk>', views.month_detailed_income, name='month_detailed_income'),
    path('wallet_details/<int:pk>', views.wallet_details, name='wallet_details'),
    path('delete_wallet/<int:pk>', views.delete_wallet, name='delete_wallet')
]
