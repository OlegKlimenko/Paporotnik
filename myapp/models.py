# -*- coding: utf-8 -*-

from django.db import models

class Type(models.Model):
    name_type = models.CharField(verbose_name="Тип товара", max_length=100)
    name_type_rus = models.CharField(verbose_name="Тип товара русск.", max_length=100, default="lol")

    def __str__(self):
        return self.name_type_rus

class City(models.Model):
    name_city = models.CharField(verbose_name="Город", max_length=100)

    def __str__(self):
        return self.name_city

class Color(models.Model):
    name_color = models.CharField(verbose_name="Цвет", max_length=100)

    def __str__(self):
        return self.name_color

class Size(models.Model):
    size = models.CharField(verbose_name="Размер", max_length=100)

    def __str__(self):
        return self.size

class Client(models.Model):
    f_name = models.CharField(verbose_name="Фамилия", max_length=100)
    l_name = models.CharField(verbose_name="Имя", max_length=100)
    m_name = models.CharField(verbose_name="Отчество", max_length=100)
    phone = models.CharField(verbose_name="Телефон", max_length=100)
    city = models.ForeignKey(City, verbose_name="Город")
    address = models.CharField(verbose_name="Адрес", max_length=200)

    def __str__(self):
        return self.f_name + " " + self.l_name + " " + self.m_name + \
               " (" + self.phone + ")" + " Город: " + str(self.city) + " Адрес:" + \
               self.address

class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    type_item = models.ForeignKey(Type, verbose_name="Тип продукта")
    other = models.TextField(verbose_name="Другая информация")
    color = models.ForeignKey(Color, verbose_name="Цвет", default = 0)
    cost = models.DecimalField(verbose_name="Стоимость за штуку", default=0, decimal_places=2, max_digits=7)
    size = models.ForeignKey(Size, verbose_name="Размер", default=0)
    is_available_now = models.BooleanField(verbose_name="В наличии?", default=False)
    available_count = models.IntegerField(verbose_name="Кол-во в наличии", default=0)
    photo = models.ImageField(verbose_name="Фото", upload_to="media")

    def __str__(self):
        return self.type_item.name_type_rus + " " + self.name + " " + self.color.name_color + \
               " (" + str(self.cost) + " грн)"

class Order(models.Model):
    id_client = models.ForeignKey(Client, null=True, blank=True, verbose_name="Клиент")
    date_order = models.DateField(verbose_name="Дата заказа")
    date_taken = models.DateField(verbose_name="Дата получения", null=True)
    is_paid = models.BooleanField(verbose_name="Оплачено?",  default=False)
    is_taken = models.BooleanField(verbose_name="Получено?",  default=False)
    summary = models.IntegerField(verbose_name="Сумма", default=0)

    def __str__(self):
        return "(Заказ #:" + str(self.id) + ")  " + str(self.id_client)

class Ordering(models.Model):
    id_order = models.ForeignKey(Order, verbose_name="Заказ")
    id_item = models.ForeignKey(Item, verbose_name="Товар")
    count_items = models.IntegerField(verbose_name="Количество", default=0)