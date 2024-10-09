from django.shortcuts import render
from webApp.models import Expense, Income
from datetime import datetime
from json import JSONEncoder
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .forms import Budget

# Create your views here.


@csrf_exempt
def submit_expense(request):
    text = request.POST['text']
    if 'date' not in request.POST or request.POST['date'] == "":
        date = datetime.now()
    else:
        date = request.POST['date']
    amount = request.POST['amount']
    description = request.POST['description']
    Expense.objects.create(date=date, amount=amount,
                           description=description, text=text)
    return HttpResponseRedirect('/budget/')


@csrf_exempt
def submit_income(request):
    text = request.POST['text']
    if 'date' not in request.POST or request.POST['date'] == "":
        date = datetime.now()
    else:
        date = request.POST['date']
    amount = request.POST['amount']
    description = request.POST['description']
    Income.objects.create(date=date, amount=amount,
                          description=description, text=text)
    return HttpResponseRedirect('/budget/')


def view_budget(request):
    form = Budget(request.POST)
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    template = loader.get_template('register.html')
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'form': form,
    }
    return HttpResponse(template.render(context, request))
