#coding:utf-8

'''
2017-9-19
爬取手表网站
'''
import logging
import json

import requests
from lxml import etree

from utils.utils import HEADERS
from pipelines import CrawlerPipeline

logger = logging.getLogger('myspider')


class Watch(object):

    def __init__(self):
        '''
        截止到 2017-9-19：其产品总页数为 189页
        '''
        self.base_url = 'https://h5.youzan.com/v2/showcase/tag?alias=d7nqj1nn&page=1'
        self.pipeline = CrawlerPipeline()

    def start_crawl(self):
        res = requests.get(self.base_url, headers=HEADERS)
        data=json.loads(res.content.decode('utf-8'))
        total = data['result']['wall']['total']
        per_page = data['result']['wall']['perPage']
        pages = int(total/per_page)
        logger.debug('蘑菇街女裙商品总页数：{};每页商品数:{}'\
                     .format(pages, per_page))
        return self.crawl_mogujie(pages)

    def crawl_noob(self, pages):
        '''
        爬取NOOB表厂
        '''
        #import pdb
        #pdb.set_trace()
        for page in range(pages):
            logger.debug('\033[96m 开始爬取第{}页 \033[0m'.format(page))
            url = 'https://h5.youzan.com/v2/showcase/tag?alias=d7nqj1nn&page={page}'\
                .format(page=page)
            res = requests.get(url, headers=HEADERS)
            html=etree.HTML(res.text)
            ul = html.xpath('//ul[@class="js-goods-list sc-goods-list clearfix list size-3"]/li')
            items = []
            for li in ul:
                product_name = li.xpath('./a/@title')
                # 该原价是指淘宝价
                origin_price = li.xpath('./a/div[2]/p[@class="goods-price-taobao"]/text()')[0]
                promotion_price = li.xpath('./a/div[2]/p[@class="goods-price"]/em/text()')[0]
                link = li.xpath('./a/@href')
                items.append({
                    'product_name': product_name,
                    'origin_price': origin_price,
                    'promotion_price': promotion_price,
                    'link': link,
                })
            logger.debug('\033[96m 第{}页爬取完毕, 总共爬取{}商品 \033[0m'.format(page, len(items)))

    def crawl_detail_noob(self, items):
        '''
        爬取NOOB表厂商品详情页
        https://detail.youzan.com/show/goods?alias=26z14q8fgzzjz&v2/goods/26z14q8fgzzjz
        爬取 图片
        '''
        details = []
        for item in items:
            res = requests.get(item['link'], headers=HEADERS)
            sale = ''
            detail = ''
            standard = ''
            item.update({
                'sale': sale,
                'detail': detail,
                'standard': standard,
            })
            details.append(item)
            self.pipeline.save_watch(details)

    def crawl_yangguangbiaoye(self, pages):
        '''
        爬取 阳光表业
        '''
        pass







if __name__ == '__main__':
    mogujie = Mogujie()
    mogujie.start_crawl()

