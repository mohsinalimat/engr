# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "engr"
app_title = "Engineering"
app_publisher = "Finbyz Tech. Pvt. Ltd."
app_description = "Engineering"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@finbyz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/engr/css/engr.css"
# app_include_js = "/assets/engr/js/engr.js"

app_include_js = [
	"/assets/js/engineering.min.js" 
]


doctype_list_js = {
	"Sales Order" : "public/js/doctype_js/sales_order_list.js"
}

doctype_js = {
	"Sales Order": "public/js/doctype_js/sales_order.js",
	"Purchase Order": "public/js/doctype_js/purchase_order.js",
	"Delivery Note": "public/js/doctype_js/delivery_note.js",
	"Customer":"public/js/doctype_js/customer.js",
	"Sales Invoice":"public/js/doctype_js/sales_invoice.js",
	"Communication":"public/js/doctype_js/communication.js",
}

override_doctype_dashboards = {
	"Sales Order": "engr.engineering.dashboard.sales_order.get_data",
	"Customer": "engr.engineering.dashboard.customer.get_data",
}

doc_events = {
	"Customer":{
		"validate":"engr.engineering.doc_events.customer.validate_customer_potential"
	},
	"Item":{
		"validate": "engr.engineering.doc_events.item.validate",
		"on_update": "engr.engineering.doc_events.item.on_update",
	},
	"Payment Entry":{
		"validate":"engr.engineering.doc_events.payment_entry.validate",
		"on_submit":"engr.engineering.doc_events.payment_entry.on_submit",
		"on_cancel":"engr.engineering.doc_events.payment_entry.on_cancel"
	},
	"Sales Invoice":{
		"validate":"engr.engineering.doc_events.sales_invoice.validate",
		"on_submit":"engr.engineering.doc_events.sales_invoice.on_submit",
		"before_cancel":"engr.engineering.doc_events.sales_invoice.before_cancel",
		"on_cancel":"engr.engineering.doc_events.sales_invoice.on_cancel",
		"on_trash":"engr.engineering.doc_events.sales_invoice.on_trash",
	},
	"Purchase Order":{
		"validate":"engr.engineering.doc_events.purchase_order.validate",
		"on_update_after_submit":"engr.engineering.doc_events.purchase_order.update_reqd_date",
		"on_submit":"engr.engineering.doc_events.purchase_order.on_submit",
		"on_cancel":"engr.engineering.doc_events.purchase_order.on_cancel",
		"on_trash":"engr.engineering.doc_events.purchase_order.on_trash",

	},
	"Sales Order":{
		"validate":"engr.engineering.doc_events.sales_order.validate",
	},
	"Delivery Note":{
		"validate":"engr.engineering.doc_events.delivery_note.validate",
		"on_submit":"engr.engineering.doc_events.delivery_note.on_submit",
		"on_cancel":"engr.engineering.doc_events.delivery_note.on_cancel",
		"on_trash":"engr.engineering.doc_events.delivery_note.on_trash",
	},
	"Salary Slip":{
		"validate":"engr.engineering.doc_events.salary_slip.validate"
	},
	"Opportunity":{
		"validate":"engr.engineering.doc_events.opportunity.validate"
	}
}
# include js, css files in header of web template
# web_include_css = "/assets/engr/css/engr.css"
# web_include_js = "/assets/engr/js/engr.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "engr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "engr.install.before_install"
# after_install = "engr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "engr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron":{
		"0 4 * * SUN": [
			"engr.api.sales_invoice_payment_remainder",
		],
	}
}
# scheduler_events = {
# 	"all": [
# 		"engr.tasks.all"
# 	],
# 	"daily": [
# 		"engr.tasks.daily"
# 	],
# 	"hourly": [
# 		"engr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"engr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"engr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "engr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "engr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "engr.task.get_dashboard_data"
# }

# Sales Partner target report changes for all fetch all item groups instead of one item group
from erpnext.selling.report.sales_partner_target_variance_based_on_item_group import item_group_wise_sales_target_variance
from engr.engineering.report.item_group_wise_sales_target_variance import get_data_column
item_group_wise_sales_target_variance.get_data_column = get_data_column


# Override for chart
from erpnext.selling.report.sales_person_target_variance_based_on_item_group import sales_person_target_variance_based_on_item_group
from engr.engineering.report.sales_person_target_variance_based_on_item_group import execute
sales_person_target_variance_based_on_item_group.execute = execute
