#coding:utf-8

import sys
import os
import logging
import django

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'nvzhuangweb.settings'
django.setup()

from dataweb.models import Mogujie

logger = logging.getLogger('mydata')

class NvzhuangPipeline(object):

    def save_mogujie(self, item_list):
        for item in item_list:
            title = item['title']
            trade_item_id = item['trade_item_id']
            price = item['price']
            org_price = item['org_price']
            sale = item['sale']
            img = item['img']
            link = item['link']
            logger.debug('\033[96m 保存商品：{}\033[0m'.format(title))
            try:
                mogujie, created = Mogujie.objects.get_or_create(
                    title = title,
                    trade_item_id = trade_item_id,
                    price = price,
                    defaults={
                        'org_price': org_price,
                        'sale': sale,
                        'img': img,
                        'link': link,
                    }
                )
                if not created:
                    mogujie.org_price = org_price
                    mogujie.sale = sale
                    mogujie.img = img
                    mogujie.link = link
            except Exception as e:
                logger.error('\033[92m 保存商品出错： {} \033[0m'.format(e))
