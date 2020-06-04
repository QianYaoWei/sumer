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

smx, omx, mx = model.model2mx(c)
