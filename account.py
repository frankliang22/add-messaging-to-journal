from openerp.osv import fields, orm , osv
from openerp.tools.translate import _

class account_move(osv.osv):
	_name = "account.move"
	_inherit = ['mail.thread','ir.needaction_mixin','account.move']
	#_inherit = "account.move"