#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午8:42
# @Author  : Aries
# @Site    : 
# @File    : rookk_main.py
# @Software: PyCharm Community Edition
import json
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
        print('err found, please check'),
        print(e)
        Result = 2
    if content:
        json_return = content
    json_return['Result'] = Result
    return json.dumps(json_return)


if __name__ == '__main__':
    app.run(port=2031, debug=True)
