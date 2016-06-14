# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import connection

# Create your models here.
class persons(models.Model):
    name = models.CharField(max_length=30)
    log  = models.CharField(max_length=200)

    def __str__(self):
        return self.name

def my_custom_sql(self):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO testing_persons VALUES('shabi','ershazi')")
    row = cursor.save()

    return row







