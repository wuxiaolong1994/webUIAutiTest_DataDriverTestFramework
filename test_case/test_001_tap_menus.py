# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong



# import os,sys
# _path = __file__.split("test_case")[0]
# sys.path.append(_path)

import ddt
from driver.functions import *
from website.model.myassert import *
from driver.read_test_data import ReadTestData
from website.page_object.jike_main import *
from selenium.common.exceptions import NoSuchElementException
import traceback
import logging


test_data_file = os.path.join(__file__.split("test_case")[0],r"test_data\test_data.xlsx")
sheet = ReadTestData(test_data_file,"top_menus")

@ddt.ddt
class TestTapTopMenus(Assert):
	
	@ddt.data(*sheet.get_data())
	@ddt.unpack
	def test_001_TapTopMenus(self,action,assert_target,assert_method,assert_keywords):
		self.main_page= MainPage(self.driver)
		try:
			action = "self.main_page." + action + "()"
			# print(action)
			eval(action)
			logging.info("执行%s"%action)
			time.sleep(1)

			# first_handle = self.driver.current_window_handle
			# all_handle = self.driver.window_handles

			# self.driver.switch_to.window(all_handle[1])
			# logging.debug("切换至新窗口")

			self.assert_page(assert_target,assert_method,assert_keywords)
			# time.sleep(2)

			now_time = get_time()
			file_description = action.split(".")[-1] + "_" + now_time
			get_screenshot(self.driver,file_description)
			# self.driver.close()
			# logging.debug("关闭新窗口")

			# self.driver.switch_to.window(first_handle)
			time.sleep(1)

			logging.info("%s pass"%action)

		except NoSuchElementException as e:
			logging.warning("%s error"%action)
			logging.info("元素未找到，错误信息：%s"%traceback.format_exc())
			raise e
		except AssertionError as e:
			logging.error("%s failed"%action)
			logging.error("断言错误，错误信息：%s"%traceback.format_exc())
			raise e
		except Exception as e:
			logging.info("未知错误，错误信息：%s"%traceback.format_exc())
			raise e




