from django import forms
from datetime import datetime


class Budget(forms.Form):
    text = forms.CharField(max_length=255, label="عنوان", required=False)
    amount = forms.IntegerField(label="مقدار", required=False)
    date = forms.DateField(label="تاریخ", required=False,
                           initial=datetime.now)
    description = forms.CharField(
        max_length=255, label="توضیحات", required=False)
