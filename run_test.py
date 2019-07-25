# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

import unittest
from HTMLTestRunnerCN import HTMLTestRunner
from driver.functions import *
import os

report_dir = os.path.abspath("./test_result/test_report")
test_dir = "./test_case"

discovery = unittest.defaultTestLoader.discover(test_dir,pattern="test_001_tap_menus.py")

now = get_time()
report_name = now + "_report.html"

report_full_path = os.path.join(report_dir,report_name)

with open(report_full_path,"wb") as file:
	runner = HTMLTestRunner(stream=file,
		title="极客数学帮web自动化测试",
		description="在首页点击顶部菜单栏各选项，验证是否可正常跳转，及跳转页面是否正确",
		tester="吴小龙")
	runner.run(discovery)


send_report(now)

print("测试完成")