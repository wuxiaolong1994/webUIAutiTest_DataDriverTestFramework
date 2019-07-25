# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong


import os,sys
_path = __file__.split("website")[0]
sys.path.append(_path)

import time
import unittest
from selenium import webdriver
from website.model.myunit import *



class Assert(MyUnit):

	def assert_page(self,target,method,sentence,element=False):
		if not element:
			if target == "url":
				source = self.driver.current_url
			elif target == "title":
				source = self.driver.title
			elif target == "text":
				source = self.driver.page_source
			else:
				raise Exception("请确认test_data.xlsx数据是否正确")
		else:
			if target == "value":
				source = element.get_atribute("value")
			elif target == "text":
				source = element.text
			else:
				raise Exception("请确认test_data.xlsx数据是否正确")

		if method == "equal":
			return self.assertEqual(sentence,source)
		elif method == "contain":
			return self.assertIn(sentence,source)
		elif method == "not equal":
			return self.assertNotEqual(sentence,source)
		elif method == "not contain":
			return self.assertNotIn(sentence,source)
		else:
			raise Exception("请确认test_data.xlsx数据是否正确")






