#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime as dt


_shfe = {
    "session": {
        Session_Morning1: ["09:00:00",    "10:15:00"],
        Session_Morning2: ["10:30:00",    "11:30:00"],
        Session_Noon:     ["13:30:00",    "15:00:00"],
        Session_Night:    None
    }

    # 银
    "ag": {
        Session_Night:    ["-21:00:00",   "02:30:00"],
    },

    # 铝
    "al": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },

    # 金
    "au": {
        Session_Night:    ["-21:00:00",   "02:30:00"],
    },

    # 石油沥青
    "bu": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 铜
    "cu": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },


    # 燃料油
    "fu": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 热轧卷板
    "hc": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },


    # 镍
    "ni": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },


    # 铅
    "pb": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },


    # 螺纹钢
    "rb": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 天然橡胶
    "ru": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 锡
    "sn": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },


    # 纸浆
    "sp": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 不锈钢
    "ss": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },

    # 线材 
    "wr": {
        Session_Night:    ["-21:00:00",   "-23:00:00"],
    },

    # 锌
    "zn": {
        Session_Night:    ["-21:00:00",   "01:00:00"],
    },
}


def nearest_time(st, timeStr):
    '''
        st: startTime is instance of datetime.datetime
    '''
    if timeStr[0] == '-':
        t = dt.datetime.combine(st.date(), dt.time.fromtimestamp(timeStr[1:]))
        t -= dt.timedelta(days=1)
    else:
        t = dt.datetime.combine(st.date(), dt.time.fromtimestamp(timeStr[1:]))

    while True:
        if is_vacation(t):
            t -= dt.timedelta(days=1)
        elif is_weekend(t):
            t -= dt.timedelta(days=1)
        else:
            return t


def get_trading_session(symbol, t, timeStr):
    '''
        timeStr: "12:00:00"

        return [Session_Night,     stime, etime, 
                Session_Morning1,  stime, etime
                Session_Morning2,  stime, etime
                Session_Noon,      stime, etime]

        stime, etime: seconds

    '''
    if symbol not in _shfe:
        return None

    if is_free(t):
        return None

    # 过滤掉被skip的session
    sids = [s for s in _shfe["session"].keys() if not is_session_skipped(ExchangerID_SHFE, s, t)]

    sessions = []
    for s in sids:
        if s in _shfe[symbol]:
            tlist = [nearest_time(t, timeStr) for timeStr in _shfe[symbol][s]]
            sessions.extend([s].extend(tlist))
        else:
            tlist = [nearest_time(t, timeStr) for timeStr in _shfe["session"][s]]
            sessions.extend([s].extend(tlist))

    return sessions
