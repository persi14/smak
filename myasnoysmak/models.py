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
    nameproduct = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название продукта")
    foodvalue = models.CharField(max_length=150, blank=True, null=True, verbose_name="Пищевая ценность")
    energyvalue = models.CharField(max_length=150, blank=True, null=True, verbose_name="Энергитеческая ценность")
    idtype = models.ForeignKey('TypeProduct', models.DO_NOTHING, db_column='idtype', verbose_name="Тип продукта")
    image = models.ImageField(upload_to="product", verbose_name="Изображение")
    structure = models.TextField(max_length=400, blank=True, null=True, verbose_name="Состав")
    cost = models.CharField(max_length=150, blank=True, verbose_name="Стоимость")

    def __str__(self):
        return self.nameproduct

    def save(self, *args, **kwargs):
        try:
            this_product = Product.objects.get(idproduct = self.idproduct)
            if this_product.image != self.image:
                this_product.image.delete(save=False)
        except:
            pass
        super(Product, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Product, self).delete(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name = u'Продукты'
        verbose_name_plural = u'Продукты'


class TypeProduct(models.Model):
    idtype = models.AutoField(primary_key=True)
    nametype = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name = u'Тип продукта')


    def __str__(self):
        return self.nametype

    class Meta:
        managed = False
        db_table = 'type_product'
        verbose_name = u'Тип продукта'
        verbose_name_plural = u'Тип продукта'