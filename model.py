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
c.onlyQuoteWithOrders = False
c.nThreads = 1

tu = epsilon.test_utils()
tu.conn()
# reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
reader = tu.dolphinDBReader();

m.recoverQuoteData(reader, mi.tradeDate)
smx, omx, mx = model.model2mx(c)

ids = [s.getSecurityID() for s in m.getTableSecurity()]

# ptmx = mx[(mx.qmtype == 'F') & (mx.secid == ids[0])]

# ptList = pt.fetch_ptlist(reader, ids[0:1], '2020-06-03')

itr = m.getQuote(ids[0])
ptList = jpype.java.util.ArrayList()
while itr.hasNext():
    ptList.add(itr.next())

ptmx = pt.ptlist2mx(ptList, 1)

nosmx = model.nosmx(omx, mx)

ocmx = model.ocmx(omx, mx)

plot.model(nosmx, ocmx, ptmx)

# profit = model.netProfit(mx, 1000)
# nos, oc = plot.model(smx, omx, mx)



# tu = epsilon.test_utils()
# tu.conn()
# # reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
# reader = tu.dolphinDBReader();
# ptList = pt.fetch_ptlist(reader, [25696], '2020-06-03')
