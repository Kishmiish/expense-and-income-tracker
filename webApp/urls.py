from django.urls import re_path, path
from webApp import views

urlpatterns = [
    re_path(r'^submit/expense/$', views.submit_expense),
    re_path(r'^submit/income/$', views.submit_income),
    re_path(r'^/$', views.view_budget),
    re_path(r'^expenses/all/$', views.all_expenses),
    re_path(r'^incomes/all/$', views.all_incomes),
]
