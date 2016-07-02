# -*- coding: utf-8 -*-

import random
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

from myapp.models import Item, Client, Order, Ordering, City
from myapp.forms import ItemForm, ItemDelForm, ItemPlusForm, ItemMinusForm, OrderForm, SortForm

def randomItems(request):
    rand_items = []
    item = list(Item.objects.all())
    while len(rand_items) != 4:
        rand_items.append(random.choice(item))
    return rand_items

def basketItems(request):
    try:
        basket_items = request.session["items"]
    except KeyError:
        basket_items = []
    return basket_items
    
def index(request):
    template = loader.get_template("index.html")
    context = RequestContext(request, {"rand_items": randomItems(request),
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_preview(request):
    template = loader.get_template("goods_preview.html")
    context = RequestContext(request, {"rand_items1": randomItems(request),
                                       "rand_items2": randomItems(request),
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def sorting_func(request, item_num):
    if request.method == "GET":
        form = SortForm(request.GET)

        if form.is_valid():
            sorting = form.cleaned_data["sorting"]

            if sorting == "убывание цена":
                items = Item.objects.filter(type_item=item_num).order_by("-cost")
            elif sorting == "возрастание цена":
                items = Item.objects.filter(type_item=item_num).order_by("cost")
            elif sorting == "убывание название":
                items = Item.objects.filter(type_item=item_num).order_by("-name")
            elif sorting == "возрастание название":
                items = Item.objects.filter(type_item=item_num).order_by("name")
        else:
            items = Item.objects.filter(type_item=item_num)
    return items

def goods_shirts(request):
    items = sorting_func(request, 1)
    template = loader.get_template("goods/goods_shirts.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_shoes(request):
    items = sorting_func(request, 2)
    template = loader.get_template("goods/goods_shoes.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_dress(request):
    items = sorting_func(request, 3)
    template = loader.get_template("goods/goods_dress.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_skirts(request):
    items = sorting_func(request, 4)
    template = loader.get_template("goods/goods_skirts.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_pants(request):
    items = sorting_func(request, 5)
    template = loader.get_template("goods/goods_pants.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_bags(request):
    items = sorting_func(request, 6)
    template = loader.get_template("goods/goods_bags.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_heads(request):
    items = sorting_func(request, 7)
    template = loader.get_template("goods/goods_heads.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_accessories(request):
    items = sorting_func(request, 8)
    template = loader.get_template("goods/goods_accessories.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_socks(request):
    items = sorting_func(request, 9)
    template = loader.get_template("goods/goods_socks.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods_others(request):
    items = sorting_func(request, 10)
    template = loader.get_template("goods/goods_others.html")
    context = RequestContext(request, {"items": items,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def goods(request):
    shirts_list = Item.objects.filter(type_item=1)
    shoes_list = Item.objects.filter(type_item=2)
    dresses_list = Item.objects.filter(type_item=3)
    skirts_list = Item.objects.filter(type_item=4)
    pants_list = Item.objects.filter(type_item=5)
    bags_list = Item.objects.filter(type_item=6)
    heads_list = Item.objects.filter(type_item=7)
    accessories_list = Item.objects.filter(type_item=8)
    socks_list = Item.objects.filter(type_item=9)
    others_list = Item.objects.filter(type_item=10)

    template = loader.get_template("goods.html")
    context = RequestContext(request, {
        "shirts_list": shirts_list,
        "shoes_list": shoes_list,
        "dresses_list": dresses_list,
        "skirts_list": skirts_list,
        "pants_list": pants_list,
        "bags_list": bags_list,
        "heads_list": heads_list,
        "accessories_list": accessories_list,
        "socks_list": socks_list,
        "others_list": others_list,
        "basket_items": basketItems(request),})

    return HttpResponse(template.render(context))

def contacts(request):
    template = loader.get_template("contacts.html")
    context = RequestContext(request, {"rand_items": randomItems(request),
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def delivery(request):
    template = loader.get_template("delivery.html")
    context = RequestContext(request, {"rand_items": randomItems(request),
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def selected_item(request, item_id):
    item = Item.objects.get(id = item_id)

    template = loader.get_template("item_view.html")
    context = RequestContext(request, {"item": item,
                                       "basket_items": basketItems(request),})
    return HttpResponse(template.render(context))

def basket(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        formDel = ItemDelForm(request.POST)
        formPlus = ItemPlusForm(request.POST)
        formMinus = ItemMinusForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data["id_item"]
            try:
                if item not in request.session["items"]:
                    request.session["items"].append(item)
                    request.session["count_items"][str(item)] = 1
            except KeyError:
                request.session["items"] = list()
                request.session["count_items"] = dict()
                if item not in request.session["items"]:
                    request.session["items"].append(item)
                    request.session["count_items"][str(item)] = 1

        elif formDel.is_valid():
            item = formDel.cleaned_data["id_item_del"]
            request.session["items"].remove(item)
            del request.session["count_items"][str(item)]

        elif formPlus.is_valid():
            item = formPlus.cleaned_data["id_item_plus"]
            available = Item.objects.get(id = item).available_count
            available_now = Item.objects.get(id = item).is_available_now

            request.session["count_items"][str(item)] += 1
            if request.session["count_items"][str(item)] > available \
               and available_now:
                request.session["count_items"][str(item)] = available

        elif formMinus.is_valid():
            item = formMinus.cleaned_data["id_item_minus"]
            request.session["count_items"][str(item)] -= 1
            if request.session["count_items"][str(item)] < 1:
                request.session["count_items"][str(item)] = 1

        request.session.modified = True

    basket_items = basketItems(request)

    if len(basket_items) > 0:
        item_list = []
        item_list.append(
            [Item.objects.get(id = basket_items[0]),
             Item.objects.get(id = basket_items[0]).available_count,
             request.session["count_items"][str(basket_items[0])]])
        for item in basket_items[1:]:
            item_list.append(
            [Item.objects.get(id = item),
             Item.objects.get(id = item).available_count,
             request.session["count_items"][str(item)]])

        cities = City.objects.all()
    else:
        item_list = []
        cities = []

    summary_cost = 0
    for item in item_list:
        summary_cost += item[0].cost * item[2]

    template = loader.get_template("basket.html")
    context = RequestContext(request, {"basket_items": basket_items,
                                       "item_list": item_list,
                                       "summary_cost": summary_cost,
                                       "cities": cities, })

    return HttpResponse(template.render(context))

def accept_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            Client.objects.create(f_name = form.cleaned_data["f_name"],
                                  l_name = form.cleaned_data["l_name"],
                                  m_name = form.cleaned_data["m_name"],
                                  phone = form.cleaned_data["phone"],
                                  city = City.objects.get(name_city = form.cleaned_data["city"]),
                                  address = form.cleaned_data["address"])
            client = Client.objects.filter(phone = form.cleaned_data["phone"])[0]
            Order.objects.create(id_client = client,
                                 date_order = datetime.datetime.now(),
                                 date_taken = None,
                                 is_paid = False,
                                 is_taken = False,
                                 summary = float(form.cleaned_data["totalCost"].replace(",", ".")))

            last_ordered = len(Order.objects.filter(id_client = client)) - 1

            order = Order.objects.filter(id_client = client)[last_ordered]
            for item in request.session["items"]:
                item_get = Item.objects.get(id = item)
                Ordering.objects.create(
                    id_order = order,
                    id_item = item_get,
                    count_items = request.session["count_items"][str(item)])

                item_get.available_count -= request.session["count_items"][str(item)]
                if item_get.available_count <= 0:
                    item_get.is_available_now = False
                item_get.save()

        request.session["items"] = list()
        request.session["count_items"] = dict()

        template = loader.get_template("accept_order.html")
        context = RequestContext(request, {"rand_items": randomItems(request),
                                           "basket_items": basketItems(request),
                                           "client": client, })
        return HttpResponse(template.render(context))
    else:
        return redirect("index")


