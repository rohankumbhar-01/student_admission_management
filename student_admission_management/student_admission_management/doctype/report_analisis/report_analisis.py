# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReportAnalisis(Document):
	
	@frappe.whitelist()
	def count(self):
	    
		        
		if not self.college:
			frappe.throw(
					'Please selelect the college before pressing Count Button',
					)
            
		# pass

		elif self.college:
			#Total Commerce Students
			commerce = frappe.db.count('Student', {
				'admission_status':'Enrolled', 'college': self.college, 'choice_of_course': 'Commerce'
				})
			self.total_commerce_students = int(commerce)

            #Total Science Students
			science = frappe.db.count('Student',{
				'admission_status':'Enrolled','college':self.college,'choice_of_course':'Science'
			})
			self.total_science_students = int(science)


			#Total Arts Students
			arts = frappe.db.count('Student',{
				'admission_status':'Enrolled','college':self.college,'choice_of_course':'Arts'
			})
			self.total_arts_students = int(arts)


			#Total Enrolled Students
			enr = frappe.db.count('Student',{
				'admission_status':'Enrolled','college':self.college})
			self.total_enrolled_students = int(enr)


			#Total Rejected Students
			rej = frappe.db.count('Student',{
				'admission_status':'Rejected','college':self.college
			})
			self.total_rejected_students = int(rej)

			#Total Avoilable Students
			available =frappe.db.count('Student',{
				'admission_status':'Available','college':self.college
			})
			self.total_available_students = int(available)


			#Total students
			total = frappe.db.count('Student',{'college':self.college})
			self.total_students = int(total)
		# elif self.total_students:
		# 	frappe.msgprint(" ")
		# else:
		# 	frappe.msgprint(" fields refreshed ")

			





			
