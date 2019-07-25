# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

from selenium import webdriver

def openBrowser():
	driver = webdriver.Chrome()
	# driver = webdriver.Firefox()
	# driver = webdriver.Ie()
	return driver
