import unittest

import time
from HTMLTestRunner import HTMLTestRunner

dis = unittest.defaultTestLoader.discover("./", "login.py")

timestr = time.strftime("%Y年%m月%d日%H时%M分%S秒")

with open("./接口测试报告" + timestr + ".html", "wb") as f:
    run = HTMLTestRunner(f)
    run.run(dis)
