#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午8:54
# @Author  : Aries
# @Site    : 
# @File    : caculate.py
# @Software: PyCharm Community Edition


class CaculateRisk(object):

    def __init__(self, request_json):
        self.request_json = request_json

    @property
    def wx_name(self):
        return self.request_json['WX']

    @property
    def phone_num(self):
        return self.request_json['PhoneNum']

    @property
    def id_num(self):
        return self.request_json['IDNum']

    @property
    def name(self):
        return self.request_json['Name']

    @property
    def nick_name(self):
        return self.request_json['NickName']

    @property
    def sex(self):
        if self.request_json['Sex'] == 0:
            sex = '女'
        elif self.request_json['Sex'] == 1:
            sex = '男'
        else:
            sex = ''
        return sex

    @property
    def birthday(self):
        return self.request_json['Birthday']

    @property
    def height(self):
        return self.request_json['Height']

    @property
    def weight(self):
        return self.request_json['Weight']

    @property
    def incidence_time(self):
        return self.request_json['IncidenceTime']

    @property
    def sapasi1(self):
        return int(self.request_json['saPASI1'])

    @property
    def sapasi2(self):
        return int(self.request_json['saPASI2'])

    @property
    def sapasi3(self):
        return int(self.request_json['saPASI3'])

    @property
    def sapasi4(self):
        return int(self.request_json['saPASI4'])

    @property
    def sapasi5(self):
        return self.sapasi1 * (self.sapasi2 + self.sapasi3 + self.sapasi4)

    @property
    def quilityoflife(self):
        return self.request_json['QualityOfLife']

    @property
    def arthritis1(self):
        return int(self.request_json['Arthritis1'])

    @property
    def arthritis2(self):
        return int(self.request_json['Arthritis2'])

    @property
    def arthritis3(self):
        return int(self.request_json['Arthritis3'])

    @property
    def arthritis4(self):
        return int(self.request_json['Arthritis4'])

    @property
    def arthritis5(self):
        return int(self.request_json['Arthritis5'])

    @property
    def arthritis6(self):
        return self.arthritis1 + self.arthritis2 + self.arthritis3 + self.arthritis4 + self.arthritis5

    @property
    def risk1(self):
        if not self.request_json['PR1']:
            return ''
        val = int(self.request_json['PR1'])
        if val > 3:
            return 0.22
        elif val < 3:
            return 1
        else:
            return 0.3

    @property
    def risk2(self):
        return self.arthritis3 * 2.51

    @property
    def risk3(self):
        if self.sapasi5 > 20:
            risk = 5.39
        elif self.sapasi5 < 10:
            risk = 1
        else:
            risk = 1.16
        return risk

    @property
    def risk4(self):
        if not self.request_json['PR4']:
            return ''
        return int(self.request_json['PR4']) * 3.42

    @property
    def risk5(self):
        if not self.request_json['PR5']:
            return ''
        return int(self.request_json['PR5']) * 31.5

    @property
    def risk6(self):
        percent = float(self.weight) * 10000 / (float(self.height) * float(self.height))
        if percent > 27:
            # 肥胖
            return 2.03
        elif 23.0 < percent < 28:
            return 1.02
        else:
            return 0

    @property
    def risk7(self):
        if self.risk4 != '' and self.risk5 != '' and self.risk1 != '':
            risk = self.risk1 + self.risk2 + self.risk3 + self.risk4 + self.risk5 + self.risk6
            return risk
        else:
            return None

    def caculate(self):
        return self.sapasi5, self.arthritis6, self.risk7

    def content(self):
        return [
            self.wx_name, self.phone_num, self.id_num, self.name, self.nick_name, self.sex, self.birthday,
            self.height, self.weight, self.incidence_time, self.sapasi1, self.sapasi2, self.sapasi3,
            self.sapasi4, self.sapasi5, self.quilityoflife, self.arthritis1, self.arthritis2, self.arthritis3,
            self.arthritis4, self.arthritis5, self.arthritis6, self.risk1, self.risk2, self.risk3, self.risk4,
            self.risk5, self.risk6, self.risk7
        ]
