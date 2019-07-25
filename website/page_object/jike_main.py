# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

# import os,sys
# _path = __file__.split("website")[0]
# sys.path.append(_path)

from website.page_object.BasePage import *
from selenium.webdriver.common.by import By

class MainPage(Page):
	url = "/"

	# 页面元素
	logo_loc = (By.CLASS_NAME,"z-logo")
	menuMain_loc = (By.LINK_TEXT,u"首页")
	menuStudy_loc = (By.LINK_TEXT,u"极客·学") 
	menuTeacher_loc = (By.LINK_TEXT,u"极客·师") 
	menuClass_loc = (By.LINK_TEXT,u"极客·堂") 
	menuPublish_loc = (By.LINK_TEXT,u"极客·致") 
	menuRecruit_loc = (By.LINK_TEXT,u"极客·募") 
	menuDiagnose_loc = (By.LINK_TEXT,u"在线诊断") 
	menuAbout_loc = (By.LINK_TEXT,u"关于我们") 
	livePic1_loc = (By.XPATH,"//div[@class='bd']/ul/li[1]")
	livePic2_loc = (By.XPATH,"//div[@class='bd']/ul/li[2]")
	livePic3_loc = (By.XPATH,"//div[@class='bd']/ul/li[3]")
	floatBox_loc = (By.CLASS_NAME,"nb-icon-inner-wrap")
	closeFloatInfoBox_loc = (By.ID,"nb_nodeboard_close")
	floatBoxMsg_loc = (By.ID,"nb-nodeboard-set-content-js")
	floatBoxName_loc = (By.ID,"nb_nodeboard_set_name")
	floatBoxTel_loc = (By.ID,"nb_nodeboard_set_phone")
	floatBoxAddress_loc = (By.ID,"nb_nodeboard_set_address")
	floatBoxSend_loc = (By.ID,"nb_nodeboard_send")
	QQ_loc = (By.CLASS_NAME,"z-ct1")
	wechat_loc = (By.CLASS_NAME,"z-ct2")
	weibo_loc = (By.CLASS_NAME,"z-ct3")
	grades_loc = (By.XPATH,"//select[@name='gd']/option")
	schools_loc = (By.XPATH,"//select[@name='school']/option")
	studentName_loc = (By.NAME,"name")
	studentTel_loc = (By.NAME,"tel")
	studentMail_loc = (By.NAME,"email")
	orderBtn_loc = (By.ID,"order")
	diagnoseBtn_loc = (By.ID,"zxcs1")
	zxzxBtn_loc = (By.ID,"sy-zxzx")


	def click_logo(self):
		self.find_element(*self.logo_loc).click()

	def click_main_page(self):
		self.find_element(*self.menuMain_loc).click()

	def click_jike_study(self):
		self.find_element(*self.menuStudy_loc).click()

	def click_jike_teacher(self):
		self.find_element(*self.menuTeacher_loc).click()

	def click_jike_class(self):
		self.find_element(*self.menuClass_loc).click()

	def click_jike_publich(self):
		self.find_element(*self.menuPublish_loc).click()

	def click_jike_recruit(self):
		self.find_element(*self.menuRecruit_loc).click()

	def click_jike_diagnose(self):
		self.find_element(*self.menuDiagnose_loc).click()

	def click_about(self):
		self.find_element(*self.menuAbout_loc).click()

	def tap_live_pic(self,num):
		if num == 1:
			self.find_element(*self.livePic1_loc).click()
		elif num == 2:
			self.find_element(*self.livePic2_loc).click()
		elif num == 3:
			self.find_element(*self.livePic3_loc).click()
		else:
			raise Exception("Parameter error,number must between 1 and 3")

	def tap_float_box(self):
		self.find_element(*self.floatBox_loc).click()

	def type_float_message(self,message):
		self.find_element(*self.floatBoxMsg_loc).send_keys(message)

	def type_float_name(self,name):
		self.find_element(*self.floatBoxName_loc).send_keys(name)

	def type_float_tel(self,tel):
		self.find_element(*self.floatBoxTel_loc).send_keys(tel)

	def type_float_address(self,address):
		self.find_element(*self.floatBoxAddress_loc).send_keys(address)

	def tap_float_send(self):
		self.find_element(*self.floatBoxSend_loc).click()

	def chose_grade(self,grade_id):
		grade_option_list = self.find_elements(*self.grades_loc)
		if grade_id == 0:
			grade_option_list[1].click()

		elif grade_id == 1:
			grade_option_list[2].click()

		elif grade_id == 2:
			grade_option_list[3].click()

		elif grade_id == 3:
			grade_option_list[4].click()

		elif grade_id == 4:
			grade_option_list[5].click()

		elif grade_id == 5:
			grade_option_list[6].click()

		elif grade_id == 6:
			grade_option_list[7].click()

		elif grade_id == 7:
			grade_option_list[8].click()

		elif grade_id == 8:
			grade_option_list[9].click()

		elif grade_id == 9:
			grade_option_list[10].click()

		elif grade_id == 10:
			grade_option_list[11].click()

		else:
			raise Exception("请输入正确的年级id")

	def chose_school(self,school_id):
		school_option_list = self.find_elements(*self.schools_loc)
		if school_id == 119:
			school_option_list[1].click()

		elif school_id == 120:
			school_option_list[2].click()

		elif school_id == 127:
			school_option_list[3].click()

		elif school_id == 133:
			school_option_list[4].click()

		elif school_id == 134:
			school_option_list[5].click()

		elif school_id == 135:
			school_option_list[6].click()

		elif school_id == 137:
			school_option_list[7].click()

		elif school_id == 139:
			school_option_list[8].click()

		elif school_id == 140:
			school_option_list[9].click()

		elif school_id == 141:
			school_option_list[10].click()

		elif school_id == 654:
			school_option_list[11].click()

		elif school_id == 660:
			school_option_list[12].click()

		elif school_id == 665:
			school_option_list[13].click()

		elif school_id == 669:
			school_option_list[14].click()

		elif school_id == 674:
			school_option_list[15].click()

		elif school_id == 678:
			school_option_list[16].click()

		elif school_id == 683:
			school_option_list[17].click()

		elif school_id == 687:
			school_option_list[18].click()

		elif school_id == 691:
			school_option_list[19].click()

		elif school_id == 700:
			school_option_list[20].click()

		elif school_id == 704:
			school_option_list[21].click()

		elif school_id == 708:
			school_option_list[22].click()

		elif school_id == 712:
			school_option_list[23].click()

		elif school_id == 716:
			school_option_list[24].click()

		elif school_id == 720:
			school_option_list[25].click()

		else:
			raise Exception("请输入正确的校区id")
		
		
	def type_name(self,name):
		self.find_element(*self.studentName_loc).send_keys(name)

	def type_tel(self,tel):
		self.find_element(*self.studentTel_loc).send_keys(tel)

	def type_mail(self,mail):
		self.find_element(*self.studentMail_loc).send_keys(mail)

	def tap_order_btn(self):
		self.find_element(*self.orderBtn_loc).click()

	def tap_diagnose_btn(self):
		self.find_element(*self.diagnoseBtn_loc).click()


	def order_online(grade_id,school_id,name,tel,mail):
		chose_grade(grade_id)
		chose_school(school_id)
		type_name(name)
		type_tel(tel)
		type_mail(mail)

	def leave_message(message,name,tel,address):
		tap_float_box()
		type_float_message()
		type_float_name()
		type_float_tel()
		type_float_address()
		tap_float_send()
