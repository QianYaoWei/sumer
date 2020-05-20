# -*- coding:utf-8 -*-
from config import *
import json
import datetime as dt
import jpype

def db_host():
    return "jdbc:mysql://" + DBHost + ":" + str(DBPort) + "/" + DBName


_dbcon = None


def db_connection():
    global _dbcon
    if _dbcon is None:
        jpckg = jpype.JPackage("java.sql")
        _dbcon = jpckg.DriverManager.getConnection(db_host(), DBUser, DBPasswd)
        return _dbcon
    else:
        return _dbcon


_dophinDB4Matlab = None


def dolphin():
    global _dophinDB4Matlab
    if _dophinDB4Matlab is None:
        jpckg = jpype.JPackage("clover.epsilon.dolphinDB")
        _dophinDB4Matlab = jpckg.DophinDB4Matlab(DolphinHost, DolphinPort, DolphinUser, DolphinPassword, DolphinName)
        return _dophinDB4Matlab
    else:
        return _dophinDB4Matlab



def md_reader(ftype, rtype):
    '''
    -------------------------------------------
    ftype:
        JavaSerialT
        Kryo.IQuotePT
        JavaSerialPT
    rtype
        mdreader.SHFE
        mdreader.CFFEX
        mdreader.xxx...
    '''
    return jpype.JPackage("clover.epsilon.util").TestUtils.createMDReader(ftype, rtype)



class TimeRange(object):
    def __init__(self):
        # startdate
        self._sdt = dt.date.today() - dt.timedelta(1)
        # enddate
        self._edt = dt.date.today()
        # tick interval
        self._interval = 500

    def __str__(self):
        return ','.join([str(self._sdt),str(self._edt),str(self._interval)])

    @property
    def sdt(self):
        return self._sdt

    @sdt.setter
    def sdt(self, sdt):
        self._sdt = sdt

    @property
    def edt(self):
        return self._edt

    @edt.setter
    def edt(self, edt):
        self._edt = edt

    @property
    def inv(self):
        return self._interval

    @edt.setter
    def inv(self, inv):
        self._interval = inv


def get_security_db(secList, tr, rtype='JavaSerialPT', ftype='mdreader.SHFE'):
    '''
    sdt(string)
    edt(string)
    -------------------------------------------
    secs: itr(int) or itr(dict)
    tr: TimeRange
    interval: millisec (int)
    '''
    reader = md_reader(ftype, rtype)
    if secList[0] is int:
        jsecs = jpype.JArray(jpype.JInt)(secList)
    elif secList[0] is dict:
        jsecs = [json.dumps(s) for s in secList]
        jsecs = jpype.JArray(jpype.JString)(jsecs)
    else:
        return None

    sdt = jpype.JString(tr.sdt.strftime("%Y-%m-%d"))
    edt = jpype.JString(tr.edt.strftime("%Y-%m-%d"))
    jpkg = jpype.JPackage("clover.model.matlab")
    sdm = jpkg.SecurityDataMatrixPT()
    rets = jpkg.SecurityDataMatrixPT.generateSDMDataDef_CN(db_connection(), jsecs, sdt, edt, jpype.JInt(tr.inv))
    sdm.fetchData(rets, reader, tr.inv)
    return sdm


if __name__ == "__main__":
    pass
