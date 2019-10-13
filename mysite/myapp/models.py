from django.db import models

class MyTable(models.Model):
    ID = models.CharField(max_length=100)
