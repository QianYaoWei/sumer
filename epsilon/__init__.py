# -*- coding:utf-8 -*-
from ..config import *
import os
import jpype
import datetime as dt
import json


if not jpype.isJVMStarted():
    if not os.path.isfile(JVMPath):
        logger.error("java path invalide!")
    args = list(JVMArgs)
    if JavaPkg:
            args.append("-Djava.class.path=" + ";".join(JavaPkg))

    jpype.startJVM(JVMPath, *args)


def db_host():
    return "jdbc:mysql://" + DBHost + ":" + str(DBPort) + "/" + DBName


_con = None


def db_connection():
    global _con
    if _con is None:
        jpckg = jpype.JPackage("java.sql")
        _con = jpckg.DriverManager.getConnection(db_host(), DBUser, DBPasswd)
        return _con
    else:
        return _con


def md_reader(ftype, rtype):
    # -------------------------------------------
    # ftype:
    #     JavaSerialT
    #     Kryo.IQuotePT
    #     JavaSerialPT
    # rtype
    #     mdreader.SHFE
    #     mdreader.CFFEX
    #     mdreader.xxx...
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
    def edt(self):
        return self._interval

    @edt.setter
    def edt(self, inv):
        self._interval = inv


def get_security_db(secList, tr, rtype='JavaSerialPT', ftype='mdreader.SHFE'):
    # sdt(string)
    # edt(string)
    # -------------------------------------------
    # secs: itr(int) or itr(dict)
    # tr: TimeRange
    # interval: millisec (int)
    reader = md_reader(ftype, rtype)
    if secList[0] is int:
        jsecs = jpype.JArray(jpype.JInt)(secList)
    elif secList[0] is dict:
        jsecs = [json.dumps(s) for s in secList]
        jsecs = jpype.JArray(jpype.JString)(jsecs)
    else:
        return None

    sdt = tr.sdt.strftime("%Y-%m-%d")
    edt = tr.edt.strftime("%Y-%m-%d")
    jpkg = jpype.JPackage("clover.model.matlab")
    sdm = jpkg.SecurityDataMatrixPT()
    rets = jpkg.SecurityDataMatrixPT.generateSDMDataDef_CN(db_connection(), jsecs, sdt, edt, tr.inv)
    sdm.fetchData(rets, reader, tr.inv)
    return sdm


if __name__ == "__main__":
    pass
