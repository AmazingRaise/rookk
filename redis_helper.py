#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/13 下午3:15
# @Author  : Aries
# @Site    :
# @File    : reids_helper.py
# @Software: PyCharm Community Edition
import time
import redis
from base.excel_helper import ExcelHelper


class RedisHelper(object):

    def __init__(self):
        # 链接
        self.__conn = redis.Redis()
        self.chan_sub = 'fm104.5'
        # 创建频道
        self.chan_pub = 'fm104.5'
        self.result = []

    def public(self, info):
        self.__conn.publish(self.chan_pub, info)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

    def get_value_from_redis(self):
        redis_sub = self.subscribe()
        while True:
            msg = redis_sub.parse_response()
            if isinstance(msg, list):
                if len(msg) > 0 and msg[1].decode('utf-8') == self.chan_sub:
                    val = eval(msg[2].decode('utf-8'))
                    self.result.append(val)
            if len(self.result) > 9:
                print('result长度为：%d, 写入文件' % len(self.result))
                excel_helper = ExcelHelper()
                for val in self.result:
                    excel_helper.insert_data(val)
                self.result = []
            time.sleep(0.1)


if __name__ == '__main__':
    rh = RedisHelper()
    rh.get_value_from_redis()
