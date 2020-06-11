# -*- coding:utf-8 -*-
from config import *
from ..db import *

from .msg import msg
from .order import order
from .quote import quote
from .sec import sec
from .msgquote import msgquote


class ModelInfo(object):

    def __init__(self):

        self.tradeDate = ""

        self.serverID = 0

        self.clientID = 0

        self.modelID = 0

        self.configFile = ""


    @property
    def jtradeDate(self):
        return jpype.JString(self.tradeDate)


    @property
    def jserverID(self):
        return jpype.JInt(self.serverID)


    @property
    def jclientID(self):
        return jpype.JInt(self.clientID)


    @property
    def jmodelID(self):
        return jpype.JString(self.modelID)


    @property
    def jAbstractMC(self):
        jpkg = jpype.JPackage('clover.epsilon.util')
        jpkg2 = jpype.JPackage('clover.epsilon.model_pt')
        jpkg3 = jpype.JPackage('clover.epsilon.database')
        
        if self.configFile:
            node = jpkg.Json.parseFile(jpype.JString(self.configFile))
            mc = jpkg.Json.parse(node.toString(), jpkg3.ModelConfiguration)
            amc = jpkg.Json.parse(mc.model.get(0).toString(), jpkg2.AbstractModelConfig)
            # TODO
            amc.root = node
            amc.conn = db_connection()
            amc.clientID = mc.clientID;
            amc.tradeDate = mc.tradeDate;

            return amc
        else:
            mc = queryModelConfiguration(self.jtradeDate, self.jserverID, self.jclientID)
            amc = jpkg.Json.parse(mc.model.get(0).toString(), jpkg2.AbstractModelConfig)
            # TODO
            amc.root = jpkg.Json.parse(mc.toString())
            amc.conn = db_connection()
            amc.clientID = mc.clientID;
            amc.tradeDate = mc.tradeDate;

            return amc



def recoverModel(mi):
    if isinstance(mi, ModelInfo):
        amc = mi.jAbstractMC
        mi.conn = db_connection()

        logger = jpype.JPackage('clover.epsilon.util').TestUtils.getDefaultLogger()
        jpkg = jpype.JPackage('clover.epsilon.model_pt')
        model = jpkg.ReadOnlyModelPT(mi.jtradeDate, amc, mi.jmodelID, logger);
        # pair = jpkg.ModelPTUtils.queryPrivateMessageOfModel(db_connection(), mi.jtradeDate, mi.jserverID, mi.jclientID, mi.jmodelID)
        # model.recoverModelFromOrderMessages(db_connection(), mi.jserverID, pair.getLeft(), pair.getRight())

        model.recoverModelFromDatabase(db_connection(), db_connection(), mi.jserverID, amc.brokers)
        return model

    return None



def queryModelConfiguration(tradeDate, sid, cid):
    jpkg = jpype.JPackage('clover.epsilon.database')
    mc = jpkg.DatabaseUtil.queryModelConfiguration(db_connection(),\
            jpype.JString(tradeDate),\
            jpype.JInt(sid),\
            jpype.JInt(cid))

    return mc
    # return mc.toString()



class Convertor(object):
    def __init__(self):
        self.modelList = []
        self.depth = 1
        self.inclQuote = True
        self.onlyQuoteWithOrders = False
        self.nThreads = 1

    def addModel(self, model):
        self.modelList.append(model)


    @property
    def jmodelList(self):
        return jpype.java.util.ArrayList(self.modelList)


    @property
    def jdepth(self):
        return jpype.JInt(self.depth)


    @property
    def jinclQuote(self):
        return jpype.JBoolean(self.inclQuote)


    @property
    def jonlyQuoteWithOrders(self):
        return jpype.JBoolean(self.onlyQuoteWithOrders)


    @property
    def jnThreads(self):
        return jpype.JInt(self.nThreads)


def model2mx(c):
    if isinstance(c, Convertor):
        afum = jpype.JPackage("clover.model.analysisframework").AnalysisFrameworkUtilMT
        tbl = afum.modelList2table2(c.jmodelList, c.jdepth, c.jinclQuote, c.jonlyQuoteWithOrders, c.jnThreads)
        # return tbl

        smx = sec.sec2mx(tbl.t_sec)

        omx = order.order2mx(tbl.t_ord)
        # 为了兼容, 这里索引从1开始
        omx.index = np.arange(1, len(omx) + 1)

        if c.inclQuote:
            mx = msgquote.msgquote2mx(tbl.t_msg)
        else:
            mx = msg.msg2mx(tbl.t_msg)

        # 为了兼容, 这里索引从1开始
        mx.index = np.arange(1, len(mx) + 1)
        return (smx, omx, mx)

    return None


def nosmx(omx, mx):
    orderMX = omx[omx.ordid >= 0]
    nos = pd.DataFrame(columns=["ordid", "side", "poseff", "price", "qty", "time", "executed", "wmp"])

    nos["ordid"] = orderMX.ordid
    nos["side"] = orderMX.side
    nos["poseff"] = orderMX.poseff
    nos["price"] = orderMX.price
    nos["qty"] = orderMX.qty
    nos["executed"] = orderMX.executed
    oids = orderMX.reqs.apply(lambda e: e[0])
    nos["time"] = mx.loc[oids].time.values
    nos["wmp"] = mx.loc[oids].wmp.values
    return nos


def ocmx(omx, mx):
    orderMX = omx[omx.ordid >= 0]
    oc = pd.DataFrame(columns=["ordid", "time", "wmp"])

    cfilter = orderMX.reqs.apply(lambda e: len(e) >= 2)
    cids = orderMX.loc[cfilter].reqs.apply(lambda e: e[1])
    oc["ordid"] = orderMX.loc[cfilter].ordid
    oc["time"] = mx.loc[cids].time.values
    oc["wmp"] = mx.loc[cids].wmp.values
    return oc


def netProfit(mx, sec, px=0):
    
    fillMX = mx[(mx.fillpx > 0) & (mx.ordid >= 0)]
    netPos = fillMX.poschg.sum()
    posValue = netPos * px

    commission = fillMX.comm.sum()
    return posValue - (sec.multiplier * sec.minpxincr) * (fillMX.poschg * fillMX.fillpx).sum() - commission
