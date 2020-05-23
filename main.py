# -*- coding:utf-8 -*-
import epsilon
import jpype
import numpy as np
import pandas as pd
import plot
import datetime as dt


#secs = [{"SecurityExchange": "SHFE", "Symbol": "fu", "MaturityMonthYear": "202009"
#    }]

secs = [
    {"SecurityExchange": "SHFE", "Symbol": "au", "MaturityMonthYear": "202012" },
    {"SecurityExchange": "SHFE", "Symbol": "fu", "MaturityMonthYear": "202009" }
]



secList = epsilon.get_sec_objs(secs);
secIDs = [s.getSecurityID() for s in secList]

#qt = epsilon.fetch_qtlist_file('/root/tests/aa.json', secIDs)
#mx = epsilon.qtlist2mx(qt, 1)


#tu = epsilon.test_utils()
#tu.conn()
## reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
#reader = tu.dolphinDBReader();
#qt = epsilon.fetch_qtlist(reader, secIDs, '2020-05-20')
#mx = epsilon.qtlist2mx(qt, 1)

incrPriceList = [s.getMinPriceIncrement() for s in secList]


tu = epsilon.test_utils()
tu.conn()
reader = tu.dolphinDBReader();

tr = epsilon.TimeRange()
tr.edt = dt.date(year=2020, month=5, day=20)
tr.day = -1
sdm = epsilon.get_quote_db(secs, tr, reader)
