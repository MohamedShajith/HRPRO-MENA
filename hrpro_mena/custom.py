from __future__ import unicode_literals
import frappe
import erpnext
from frappe.utils import cint
import json
from frappe.utils import date_diff, add_months, today, add_days, add_years, nowdate, flt
from frappe.model.mapper import get_mapped_doc
from frappe.utils.file_manager import get_file
from frappe.utils.csvutils import UnicodeWriter, read_csv_content
import datetime
from datetime import datetime, timedelta, date
from frappe.utils import now_datetime, nowdate
from dateutil import relativedelta
import datetime
import calendar

@frappe.whitelist()
def get_leave_application(employee):
    leave_application = frappe.get_all('Leave Application', {'employee': employee, 'docstatus': 1}, ['*'])
    if leave_application:
        for lap in leave_application:
            from_date = lap.from_date
            first_of_month = from_date.replace(day=1)
            to_date = lap.from_date
            before_day = to_date - timedelta(days=1)
            attendance = frappe.db.sql("""select count(*) as count, sum(ot_hours) as ot ,sum(week_end_ot) as wot,sum(holiday_ot) as hot from `tabAttendance` where docstatus != 2 and employee = '%s' and  attendance_date between '%s' and '%s' """ % (employee, first_of_month, before_day), as_dict=1)[0]
            abs1 = frappe.db.sql("""select count(*) as count from `tabAttendance` where docstatus != 2 and employee = '%s' and  attendance_date between '%s' and '%s' and status = 'Absent' """ % (employee, first_of_month, before_day), as_dict=1)[0]
            abs2 = frappe.db.sql("""select count(*) as count from `tabAttendance` where docstatus != 2 and employee = '%s' and  attendance_date between '%s' and '%s' and status = 'On Leave' and leave_type = 'Leave Without Pay' """ % (employee, first_of_month, before_day), as_dict=1)[0]
            return first_of_month, before_day,lap.from_date, lap.custom_to_date,attendance.count, attendance.ot or 0, attendance.wot or 0, attendance.hot or 0, lap.lop_days, lap.total_leave_days, lap.leave_balance, lap.leave_type, abs1.count, abs2.count


@frappe.whitelist()
def prob_eval(employee_name):
	prob = frappe.db.exists("Staff Probation Evaluation Form",employee_name)
	if prob:
		return True
	else:
		return False
