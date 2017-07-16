#coding:utf-8
from django.contrib import admin

from dataweb.models import Mogujie

admin.AdminSite.site_header = '四月之家'

@admin.register(Mogujie)
class MogujieAdmin(admin.ModelAdmin):
    list_display = ['title', 'trade_item_id', 'price', 'org_price', 'sale', 'update_date']
    search_fields = ['title']
    ordering = ['-sale']
    list_select_related = True
    #改变编辑页的显示
    #fields = (('title', 'trade_item_id', 'price',
    #           'org_price', 'sale', 'img', 'update_date'),
    #          'link')


#admin.site.register(Mogujie)
