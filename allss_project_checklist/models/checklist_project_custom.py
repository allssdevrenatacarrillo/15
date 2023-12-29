from odoo import models, fields, api
import pytz
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class ProjectProjectCustom(models.Model):
    _inherit = 'project.project'
    # _order = 'allss_last_update desc'

    # model_a_id = fields.Many2one('account.move', string='Model A')
    # allss_status_pagamento = fields.Selection(related='model_a_id.payment_state', string="Status Pagamento Auditoria", store=True)
    allss_status_pagamento = fields.Selection(related='sale_line_id.order_id.invoice_ids.id.payment_state', string="Status Pagamento Auditoria", store=True)
    # allss_status_pagamento = fields.Selection(related='model_a_id', string="Status Pagamento Auditoria", store=True)
