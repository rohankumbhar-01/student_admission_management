# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class College(Document):
	pass

# @frappe.whitelist()
# def before_save(self):

		
# 	parent_doc = frappe.get_doc('Student enrollment form')
# 	child_table_records = parent_doc.get('student_details')

	
# 	for i in child_table_records:
# 		print(i)

# 		for college in self.eligibility_criteria:

# 			if (i.choice_of_course == "Science" and college.course == "Science" and i.hsc_percentage >= college.percentage):
# 				print(i.full_name, i.choice_of_course, i.ssc_percentage, college.course)
				
# 				self.append('science_students', {
# 					'full_name': i.full_name
# 				})	

# 			if (i.choice_of_course == "Commerce" and college.course == "Commerce" and i.hsc_percentage >= college.percentage):
				
# 				self.append('commerce_students', {
# 					'full_name': i.full_name
# 				})	

# 			if (i.choice_of_course == "Arts" and college.course == "Arts" and i.hsc_percentage >= college.percentage):
				
# 				self.append('arts_students', {
# 					'full_name': i.full_name
# 				})
# @frappe.whitelist()
# def frappe_call():
# 	return'hi'



