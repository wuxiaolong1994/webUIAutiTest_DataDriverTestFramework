# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

# import os,sys
# _path = __file__.split("website")[0]
# sys.path.append(_path)

import unittest
from driver.open_browser import *
from driver.functions import *
import ddt

class MyUnit(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		logging_init(logging.INFO)
		cls.driver = openBrowser()
		logging.debug("打开浏览器")

		cls.driver.maximize_window()

		# cls.driver.implicitly_wait(10)
		# logging.debug("设置隐式等待10s")

		print("开始执行测试用例")
		

	def setUp(self):
		print("setUp")

	def tearDown(self):
		print("tearDown")

	@classmethod
	def tearDownClass(cls):
		print("测试结束")
		cls.driver.quit()


