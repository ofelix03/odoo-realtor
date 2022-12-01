from odoo import fields, models


class Property(models.Model):
    _name = "realtor.property"
    _description = "Real Estate Property"

    name = fields.Char(required=True)
    manager_id = fields.Many2one(
        comodel_name="realtor.property.manager", string="Manager", required=True
    )
    amenity_ids = fields.One2many(
        comodel_name="realtor.property.amenity",
        inverse_name="property_id",
        required=True,
    )
    location = fields.Char(required=True)
    cover_image = fields.Binary(attachment=True)

    def action_interested(self):
        template = self.env.ref("realtor.interested_property_template")
        template.send_mail(self.id)
