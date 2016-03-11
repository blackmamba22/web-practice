from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class ToDoItem(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateTimeField(default=datetime.today)

    def __unicode__(self):
        return self.name
