# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class (models.ClientOrders):
    client_order_number = models.TextField(db_column='Номер заказа клиента', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    manager_code = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    client_code = models.TextField(db_column='Код клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    subscribe_date = models.TextField(db_column='Дата оформления', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Заказ клиента'


class (models.DeveloperOrders):
    developer_oreder_number = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    manager_code = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    developer_code = models.TextField(db_column='Код поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    order_date = models.TextField(db_column='Дата заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    status = models.TextField(db_column='status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Заказ поставщика'


class (models.Categories):
    category_code = models.TextField(db_column='Код категории', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    category_name = models.TextField(db_column='Название категории', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Категория'


class (models.Clients):
    client_code = models.TextField(db_column='Код клиента', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    last_name = models.TextField(db_column='last_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    first_name = models.TextField(db_column='first_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Клиент'


class (models.MarketBus):
    client_order_number = models.TextField(db_column='Номер заказа клиента', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    promo_code = models.TextField(db_column='promo_code', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discount = models.TextField(db_column='discount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    client_code = models.TextField(db_column='Код клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Корзина товаров'


class (models.Managers):
    manager_code = models.TextField(db_column='Код менеджера', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    first_name = models.TextField(db_column='first_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_name = models.TextField(db_column='last_name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    отчество = models.TextField(db_column='Отчество', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Менеджер'


class (models.Developers):
    developer_code = models.TextField(db_column='Код поставщика', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    address = models.TextField(db_column='address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Поставщик'


class (models.Market):
    item_id = models.TextField(db_column='Артикул товара', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    free_items_number = models.TextField(db_column='Свободное количество товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    reserve_items_number = models.TextField(db_column='Количество товара в резерве', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Склад'


class (models.ClientAccount):
    client_order_number = models.TextField(db_column='Номер заказа клиента', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    pay_dates = models.TextField(db_column='Дата оплаты', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    pay_price = models.TextField(db_column='Сумма к оплате', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    status = models.TextField(db_column='status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Счет клиента'


class (models.DeveloperAccount):
    developer_oreder_number = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    manager_code = models.TextField(db_column='Код менеджера', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    order_price = models.TextField(db_column='Сумма заказа', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    pay_dates = models.TextField(db_column='Дата оплаты', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Счет поставщика'


class (models.Items):
    item_id = models.TextField(db_column='Артикул товара', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    item_name = models.TextField(db_column='Название товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    status_наличия = models.TextField(db_column='status наличия', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    price = models.TextField(db_column='price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        
        db_table = 'Товар'


class (models.DeveloperItemOrder):
    item_id = models.TextField(db_column='Артикул товара', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    developer_oreder_number = models.TextField(db_column='Номер заказа поставщика', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    items_number = models.TextField(db_column='Количество товара', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Товар-Заказ поставщика'


class (models.ItemCategory):
    item_id = models.TextField(db_column='Артикул товара', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    category_code = models.TextField(db_column='Код категории', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Товар-Категория'


class (models.ItemsItemBus):
    item_id = models.TextField(db_column='Артикул товара', blank=True, null=True, primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    client_order_number = models.TextField(db_column='Номер заказа клиента', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    items_items_number = models.TextField(db_column='Количество товаров', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        
        db_table = 'Товар-Корзина товаров'
