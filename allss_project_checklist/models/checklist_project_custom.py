from odoo import models, fields, api
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class ProjectProjectCustom(models.Model):
    _inherit = 'project.project'

    # model_a_id = fields.Many2one('account.move', string='Model A')
    # allss_status_pagamento = fields.Selection(related='model_a_id.payment_state', string="Status Pagamento Auditoria", store=True)
    # allss_status_pagamento = fields.Selection(related='sale_line_id.order_id.invoice_ids.payment_state', string="Status Pagamento Auditoria", store=True)
    # cond_pedido_field = fields.Char(string='Nome', compute="_get_pedido", readonly=True)

    # def _get_pedido(self):
    #     # cond_pedido = {self.sale_line_id.order_id.invoice_ids}
    #     cond_pedido = 'xpto'
    #     return cond_pedido


    # id_fatura = fields.Char(related="sale_line_id.order_id.invoice_ids.id", string="nome fatura")
    # id_fatura_dois = fields.Many2one('account.move', compute='set_account_move_id', string='nome fatura')
    # nome_fatura = fields.Char(related="sale_line_id.order_id.invoice_ids.id", string="nome fatura")
    # nome_fatura = {sale_line_id.order_id.invoice_ids.id}
    # allss_status_pagamento = fields.Selection(related='id_fatura_dois.payment_state', string="Status Pagamento Auditoria", store=True)
    payment_state = fields.Char(related="sale_line_id.order_id.invoice_ids.payment_state", string="nome fatura")
    allss_status_pagamento = fields.Selection(related='payment_state.payment_state', string="Status Pagamento Auditoria", store=True)

    # def set_account_move_id(self):    
    #     id_account = self.env['account.move'].search([('id','=', self.id_fatura)])
    #     self.id_fatura_dois = id_account
