# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
	def before_save(self):
		self.full_name = f'{self.first_name or ""} {self.middle_name or ""} {self.last_name or ""}'
	# frappe.db.set_value("Student","admission_status", "Available")
	# frappe.db.set_value('Student', student_name, 'admission_status', 'Available')


