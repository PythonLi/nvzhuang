#coding:utf-8
from django.contrib import admin

from dataweb.models import Mogujie

admin.AdminSite.site_header = '四月之家'

class MogujieAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'org_price', 'sale', 'update_date', 'web_link']
    search_fields = ['title']
    ordering = ['-sale']
    list_select_related = True
    #改变编辑页的显示
    #fields = (('title', 'trade_item_id', 'price',
    #           'org_price', 'sale', 'img', 'update_date'),
    #          'link')

    def web_link(self,obj):
        return u'<a href="{link}" target="_blank">{obj}</a>'.format(link=obj.link, obj=obj.trade_item_id)
    web_link.allow_tags = True
    web_link.short_description = "网站链接"
    def __init__(self,*args,**kwargs):
       super(MogujieAdmin, self).__init__(*args, **kwargs)
       #self.list_display_links = (None, )


admin.site.register(Mogujie, MogujieAdmin)
