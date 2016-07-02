# -*- coding: utf-8 -*-

from django.contrib import admin
from myapp.models import Client, Item, Order, Ordering, City, Type, Color, Size

class ClientAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name", "m_name", "phone", "city", "address")
    list_filter = ["f_name", "l_name", "phone", "city"]

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_type", "cost", "get_size", "get_color",
                    "is_available_now", "available_count")
    list_filter = ["type_item", "is_available_now", "size", "color", "cost", "available_count"]

    def get_type(self, obj):
        return obj.type_item.name_type_rus

    def get_size(self, obj):
        return obj.size.size

    def get_color(self, obj):
        return obj.color.name_color

class OrderingAdmin(admin.ModelAdmin):
    list_display = ("id_order", "id_item", "count_items")
    list_filter = ["id_order", "id_item", "count_items"]

class OrderingInline(admin.TabularInline):
    model = Ordering
    fk_name = "id_order"
    max_num = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "id_client", "date_order", "date_taken", "is_paid",
                    "is_taken", "summary")
    list_filter = ["date_order", "date_taken", "is_paid", "is_taken",
                   "summary"]

    inlines = [
        OrderingInline,
        ]

class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name_city")
    list_filter = ["id", "name_city"]

class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name_type", "name_type_rus")
    list_filter = ["id", "name_type", "name_type_rus"]

class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name_color")
    list_filter = ["id", "name_color"]

class SizeAdmin(admin.ModelAdmin):
    list_display = ("id", "size")
    list_filter = ["id", "size"]

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Ordering, OrderingAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)

