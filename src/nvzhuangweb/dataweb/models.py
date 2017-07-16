#coding:utf-8
from django.db import models
from django.utils import timezone


class Mogujie(models.Model):
    title = models.CharField(verbose_name='商品名', max_length=300 )
    trade_item_id = models.CharField(verbose_name='商品ID', max_length=50)
    price = models.CharField(verbose_name='价格', max_length=50)
    org_price = models.CharField(verbose_name='原价', max_length=50)
    sale = models.IntegerField(verbose_name='销量')
    img = models.ImageField(verbose_name='图片', upload_to='mogujie')
    link = models.URLField(verbose_name='详情链接', max_length=300)
    update_date = models.DateTimeField(verbose_name='更新时间', default=timezone.now)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'mogujie'
        verbose_name = verbose_name_plural = '蘑菇街'
        index_together = ('title', 'trade_item_id', 'price', 'sale')
