#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from . import db_connection
from config import *
import jpype

_fields = ['tradedate', 'time', 'origtime', 'mtype', 'secid',
        'dfid', 'qmtype', 'bid', 'bsz', 'ask', 'asz', 'lastpx',
        'lastsz', 'lastamt', 'oin', 'ttvol', 'ttamt']

# 'wmp'

def qtlist2mx(qtList, depth):
    df = pd.DataFrame(columns=_fields)
    afu = jpype.JPackage("clover.model.analysisframework").AnalysisFrameworkUtil
    qArray = afu.quoteList2quoteObjArray(qtList, depth)

    for i, v in enumerate(_fields):
        df[v] = afu.getQuoteField(qArray, _fields[i], jpype.JInt(depth))

    return df

    # df.wmp = t_quote.bid(:,1) + (t_quote.ask(:,1)-t_quote.bid(:,1)).*t_quote.bsz(:,1)./(t_quote.bsz(:,1)+t_quote.asz(:,1));


def load_json_raw(fpath, sids, depth, filterOutBadQuotes=True, tradeDate="2020-05-08"):
    ids = jpype.JArray(jpype.JInt)([])
    if sids:
        ids = jpype.JArray(jpype.JInt)(sids)

    mdu = jpype.JPackage("clover.epsilon.marketdata").MarketDataUtil
    qcList = mdu.jsonRawToQuoteCList(jpype.JString(fpath), ids, jpype.JBoolean(filterOutBadQuotes))

    qtList = mdu.quoteC2quotePT(qcList, db_connection(), jpype.JString(tradeDate))


    return qtlist2mx(qtList, depth)


if __name__ == "__main__":
    pass
