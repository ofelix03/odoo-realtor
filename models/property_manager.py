from odoo import fields, models


class PropertyManager(models.Model):
    _name = "realtor.property.manager"
    _description = "Real Estate Property Manager"

    name = fields.Char(required=True)
    mobile = fields.Char(required=True)
    email = fields.Char(required=True)
