import unittest

import time
from HTMLTestRunner import HTMLTestRunner

dis = unittest.defaultTestLoader.discover("./", "login.py")

timestr = time.strftime("%Y/%m/%d/%H/%M/%S")

with open("./接口测试报告" + timestr + ".html", "wb") as f:
    run = HTMLTestRunner(f)
    run.run(dis)
