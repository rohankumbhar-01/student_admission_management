// Copyright (c) 2023, Rohan_k and contributors
// For license information, please see license.txt

frappe.ui.form.on('Report Analisis', {
	refresh: function(frm) {
		if (!frm.doc.description) {
			frm.set_intro('This is a report analisis page ', 'red');
		}
		frm.disable_save();
		frm.add_custom_button(__('Count'), function() {
			

			frappe.call({
				method:'count',
				doc:frm.doc,
				callback:function(r){
					frm.refresh_fields('total_science_students')
					frm.refresh()
				}
				
				
			})
			if (frm.is_dirty()) {
				frappe.show_alert('Analisis is done by Count Button !')
			}
			
			
		})
	}	
	
});
