#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .util import *

class vacations(object):
    _vacations = {
        "2020": {
            # 假期
            "vacations": [
                # dt.date.fromtimestamp()
                # 元旦
                "01-01", 
                # 春节
                "01-24~02-02", 
                # 清明
                "04-04~04-06", 
                # 劳动节
                "05-01~05-05", 
                # 端午节
                "06-25~06-27", 
                # 中秋节
                # 国庆节
                "10-01~10-08"
            ],

            "skip": {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },

            ExchangerID_SHFE: {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },

            ExchangerID_DCE: {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },

            ExchangerID_INE: {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },

            ExchangerID_CZCE: {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },

            ExchangerID_CFFEX: {
                Session_Night:    [],
                Session_Morning1: [],
                Session_Morning2: [],
                Session_Noon:     []
            },
        },
    }


    @classmethod
    @timestamp2dt
    def is_vacation(cls, t):
        '''
            t is instance of datetime.datetime
        '''
        y = str(t.year)
        if y not in cls._vacations:
            # 没配置
            return False

        d = "%02d02d"%(t.month, t.day)
        for v in cls._vacations[y]["vacations"]:
            l = v.split("~")
            if len(l) == 1 and d == l[0]:
                return True
            elif len(l) == 2 and l[0] <= d <= l[1]:
                return True

        return False


    @classmethod
    @timestamp2dt
    def is_free(cls, t):
        if is_weekend(t) or cls.is_vacation(t):
            return True
        return False


    @classmethod
    @timestamp2dt(2)
    def is_session_skipped(cls, ex, session, t):
        if cls.is_free(t):
            return True

        y = str(t.year)
        if y not in cls._vacations or ex not in cls._vacations[y]:
            # 没配置
            return True
        
        d = "%02d02d"%(t.month, t.day)
        if d in cls._vacations[y][ex][session]:
            return True

        return False


    @classmethod
    @timestamp2dt
    def has_vacation_inbetween(cls, t1, t2):
        '''
            t1, t2 is instance of datetime.datetime
        '''
        if t2 <= t1:
            return False

        while t2 > t1:
            if cls.is_vacation(t2):
                return True
            t2 -= dt.timedelta(days=1)
        return False


if __name__ == "__main__":
    pass
