# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

import openpyxl

class ReadTestData():
	def __init__(self,path,title):
		self.path = path
		self.title = title
		self.wb = openpyxl.load_workbook(self.path)
		self.ws = self.wb[title]

	def get_data(self):
		rows = self.ws.rows
		data = []
		for row in rows:
			temp = []
			for cell in row:
				temp.append(cell.value)
			data.append(temp[1:])
		return data[1:]

if __name__ == "__main__":
	sheet = ReadTestData(r"C:\Users\VULCAN\Desktop\简历\极客数学帮\web自动化\test_data\test_data.xlsx","top_menus")
	data = sheet.get_data()
	for line in data:
		print(line)