from odoo import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class ProjectProjectCustom(models.Model):
    _inherit = 'project.project'

    model_a_id = fields.Many2one('account.move', related='sale_line_id.order_id.invoice_ids.invoice_ids.id', string='Model A')
    # allss_status_pagamento = fields.Selection(related='model_a_id.payment_state', string="Status Pagamento Auditoria", store=True)
    # allss_status_pagamento = fields.Selection(related='sale_line_id.order_id.invoice_ids.payment_state', string="Status Pagamento Auditoria", store=True)
    allss_status_pagamento = fields.Char(related='model_a_id.payment_state', string="Status Pagamento Auditoria", store=True)
    # allss_status_pagamento_dois = fields.Char(related='sale_line_id.order_id.invoice_ids.invoice_id.payment_state', string="Status Pagamento Auditoria", store=True)
    # cond_pedido_field = fields.Char(string='Nome', compute="_get_pedido", readonly=True)