# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import time

class Studentregistrationform(Document):
	def before_save(self):
		self.full_name = f'{self.first_name or ""} {self.middle_name or ""} {self.last_name or ""}'
	def on_submit(self):
		student = frappe.new_doc('Student')
		student.first_name = self.first_name
		student.middle_name = self.middle_name
		student.last_name = self.last_name
		student.full_name = self.full_name
		student.sex = self.sex
		student.blood_group = self.blood_group
		student.mobile_no = self.mobile_no
		student.e_mail = self.e_mail
		student.address = self.address
		student.nactionality = self.nactionality
		student.choice_of_course = self.choice_of_course 
		student.ssc_percentage = self.ssc_percentage
		student.hsc_percentage = self.hsc_percentage
		student.admission_status = "Available"
		student.insert()
		frappe.msgprint("The Record Created Successfully in Student Doctype")
		# frappe.db.set_value('Student','admission_status', 'Available')
	
		# time.sleep(3)
		# frappe.publish_realtime("clear_messages")
		
	


