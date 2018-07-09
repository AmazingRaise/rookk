#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午8:42
# @Author  : Aries
# @Site    : 
# @File    : rookk_main.py
# @Software: PyCharm Community Edition
import os
import json
import time
import traceback
from flask import Flask, session
from flask import request
from controller.caculate import CaculateRisk
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
        print(request.json)
        cr = CaculateRisk(request.json)
        sapsi5, arthritis6, pr7 = cr.caculate()
        content = {'saPASI': sapsi5, 'Arthritis6': arthritis6, 'PR7': pr7}
    except Exception as e:
        traceback.print_exc()
        Result = 2
        print('err found, please check'),
        print(e)

    if content:
        json_return = content
    json_return['Result'] = Result
    return json.dumps(json_return)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)
