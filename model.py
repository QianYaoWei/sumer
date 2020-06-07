# -*- coding:utf-8 -*-
from config import *
import epsilon
from epsilon import db, pt, sdm, model
import plot


mi = model.ModelInfo()
# mi.tradeDate = '2020-05-29'
mi.tradeDate = '2020-06-03'
mi.serverID = 40
mi.clientID = 58
mi.modelID = 'SHFE.zn'
# mi.configFile = 'test.json'


mc = model.queryModelConfiguration(mi.jtradeDate, mi.jserverID, mi.jclientID)
with open('test.json',  'w') as f1:
    f1.write(str(mc.toString()))


# amc = mi.jAbstractMC
m = model.recoverModel(mi)
c = model.Convertor()
c.addModel(m)
c.inclQuote = False
# c.inclQuote = True 
c.onlyQuoteWithOrders = False
c.nThreads = 1

tu = epsilon.test_utils()
tu.conn()
# reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
reader = tu.dolphinDBReader();
# ids = [s.getSecurityID() for s in m.getTableSecurity()]
# ptList = pt.fetch_ptlist(reader, ids, '2020-06-03')
# for q in ptList:
#     m.__processQuote(q)
m.recoverQuoteData(reader, mi.tradeDate)
smx, omx, mx = model.model2mx(c)

# tbl = model.model2mx(c)



# tu = epsilon.test_utils()
# tu.conn()
# # reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
# reader = tu.dolphinDBReader();
# ptList = pt.fetch_ptlist(reader, [25696], '2020-06-03')
