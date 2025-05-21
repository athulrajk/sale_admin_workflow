from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    manager_reference = fields.Char(string="Manager Reference")
    auto_workflow = fields.Boolean(string="Auto Workflow")

    def action_confirm(self):
        limit = float(self.env['ir.config_parameter'].sudo().get_param('sale_admin_workflow.sale_order_limit') or 0)
        for order in self:
            if order.amount_total > limit and not self.env.user.has_group('sale_admin_workflow.group_sale_admin'):
                raise UserError("Only Sale Admin can confirm orders exceeding the sale order limit.")
        
        res = super().action_confirm()

        for order in self:
            if order.auto_workflow:
                # Auto confirm pickings
                for picking in order.picking_ids:
                    picking.action_confirm()
                    picking.action_assign()
                    for move in picking.move_ids_without_package:
                        move.quantity_done = move.product_uom_qty
                    picking.button_validate()

                # Create and post invoice
                invoice
