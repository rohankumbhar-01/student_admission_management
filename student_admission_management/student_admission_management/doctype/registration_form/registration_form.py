# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Registrationform(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.middle_name} {self.last_name or ""}'
