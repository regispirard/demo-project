# Copyright 2023 TINCID SRL (Régis Pirard)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class DemoEmployee(models.Model):

    _name = "demo.employee"
    _description = "DEMO Employee"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _mail_post_access = "read"


    employee_name = fields.Char(
        string="Employee Full Name",
    )
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        readonly=True,
    )