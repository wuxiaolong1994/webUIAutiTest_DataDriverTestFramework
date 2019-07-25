# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

import time

class Page():
	def __init__(self,driver):
		self.driver = driver
		self.base_url = "http://www.shuxuebang.com"
		self.timeout = 10
		url_ = self.base_url + self.url
		self.driver.get(url_)

	def _open(self,url):
		_url = self.base_url + url
		self.driver.maximize_window()
		self.driver.get(_url)
		time.sleep(2)

	def open(self):
		self._open(self.url)


	def find_element(self,*locator):
		return self.driver.find_element(*locator)


	def find_elements(self,*locator):
		return self.driver.find_elements(*locator)