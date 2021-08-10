# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class (models.Model):
    номер_заказа_клиента = models.TextField(db_column='Номер заказа клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_менеджера = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_клиента = models.TextField(db_column='Код клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    дата_оформления = models.TextField(db_column='Дата оформления', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Заказ клиента'


class (models.Model):
    номер_заказа_поставщика = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_менеджера = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_поставщика = models.TextField(db_column='Код поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    дата_заказа = models.TextField(db_column='Дата заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    статус = models.TextField(db_column='Статус', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Заказ поставщика'


class (models.Model):
    код_категории = models.TextField(db_column='Код категории', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    название_категории = models.TextField(db_column='Название категории', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Категория'


class (models.Model):
    код_клиента = models.TextField(db_column='Код клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    фамилия = models.TextField(db_column='Фамилия', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    имя = models.TextField(db_column='Имя', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    адрес = models.TextField(db_column='Адрес', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    телефон = models.TextField(db_column='Телефон', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Клиент'


class (models.Model):
    номер_заказа_клиента = models.TextField(db_column='Номер заказа клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    промокод = models.TextField(db_column='Промокод', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    скидка = models.TextField(db_column='Скидка', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    код_клиента = models.TextField(db_column='Код клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Корзина товаров'


class (models.Model):
    код_менеджера = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    имя = models.TextField(db_column='Имя', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    фамилия = models.TextField(db_column='Фамилия', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    отчество = models.TextField(db_column='Отчество', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    телефон = models.TextField(db_column='Телефон', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Менеджер'


class (models.Model):
    код_поставщика = models.TextField(db_column='Код поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    адрес = models.TextField(db_column='Адрес', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    телефон = models.TextField(db_column='Телефон', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Поставщик'


class (models.Model):
    артикул_товара = models.TextField(db_column='Артикул товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    свободное_количество_товара = models.TextField(db_column='Свободное количество товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    количество_товара_в_резерве = models.TextField(db_column='Количество товара в резерве', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Склад'


class (models.Model):
    номер_заказа_клиента = models.TextField(db_column='Номер заказа клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    дата_оплаты = models.TextField(db_column='Дата оплаты', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    сумма_к_оплате = models.TextField(db_column='Сумма к оплате', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    статус = models.TextField(db_column='Статус', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Счет клиента'


class (models.Model):
    номер_заказа_поставщика = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_менеджера = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    сумма_заказа = models.TextField(db_column='Сумма заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    дата_оплаты = models.TextField(db_column='Дата оплаты', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Счет поставщика'


class (models.Model):
    артикул_товара = models.TextField(db_column='Артикул товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    название_товара = models.TextField(db_column='Название товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    статус_наличия = models.TextField(db_column='Статус наличия', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    цена = models.TextField(db_column='Цена', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Товар'


class (models.Model):
    артикул_товара = models.TextField(db_column='Артикул товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    номер_заказа_поставщика = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    количество_товара = models.TextField(db_column='Количество товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Товар-Заказ поставщика'


class (models.Model):
    артикул_товара = models.TextField(db_column='Артикул товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    код_категории = models.TextField(db_column='Код категории', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Товар-Категория'


class (models.Model):
    артикул_товара = models.TextField(db_column='Артикул товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    номер_заказа_клиента = models.TextField(db_column='Номер заказа клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    количество_товаров = models.TextField(db_column='Количество товаров', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Товар-Корзина товаров'
