# -*- coding:utf-8 -*-
from config import *
import os
import jpype

from .db import db_connection, dolphin, md_reader, TimeRange, get_security_db

from .security import qtlist2mx, load_json_raw


if not jpype.isJVMStarted():
    if not os.path.isfile(JVMPath):
        logger.error("java path invalide!")
    args = [JVMArgs, ]

    if JavaPkg:
        args.append("-Djava.class.path=" + ":".join(JavaPkg))

    print(args)
    jpype.startJVM(JVMPath, *args, convertStrings=False)
