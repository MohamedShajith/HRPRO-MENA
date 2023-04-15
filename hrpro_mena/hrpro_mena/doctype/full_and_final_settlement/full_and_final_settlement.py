# Copyright (c) 2023, TEAMPRO and contributors
# For license information, please see license.txt

import frappe
import datetime
import calendar

from frappe.model.document import Document

class FullandFinalSettlement(Document):
	@frappe.whitelist()
	def get_current_month_date(self):
		ff = frappe.get_value('Resignation Form', {'employee': self.employee}, ['actual_relieving_date'])
		now = ff
		days = calendar.monthrange(now.year, now.month)[1]
		frappe.errprint(days)
		return(days)

	@frappe.whitelist()
	def calculate_attendance(self):
		name,hod_rel,actual_rel = frappe.db.get_value("Resignation Form",{'name':self.employee},["name","hods_relieving_date","actual_relieving_date"])
		current_date = actual_rel
		first_day_of_month = current_date.replace(day=1)
		hod_date = str(first_day_of_month)
		app_date = str(actual_rel)
		if name:
			att = frappe.db.count("Attendance",{'name':self.employee,'status':"Present",'attendance_date':('between',(hod_date,app_date))},["name","hods_relieving_date","actual_relieving_date"])

			
			cal = att
			return cal, name
		

	@frappe.whitelist()
	def get_reg_form(self):
		name,hod_rel,actual_rel = frappe.db.get_value("Resignation Form",{'name':self.employee},["name","hods_relieving_date","actual_relieving_date"])
		current_date = actual_rel
		first_day_of_month = current_date.replace(day=1)
		return name, first_day_of_month,actual_rel