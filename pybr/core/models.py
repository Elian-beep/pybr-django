from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class State(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    name = models.CharField(db_column='tx_name', null=False, blank=False, max_length=64)
    abbreviation = models.CharField(db_column='tx_abreviation', null=False, max_length=2)

    class Meta:
        db_table = 'state'
        managed = True