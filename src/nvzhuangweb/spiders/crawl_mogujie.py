#coding:utf-8

'''
2017-7-15
爬蘑菇街女装
'''
import logging
import json

import requests

from utils.utils import HEADERS
from pipelines import NvzhuangPipeline

logger = logging.getLogger('myspider')


class Mogujie(object):

    def __init__(self):
        self.base_url = 'http://list.mogujie.com/search?cKey=15&fcid=50004&action=skirt&page=1'
        self.pipeline = NvzhuangPipeline()

    def start_crawl(self):
        res = requests.get(self.base_url, headers=HEADERS)
        data=json.loads(res.content.decode('utf-8'))
        total = data['result']['wall']['total']
        per_page = data['result']['wall']['perPage']
        pages = int(total/per_page)
        logger.debug('蘑菇街女裙商品总页数：{};每页商品数:{}'\
                     .format(pages, per_page))
        return self.crawl_mogujie(pages)

    def crawl_mogujie(self, pages):
        #import pdb
        #pdb.set_trace()
        for page in range(pages):
            logger.debug('\033[96m 开始爬取第{}页 \033[0m'.format(page))
            url = 'http://list.mogujie.com/search?cKey=15&fcid=50004&action=skirt&page={page}'\
                .format(page=page)
            res = requests.get(url, headers=HEADERS)
            data = json.loads(res.content.decode('utf-8'))
            items = data['result']['wall']['docs']
            item_list = []
            for item in items:
                title = item['title']
                trade_item_id = item['tradeItemId']
                price = item['price']
                org_price = item['orgPrice']
                sale = item['sale']
                img = item['img']
                link = item['link']
                item_list.append({
                    'title': title,
                    'trade_item_id': trade_item_id,
                    'price': price,
                    'org_price': org_price,
                    'sale': sale,
                    'img': img,
                    'link': link,
                })
            self.pipeline.save_mogujie(item_list)
            logger.debug('\033[96m 第{}页爬取完毕, 总共爬取{}商品 \033[0m'.format(page, len(item_list)))










if __name__ == '__main__':
    mogujie = Mogujie()
    mogujie.start_crawl()

