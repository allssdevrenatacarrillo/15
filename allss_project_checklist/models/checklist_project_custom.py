from odoo import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class ProjectProjectCustom(models.Model):
    _inherit = 'project.project'

    model_a_id = fields.Many2one('account.move', string='Model A')
    # allss_status_pagamento = fields.Selection(related='model_a_id.payment_state', string="Status Pagamento Auditoria", store=True)
    allss_status_pagamento = fields.Selection(related='sale_line_id.order_id.invoice_ids.payment_state', string="Status Pagamento Auditoria", store=True)
    # allss_status_pagamento = fields.Selection(related='model_a_id', string="Status Pagamento Auditoria", store=True)

    @api.model
    def account_search(self, sale_line_id):
        model_a_id = self.search(sale_line_id.order_id.invoice_ids.id)
        return model_a_id
