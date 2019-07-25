# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

from configparser import ConfigParser
import os

# 获取配置信息
def get_config(tag):
	config_path = os.path.join(os.path.dirname(__file__),"config.ini")
	# print(config_path)
	config = ConfigParser()
	config.read(config_path)
	# print(config.sections())

	config_info = {}

	# 获取mail配置
	if tag == "mail":
		config_info["server"] = config["mail"]["server"]
		config_info["user"] = config["mail"]["user"]
		config_info["password"] = config["mail"]["password"]
		config_info["sender"] = config["mail"]["sender"]
		config_info["receivers"] = config["mail"]["receivers"].split(",")
		return config_info

	# 获取database配置
	elif tag == "database":
		config_info["host"] = config["database"]["host"]
		config_info["port"] = eval(config["database"]["port"])
		config_info["user"] = config["database"]["user"]
		config_info["password"] = config["database"]["password"]
		config_info["db"] = config["database"]["db"]
		config_info["charset"] = config["database"]["charset"]
		return config_info

	else:
		raise Exception("参数错误。")


if __name__ == "__main__":
	config_info = get_config("mail")
	print(config_info)
	config_info = get_config("database")
	print(config_info)