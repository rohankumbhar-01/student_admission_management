// Copyright (c) 2023, Rohan_k and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {
		if (!frm.doc.description) {
			var nam = frm.doc.name;
			frm.set_intro(`This is ${nam}'s description`,'red');
		}
	}
	// refresh: function(frm) {

	// }
});
