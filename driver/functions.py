# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

import logging
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
from driver.read_config import*


# 获取当前系统时间
def get_time():
	crnt_time = time.strftime("%Y%m%d_%H%M%S",time.localtime())
	# print(crnt_time)
	return crnt_time


# 截图
def get_screenshot(driver,description):
	crnt_time = get_time()
	screenshot_dir = os.path.join(__file__.split("driver")[0],r"test_result\screenshots")
	# print(screenshot_dir)
	screenshot_path = os.path.join(screenshot_dir,description+".png")
	# print(screenshot_path)
	driver.get_screenshot_as_file(screenshot_path)

# 获取最新的测试报告
def get_latest_report():
	report_dir = os.path.join(__file__.split("driver")[0],r"test_result\test_report")
	# print(report_dir)
	report_list = os.listdir(report_dir)
	report_list.sort(key=lambda report_file:os.path.getatime(os.path.join(report_dir,report_file)))
	# print(report_list)
	return os.path.join(report_dir,report_list[-1])

# 通过邮件发送测试报告
def send_report(now):
	latest_report = get_latest_report()
	filename = "AutoTestReport_" + now + "_.html"
	mail_config = get_config("mail")
	# print(mail_config)
	with open(latest_report,"rb") as file:
		mail_content = file.read()

	smtpserver = mail_config["server"]
	user = mail_config["user"]
	password = mail_config["password"]


	sender = mail_config["sender"]
	receivers = mail_config["receivers"]
	subject = "极客数学帮web自动化测试_测试报告_%s"%get_time()

	try:
		# 邮件正文
		msg = MIMEMultipart()
		msg["Subject"] = Header(subject,"utf-8")
		msg["From"] = sender
		msg["To"] = ",".join(receivers)

		text_msg = MIMEText(mail_content,"html","utf-8")

		html_attachment = MIMEApplication(mail_content)
		html_attachment.add_header('Content-Disposition', 'attachment', filename=filename)

		msg.attach(text_msg)
		msg.attach(html_attachment)


		# SSL协议常用端口号：465
		smtp = smtplib.SMTP_SSL(smtpserver,465)

		# helo向服务器标识用户身份
		smtp.helo(smtpserver)

		# 服务器返回结果确认
		smtp.ehlo(smtpserver)

		smtp.login(user,password)

		print("开始发送测试报告...")
		smtp.sendmail(sender,receivers,msg.as_string())
		print("测试报告发送完成！")
	except Exception as e:
		print(e)

def logging_init(loglevel):
	log_file_path = os.path.join(__file__.split("driver")[0],r"log\0.log")
	log_format = "[ %(asctime)s ] - %(name)s -%(levelname)s : %(message)s "
	logging.basicConfig(
		format = log_format,
		level = loglevel,
		filename = log_file_path,
		filemode = "a"
		)

if __name__ == "__main__":
	# get_time()
	# get_screenshot("sd")
	# print(get_latest_report())
	# send_report()
	# logging_init(logging.DEBUG)
	# logging.debug("debug log")
	# logging.error("error log")
	pass
