# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class News(models.Model):
    idnews = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True, auto_now_add=True)
    text = models.TextField(blank=True, null=True, verbose_name="Текст новости")
    url_image = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name="Заголовок новости")

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'news'
        verbose_name = u'Новости'
        verbose_name_plural = u'Новости'


class Product(models.Model):
    idproduct = models.AutoField(primary_key=True)
    nameproduct = models.CharField(max_length=100, blank=True, null=True)
    foodvalue = models.CharField(max_length=150, blank=True, null=True)
    energyvalue = models.CharField(max_length=150, blank=True, null=True)
    idtype = models.ForeignKey('TypeProduct', models.DO_NOTHING, db_column='idtype',)

    def __str__(self):
        return self.nameproduct

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name = u'Продукты'
        verbose_name_plural = u'Продукты'


class TypeProduct(models.Model):
    idtype = models.AutoField(primary_key=True)
    nametype = models.CharField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nametype

    class Meta:
        managed = False
        db_table = 'type_product'
        verbose_name = u'Тип продукта'
        verbose_name_plural = u'Тип продукта'