#-*- coding: utf-8 -*-

import re
import redis
import json
import sys

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        """
        TODO: 将 item 结果以 JSON 形式保存到 Redis 数据库的 list 结构中
        """        
        data = json.dumps(item)
        self.redis.lpush('douban_movie:items',data)
        if self.redis.llen('douban_movie:items')>35:
            print('已经有35条数据')
        return item
        

    def open_spider(self, spider):
        # 连接数据库
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)