# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^goods_preview', views.goods_preview, name="goods_preview"),
    #url(r'^goods', views.goods, name="goods"),
    url(r'^contacts', views.contacts, name="contacts"),
    url(r'^delivery', views.delivery, name="delivery"),
    url(r'^item/(?P<item_id>\d+)/$', views.selected_item),
    url(r'^basket', views.basket, name="basket"),
    url(r'^thanks', views.accept_order, name="thanks"),

    url(r'^shirts', views.goods_shirts, name="shirts"),
    url(r'^shoes', views.goods_shoes, name="shoes"),
    url(r'^dress', views.goods_dress, name="dress"),
    url(r'^skirts', views.goods_skirts, name="skirts"),
    url(r'^pants', views.goods_pants, name="pants"),
    url(r'^bags', views.goods_bags, name="bags"),
    url(r'^heads', views.goods_heads, name="heads"),
    url(r'^accessories', views.goods_accessories, name="accessories"),
    url(r'^socks', views.goods_socks, name="socks"),
    url(r'^others', views.goods_others, name="others"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
