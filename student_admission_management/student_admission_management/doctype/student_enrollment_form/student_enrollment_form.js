// Copyright (c) 2023, Rohan_k and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student enrollment form', {
    
	refresh:function(frm) {
       

        frm.disable_save();
        frm.clear_table('student_details')
        frm.refresh_fields("student_details")


		frm.add_custom_button(__('Fetch Students'), function() {
            // Your code to fetch students goes here
            frm.trigger('validate');
            frappe.call ({
                method: 'frm_call',
                doc:frm.doc,
                callback: function(r){
                    
                    console.log(r)
                    frm.refresh_fields("student_details")
                }
            })
            // frappe.msgprint("Student Fetched successful")
        });
        frm.add_custom_button(__('Enroll now'), function() {
            const newLocal = "Student enrolled successfully";
            frappe.call({

                method:'student_enroll',
                doc:frm.doc,
                callback: function(r){
                    console.log(r.message)
                    // frm.refresh_fields("")

                }
               
            })
           
            // Your code to fetch students goes here
            frappe.msgprint(newLocal)    
        })
    }	
});



// frappe.ui.form.on("Student enrollment form",{
//     validate:function(frm){
//         // frm.add_custom_button(__('Conform Admission'),function(){
//             frappe.call({
//                 method:"status_change",
//                 doc:frm.doc,
//                 callback:function(r){
//                     console.log(r.message)
//                 }
//             })
//             frappe.msgprint("Student Admission status changes successfully")
//         // })
//     }
// })
