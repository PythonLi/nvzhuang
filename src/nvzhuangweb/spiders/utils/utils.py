#coding:utf-8

import random

from fake_useragent import UserAgent


def get_user_agent():
    ua = UserAgent()
    return ua.random


REFERER_LIST = [
    'https://www.google.com/',
    'https://www.baidu.com/',
]

HEADERS = {
            "User-Agent": get_user_agent(),
            #"Referer" : random.choice(REFERER_LIST),
            "Accept-encoding": "gzip",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch, br",
            "Accept-Language": "en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            }
