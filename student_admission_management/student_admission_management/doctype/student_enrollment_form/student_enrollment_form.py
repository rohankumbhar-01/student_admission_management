# Copyright (c) 2023, Rohan_k and contributors
# For license information, please see license.txt

import frappe
# import pyttsx3
from frappe.model.document import Document

# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

class Studentenrollmentform(Document):
    
    @frappe.whitelist()
    def frm_call(self):
       
       doc = frappe.get_all('Student',{
           'admission_status': 'Available','college':self.college}, 
		       [
           'full_name','e_mail','choice_of_course','hsc_percentage','ssc_percentage'])
       
       self.student_details=[]
       
       print("##############################",doc)
       for student in doc:
            self.append('student_details',{
				'full_name':student.full_name,
				'e_mail':student.e_mail,
				'choice_of_course':student.choice_of_course,
				'hsc_percentage':student.hsc_percentage,
				'ssc_percentage':student.ssc_percentage
			})
	    
    @frappe.whitelist()
    def student_enroll(self):
                    
            if not self.student_details:
                        frappe.throw(
                            'This file does not exist',
                        )
            elif self.student_details:
                clg_doc = frappe.get_doc('College',{"name":self.college})
                
                
                # clg_doc.science_students=[]
                # clg_doc.commerce_students=[]
                # clg_doc.arts_students=[]


                #for storing subject required percentage in variables 
                
                for i in clg_doc.eligibility_criteria:
                    if i.course == "Science":
                        sci_cri_percnt = i.percentage #variable
                    if i.course == "Commerce":
                        comm_cri_percent =i.percentage  #Variable
                    if i.course == "Arts":
                        arts_cri_percent = i.percentage


                for a in self.student_details:


                    if (a.choice_of_course == "Science" and int(a.hsc_percentage) >= int(sci_cri_percnt)):
                        clg_doc.append('science_students', {
                            'full_name': a.full_name
                        })	

                        #For Changing Fetched Avoilable Student status into  Enroll .
                        for student in clg_doc.science_students:
                            print("-------------------------------------",student)
                            frappe.db.sql('''
                            UPDATE `tabStudent`
                            SET admission_status='Enrolled'
                            WHERE
                            full_name ='{0}'
                            '''.format(student.full_name))

                    elif (a.choice_of_course == "Commerce" and  int(a.hsc_percentage) >= int(comm_cri_percent)):
                        clg_doc.append('commerce_students', {
                            'full_name': a.full_name
                        })

                        
                        for student in clg_doc.commerce_students:
                            print("-------------------------------------",student)
                            frappe.db.sql('''
                            UPDATE `tabStudent`
                            SET admission_status='Enrolled'
                            WHERE
                            full_name ='{0}'
                            '''.format(student.full_name))               

                        
                
            

                    elif (a.choice_of_course == "Arts" and  int(a.hsc_percentage) >= int(arts_cri_percent)):
                        clg_doc.append('arts_students', {
                            'full_name': a.full_name
                        })
                        for student in clg_doc.arts_students:
                            print("-------------------------------------",student)
                            frappe.db.sql('''
                            UPDATE `tabStudent`
                            SET admission_status='Enrolled'
                            WHERE
                            full_name ='{0}'
                            '''.format(student.full_name)) 
                    #Changing status into Rejected
                    else:
                        frappe.db.sql('''
                        UPDATE `tabStudent`
                        SET admission_status='Rejected'
                        WHERE
                        full_name ='{0}'
                        '''.format(a.full_name))      
                        # frappe.msgprint("Student rejected")
                clg_doc.save()          

        

        #For Changing Fetched Avoilable Student status into  Enroll .
        # for student in clg_doc.science_students:
        #     # print("-------------------------------------",u)
        #     frappe.db.sql('''
        #     UPDATE `tabStudent`
        #     SET admission_status='Enrolled'
        #     WHERE
        #     full_name ='{0}'
        #     '''.format(student.full_name))


        # for student in clg_doc.commerce_students:
        #     # print("-------------------------------------",update)
        #     frappe.db.sql('''
        #     UPDATE `tabStudent`
        #     SET admission_status='Enrolled'
        #     WHERE
        #     full_name ='{0}'
        #     '''.format(student.full_name))

        # for student in clg_doc.arts_students:
        #     # print("-------------------------------------",update)
        #     frappe.db.sql('''
        #     UPDATE `tabStudent`
        #     SET admission_status='Enrolled'
        #     WHERE
        #     full_name ='{0}'
        #     '''.format(student.full_name)) 

        
            
    
        # clg_doc.save()
        # frappe.db.commit()
        # return True
    
        

    # @frappe.whitelist()
    # def status_change(self):
    #     update = frappe.get_doc("College",{"name":self.college})
    #     print("----------------------------------------",update)
    #     # college = frappe.get_doc("COllege",{self.College})
    #     for student in update.science_students:
    #         print("-------------------------------------",update)
    #         frappe.db.sql('''
    #         UPDATE `tabStudent`
    #         SET admission_status='Enrolled'
    #         WHERE
    #         full_name ='{0}'
    #         '''.format(student.full_name))

    #     for student in update.commerce_students:
    #         print("-------------------------------------",update)
    #         frappe.db.sql('''
    #         UPDATE `tabStudent`
    #         SET admission_status='Enrolled'
    #         WHERE
    #         full_name ='{0}'
    #         '''.format(student.full_name))

    #     for student in update.arts_students:
    #         print("-------------------------------------",update)
    #         frappe.db.sql('''
    #         UPDATE `tabStudent`
    #         SET admission_status='Enrolled'
    #         WHERE
    #         full_name ='{0}'
    #         '''.format(student.full_name))
    #         # clg_doc.save()
            




			
    
    
    # @frappe.whitelist()
    # def fetch_students(self):
    #     self.disable_save()
    #     college = self.college
    #     students = []
    #     for student in frappe.get_all("Student", {"admission_status": "Available"}):
    #         if frappe.db.get_value("Eligibility Criteria", {"parent": college, "course": student.choice_of_course},
    #                                 "percentage") <= student.hsc_percentage:
    #             students.append(student)
        
    #     self.student_details = []
    #     for student in students:
    #         self.append("student_details", {
    #             "full_name": student.full_name,
    #             "e_mail": student.e_mail,
    #             "choice_of_course": student.choice_of_course,
    #             "hsc_percentage": student.hsc_percentage,
    #             "ssc_percentage": student.ssc_percentage
    #         })

    # def validate(self):
    #     if not self.student_details:
    #         frappe.throw("Please fetch students first.")
    
    # def on_submit(self):
    #     for student in self.student_details:
    #         # Your code to enroll student goes here
    #         pass

# class Studentenrollmentform(Document):
    
#     @frappe.whitelist()
#     def frm_call(self):
       

#        doc = frappe.get_all('Student',{
#            'admission_status': 'Available'}, 
# 		       [
#            'full_name','e_mail','choice_of_course','hsc_percentage','ssc_percentage'])

#        self.student_details=[]
       
#        for student in doc:
#             self.append('student_details',{
# 				'full_name':student.full_name,
# 				'e_mail':student.e_mail,
# 				'choice_of_course':student.choice_of_course,
# 				'hsc_percentage':student.hsc_percentage,
# 				'ssc_percentage':student.ssc_percentage
# 			})
			

	# @frappe.whitelist()
        
	# def get_students():
	# 	# Fetch all the students and their details
	# 	students = frappe.db.get_all('Student', fields=['name', 'full_name', 'email', 'choice_of_course', 'hsc_percentage', 'ssc_percentage'])

	# 	# Return the list of students to the client-side
	# 	return students
