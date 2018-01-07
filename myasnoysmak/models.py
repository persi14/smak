# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models





class Comment(models.Model):
    idcomment = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Product(models.Model):
    idproduct = models.IntegerField(primary_key=True)
    nameproduct = models.CharField(max_length=100, blank=True, null=True)
    foodvalue = models.CharField(max_length=150, blank=True, null=True)
    energyvalue = models.CharField(max_length=150, blank=True, null=True)
    idtype = models.ForeignKey('TypeProduct', models.DO_NOTHING, db_column='idtype', unique=True)

    class Meta:
        managed = False
        db_table = 'product'


class TypeProduct(models.Model):
    idtype = models.IntegerField(primary_key=True)
    nametype = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_product'
