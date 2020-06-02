# -*- coding:utf-8 -*-
import os
import logging
import numpy as np
import pandas as pd
import json
import jpype
import datetime as dt

# ------------------java
JVMPath = "/usr/java/jdk1.8.0_131/jre/lib/amd64/server/libjvm.so"
JVMArgs = "-ea"
JavaPkg = ["/root/tests/sumer/.git/model-jar-with-dependencies.jar","/root/tests/sumer/.git/epsilon-jar-with-dependencies.jar"]

# ------------------mysql
# DBHost = "192.168.10.11"
# DBPort = 3309
# DBName = "epsilon"
# DBUser = "epsilon"
# DBPasswd = "epsilon7777"

DBHost = "127.0.0.1"
DBPort = 3306
DBName = "sumer"
DBUser = "root"
DBPasswd = "root1234"


# ------------------dolphinDB
DolphinHost = "192.168.10.18"
DolphinPort = 8848
DolphinUser = "epsilon"
DolphinPassword = "epsilon7777"
DolphinName = "dfs://md_prod"


# 行情文件所在目录
QuoteDir = "/home/dev/nas_public/json_raw_tapes/cn_fut/"

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


# ------------------sys
STD_MODEL_CONFIG='/root/.jenkins/workspace/epsilon.epsilon_test_config/java_conf/std_model_config.json'
TZ='Asia/Shanghai'



if logger is None:
    logger = logging.getLogger()
    logger.setLevel(LoggingLevel)
    fh = logging.FileHandler(LOGPath + '/' + LOGName, mode='a')
    fh = logging.FileHandler(LOGName, mode='a')
    formatter = logging.Formatter("%(asctime)s-%(filename)s[%(levelname)s:%(lineno)d]:%(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

os.environ["STD_MODEL_CONFIG"] = STD_MODEL_CONFIG
os.environ["TZ"] = TZ


#import imp
#imp.reload(xxx))
