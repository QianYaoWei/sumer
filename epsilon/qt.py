#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from config import *
from . import db_connection

_fields = ['tradedate', 'time', 'origtime', 'mtype', 'secid',
            'dfid', 'qmtype', 'bid', 'bsz', 'ask', 'asz', 'lastpx',
            'lastsz', 'lastamt', 'oin', 'ttvol', 'ttamt']

def qtlist2mx(qtList, depth):
    df = pd.DataFrame(columns=_fields)
    afu = jpype.JPackage('clover.model.analysisframework').AnalysisFrameworkUtil
    qArray = afu.quoteList2quoteObjArray(qtList, depth)

    for i, v in enumerate(_fields):
        df[v] = afu.getQuoteField(qArray, _fields[i], jpype.JInt(depth))

    df.origtime = df.origtime / 1000000
    # df.time = pd.to_datetime(df.time, unit='ns');
    # df.origtime = pd.to_datetime(df.origtime, unit='ns');
    # df.origtime = df.origtime.apply(lambda e: pd.Timestamp(e, unit='ns', tz='Asia/Shanghai'))
    f = lambda e: e[0]
    df['bid0'] = df.bid.apply(f)
    df['bsz0'] = df.bsz.apply(f)
    df['ask0'] = df.ask.apply(f)
    df['asz0'] = df.asz.apply(f)
    df['wmp'] = df.bid0 + (df.ask0 - df.bid0) * df.bsz0 / (df.bsz0 + df.asz0)

    df.index = df.origtime
    return df



def fetch_qtlist(reader, sids, tradeDate):
    #createJsonQuoteCMDReader(jpype.JString('/market_data/json_raw_cn_fut'))
    if sids:
        sids = jpype.JArray(jpype.JInt)(sids)
        return reader.getQuoteList(jpype.JString(tradeDate), sids)
    else:
        return reader.getQuoteList(jpype.JString(tradeDate))


def fetch_qtlist_file(fpath, sids, tradeDate='2020-05-08'):

    '''tradeDate 该字段只用于取到最小变动单位'''
    ids = jpype.JArray(jpype.JInt)([])
    if sids:
        ids = jpype.JArray(jpype.JInt)(sids)
    mdu = jpype.JPackage('clover.epsilon.marketdata').MarketDataUtil
    qcList = mdu.jsonRawToQuoteCList(jpype.JString(fpath), ids, jpype.JBoolean(True))
    qtList = mdu.quoteC2quotePT(qcList, db_connection(), jpype.JString(tradeDate))
    return qtList


def get_sec_objs(secs, tradeDate='2020-05-08'):
    '''
        secs-> [
            {"SecurityExchange": "DCE", "Symbol": "p", "MaturitySequence": "+1"},
            {"SecurityExchange": "CFFEX", "Symbol": "IF", "MaturityMonthYear": "201705"}
        ]
    '''
    util = jpype.JPackage('clover.model.util')
    mu = util.ModelUtils

    return [mu.parseSecurity(db_connection(),\
            jpype.JString(tradeDate),\
            util.Json.parse(json.dumps(s)))\
            for s in secs]



if __name__ == '__main__':
    pass
