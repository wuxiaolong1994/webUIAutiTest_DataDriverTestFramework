# -*- coding:utf-8 -*-
# Date:2019/7/24
# Author:wuxiaolong

select_student_info_by_id = "select * from xx where id=%s"

select_student_info_by_student_name = "select * from xx where name=%s"

select_student_info_by_TeacherName = "select student_id,student_name \
from students \
where teacher_id in (select teacher_id from teachers where tearcher_name=%s)"

select_scoreInfo_by_class_id = "select max(score),min(score),avg(score) \
from score_table \
where class_id=%s"