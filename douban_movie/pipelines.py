#-*- coding: utf-8 -*-

import re
import redis
import json
import sys
from scrapy.exceptions import DropItem

class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        """
        TODO: 将 item 结果以 JSON 形式保存到 Redis 数据库的 list 结构中
        """        
        # data = json.dumps(item)
        self.redis.lpush('douban_movie:items',item)
        if self.redis.llen('douban_movie:items')>35:
            print('已经有35条数据')
        if float(item['score']<8.0):
            raise DropItem('score is less than 8.0')
        return item
        

    def open_spider(self, spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)