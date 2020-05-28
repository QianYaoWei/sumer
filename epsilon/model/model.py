# -*- coding:utf-8 -*-
from config import *


class ModelInfo(object):

    def __init__(self):
        self.tradeDate = ""
        self.serverID = 0
        self.clientID = 0
        self.modelID = 0
        self.modelSetup = ""
        self.className = ""


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
        return jpype.JInt(self.modelID)


    @property
    def jmodelSetup(self):
        return jpype.JString(self.modelSetup)


    @property
    def jclassName(self):
        return jpype.JString(self.className)



def recoverModel(mi):
    mau = jpype.JPackage("clover.model.analysis2").ModelAnalysisUtils
    model = mau.recoverModel(db_connection(), mi.jtradeDate, mi.jserverID,\
                            mi.jclientID, jmodelID, jmodelSetup,\
                            jpype.JString(""), jclassName)
    return model


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
    afum = jpype.JPackage("clover.model.analysisframework").AnalysisFrameworkUtilMT
    return afum.modelList2table2(c.jmodelList, c.jdepth, c.jinclQuote, c.jonlyQuoteWithOrders, c.jnThreads)
