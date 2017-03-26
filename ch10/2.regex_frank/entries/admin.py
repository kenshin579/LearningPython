# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Entry #relative import (장점: app의 이름 변경, 옮겨도 문제가 안됨)

# Entry model을 admin panel과 연결하기

@admin.register(Entry) #display the Entry model in the admin panel
class EntryAdmin(admin.ModelAdmin):
    fieldsets = [ # the create/edit page
        ('Regular Expression',
         {'fields': ['pattern', 'test_string']}),
        ('Other Information',
         {'fields': ['user', 'date_added']}),
    ]
    list_display = ('pattern', 'test_string', 'user') #list page (no date)
    list_filter = ['user']
    search_fields = ['test_string']

