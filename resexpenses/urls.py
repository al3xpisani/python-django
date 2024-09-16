from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="resexpenses"),
    path('add-expense', views.add_expense, name="add_expenses")
]