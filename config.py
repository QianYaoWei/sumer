# -*- coding:utf-8 -*-
import logging
import os

# ------------------java
JVMPath = ""
JVMArgs = ""
JavaPkg = ""
# ------------------mysql
DBHost = ""
DBPort = 0
DBName = ""
DBUser = ""
DBPasswd = ""

# 行情文件所在目录
QuoteDir = ""

# ------------------logging
logger = None
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL
LoggingLevel = logging.INFO
LOGPath = os.path.dirname(os.getcwd())
LOGName = 'epsilon.log'


if logger is None:
    logger = logging.getLogger()
    logger.setLevel(LoggingLevel)
    fh = logging.FileHandler(LOGPath + LOGName, mode='a')
    formatter = logging.Formatter("%(asctime)s-%(filename)s[%(levelname)s:%(lineno)d]:%(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
