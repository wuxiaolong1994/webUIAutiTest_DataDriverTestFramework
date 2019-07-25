# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

from driver.read_config import *
from driver.sql import *
import pymysql

class DatabaseInit():
	def __init__(self):
		db_config = get_config("database")
		self.host = db_config["host"]
		self.port = db_config["port"]
		self.user = db_config["user"]
		self.password = db_config["password"]
		self.db = db_config["db"]
		self.charset = db_config["charset"]

	def _connect(self):
		self.connection = pymysql.connect(
			host = self.host,
			port = self.port,
			user = self.user,
			password = self.password,
			db = self.db,
			charset = self.charset
			)
		# self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
		self.cursor = slef.connection.cursor()


	def select(self,sql_sentencce):
		self.cursor.execute(sql_sentencce)
		result = self.cursor.fetchall()
		return result


	def select_info_by_student_id(self,id):
		self.execute(select_student_info_by_id,[str(id)])
		result = self.cursor.fetchall()
		return result

	def select_info_by_student_name(self,name):
		self.execute(select_student_info_by_student_name,[str(name)])
		result = self.cursor.fetchall()
		return result

	def close(self):
		self.connection.commit()
		self.cursor.close()
		self.connection.close()


