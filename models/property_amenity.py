from odoo import fields, models


class PropertyAmenities(models.Model):
    _name = "realtor.property.amenity"
    _description = "Real Estate Property Amenity"

    name = fields.Char(required=True)
    property_id = fields.Many2one(comodel_name="realtor.property", string="Property")
