# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea

from .models import Record

class RecordForm(ModelForm):
    class Meta:  # todo: Meta 클래스는 어떤 역할을 할까??
        model = Record # specify which model to use
        fields = ['title', 'username', 'email', 'url', # which fields to displays
                  'password', 'notes']
        widgets = {'notes': Textarea(attrs={'cols': 40, 'rows': 4})} # provide minimal styling for the dimensions of the notes field
