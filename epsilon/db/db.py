# -*- coding:utf-8 -*-
from config import *

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



#def md_reader(ftype, rtype):
#    '''
#    -------------------------------------------
#    ftype:
#        JavaSerialT
#        Kryo.IQuotePT
#        JavaSerialPT
#    rtype
#        mdreader.SHFE
#        mdreader.CFFEX
#        mdreader.xxx...
#    '''
#    return jpype.JPackage("clover.epsilon.util").TestUtils.createMDReader(ftype, rtype)



class TimeRange(object):
    def __init__(self):
        # startdate
        self._sdt = None
        # self._sdt = dt.date.today() - dt.timedelta(1)

        # enddate
        self._edt = None
        # self._edt = dt.date.today()

        self._day = -1

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
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    @property
    def inv(self):
        return self._interval

    @inv.setter
    def inv(self, inv):
        self._interval = inv


def get_quote_db(secs, tr, reader):
    '''
    sdt(string)
    edt(string)
    -------------------------------------------
    secs: itr(int) or itr(dict)
    tr: TimeRange
    interval: millisec (int)
    '''
    if type(secs[0]) == int:
        jsecs = jpype.JArray(jpype.JInt)(secs)
    elif type(secs[0]) == dict:
        jsecs = [json.dumps(s) for s in secs]
        jsecs = jpype.JArray(jpype.JString)(jsecs)
    else:
        return None

    if not isinstance(tr, TimeRange):
        return None

    jpkg = jpype.JPackage("clover.model.matlab")
    sdm = jpkg.SecurityDataMatrixPT()
    if tr.sdt and tr.edt:
        sdt = jpype.JString(tr.sdt.strftime("%Y-%m-%d"))
        edt = jpype.JString(tr.edt.strftime("%Y-%m-%d"))
        inv = jpype.JInt(tr.inv)
        rets = jpkg.SecurityDataMatrixPT.generateSDMDataDef_CN(db_connection(), jsecs, sdt, edt, inv)
        sdm.fetchData(rets, reader, tr.inv)
    elif tr.edt and tr.day < 0:
        day = jpype.JInt(tr.day)
        edt = jpype.JString(tr.edt.strftime("%Y-%m-%d"))
        inv = jpype.JInt(tr.inv)
        rets = jpkg.SecurityDataMatrixPT.generateSDMDataDef_CN(db_connection(), jsecs, day, edt, inv)
        sdm.fetchData(rets, reader, tr.inv)
    return sdm


if __name__ == "__main__":
    pass
