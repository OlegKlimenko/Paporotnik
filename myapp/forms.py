# -*- coding: utf-8 -*-

from django import forms

class ItemForm(forms.Form):
    id_item = forms.IntegerField()

class ItemDelForm(forms.Form):
    id_item_del = forms.IntegerField()

class ItemPlusForm(forms.Form):
    id_item_plus = forms.IntegerField()

class ItemMinusForm(forms.Form):
    id_item_minus = forms.IntegerField()

class OrderForm(forms.Form):
    f_name = forms.CharField(max_length = 100)
    l_name = forms.CharField(max_length = 100)
    m_name = forms.CharField(max_length = 100)
    phone = forms.CharField(max_length = 100)
    city = forms.CharField(max_length = 100)
    address = forms.CharField(max_length = 100)
    totalCost = forms.CharField(max_length = 100)

class SortForm(forms.Form):
    sorting = forms.CharField(max_length = 25)
