# -*- coding:utf-8 -*-
import epsilon
from epsilon import db, pt, sdm

import jpype
import numpy as np
import pandas as pd
import datetime as dt

import plot


#secs = [{"SecurityExchange": "SHFE", "Symbol": "fu", "MaturityMonthYear": "202009"
#    }]

secs = [
    {"SecurityExchange": "SHFE", "Symbol": "au", "MaturityMonthYear": "202012" },
    #{"SecurityExchange": "SHFE", "Symbol": "fu", "MaturityMonthYear": "202009" }
]



secList = pt.get_sec_objs(secs);
secIDs = [s.getSecurityID() for s in secList]

#pt = pt.fetch_ptlist_file('/root/tests/aa.json', secIDs)
#mx = pt.ptlist2mx(pt, 1)


#tu = epsilon.test_utils()
#tu.conn()
## reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
#reader = tu.dolphinDBReader();
#pt = epsilon.fetch_ptlist(reader, secIDs, '2020-05-20')
#mx = epsilon.ptlist2mx(pt, 1)

incrPriceList = [s.getMinPriceIncrement() for s in secList]


tu = epsilon.test_utils()
tu.conn()
reader = tu.dolphinDBReader();

tr = db.TimeRange()
tr.edt = dt.date(year=2020, month=5, day=20)
tr.day = -1

m = db.get_quote_db(secs, tr, reader)
