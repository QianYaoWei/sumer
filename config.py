# -*- coding:utf-8 -*-
import logging
import os

# ------------------java
JVMPath = "/usr/java/jdk1.8.0_131/jre/lib/amd64/server/libjvm.so"
JVMArgs = "-ea"
JavaPkg = ["/root/.jenkins/workspace/model-jar-with-dependencies.jar","/root/.jenkins/workspace/epsilon-jar-with-dependencies.jar"]
# ------------------mysql
DBHost = "192.168.10.11"
DBPort = 3309
DBName = "epsilon"
DBUser = "epsilon"
DBPasswd = "epsilon7777"


# ------------------dolphinDB
DolphinHost = "192.168.10.18"
DolphinPort = 8848
DolphinUser = "epsilon"
DolphinPassword = "epsilon7777"
DolphinName = "dfs://md_prod"


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
