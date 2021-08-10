from django.db import models


class Сlient(models.Model):
    id_client = models.IntegerField(primary_key=True)
    lastname = models.TextField()
    firstname = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField()

class Order(models.Model):
    id_order = models.IntegerField(primary_key=True)
    code_manager = models.IntegerField()
    id_client = models.ForeignKey(Сlient, on_delete=models.CASCADE)
    date_order = models.DateTimeField()

class Order_Client(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bill = models.IntegerField()
    status = models.TextField() #придумать статусы

class Basket(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE )
    Varchar = models.TextField()
    Sale = models.IntegerField(max_length= 100)
    status = models.TextField(Order, on_delete=models.CASCADE)

class Product(models.Model):
    id_product = models.ForeignKey(primary_key=True)
    name_product = models.TextField()
    product_volume = models.IntegerField()
    cost_product = models.IntegerField()

class Product_Backet(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    value_product = models.IntegerField()

class Category(models.Model):
    id_category = models.ForeignKey(primary_key=True)
    category_name = models.TextField()

class Product_category(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Stock(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    free_count = models.IntegerField()
    reserv_count = models.IntegerField()

class Managere(models.Model):
    id_manager = models.ForeignKey(primary_key=True)
    fistname_manager = models.TextField()
    lastname_manager = models.TextField()
    patronymic_manager = models.TextField()   # отчество
    phone_manager = models.IntegerField()

class Provider(models.Model):
    id_prvider = models.ForeignKey(primary_key=True)
    address_provider = models.TextField()
    phone_number_provider = models.IntegerField()

class Product_order_provider(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_order_provider = models.ForeignKey()
    count_product = models.ImageField()

class Bill_provider(models.Model):
    number_order_provider = models.ForeignKey(Product_order_provider, on_delete=models.CASCADE)
    id_manager = models.ForeignKey(Managere, on_delete=models.CASCADE)
    bill = models.IntegerField()
    date_order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Order_provider(models.Model):
     number_order_provider = models.ForeignKey(Product_order_provider, on_delete=models.CASCADE)
     id_manager = models.ForeignKey(Managere, on_delete=models.CASCADE)
     id_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
     date_order = models.ForeignKey(Order, on_delete=models.CASCADE)
     status = models.TextField() # связвть и придумать статусы


