#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午8:42
# @Author  : Aries
# @Site    : 
# @File    : rookk_main.py
# @Software: PyCharm Community Edition
import os
import json
from redis_helper import RedisHelper
from flask import Flask, session
from flask import request
from controller.caculate import CaculateRisk

redis_helper = RedisHelper()
app = Flask(__name__)


@app.route('/')
def index():
    return 'this is index...'


@app.route('/Alldata', methods=['POST'])
def alldata():
    Result = 1
    content = {}
    json_return = {}
    try:
        app.logger.debug('request get...')
        cr = CaculateRisk(request.json)
        sapsi5, arthritis6, pr7 = cr.caculate()
        content = {'saPASI': sapsi5, 'Arthritis6': arthritis6, 'PR7': pr7}
        redis_helper.public(cr.content())
    except Exception as e:
        app.logger.exception(e)
        Result = 2
    if content:
        json_return = content
    json_return['Result'] = Result
    return json.dumps(json_return)


if __name__ == '__main__':
    app.run(port=9160, debug=True)
