# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Entry(models.Model): # models.Model 클래스를 상속받음
    user = models.ForeignKey(User)
    pattern = models.CharField(max_length=255)
    test_string = models.CharField(max_length=255)
    date_added = models.DateTimeField(default=timezone.now) #note: callable 함수를 보냄

    class Meta:
        verbose_name_plural = 'entries'

# Need to instruct Django that it needs to create the code to update the database
# python3 manage.py makemigrations entries
# python3 manage.py migrate