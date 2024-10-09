from django.urls import re_path, path
from webApp import views

urlpatterns = [
    re_path(r'^submit/expense/$', views.submit_expense),
    re_path(r'^submit/income/$', views.submit_income),
    re_path(r'^budget/$', views.view_budget),
]
