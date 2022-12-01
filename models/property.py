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
        body_html = template.body_html.replace("--property-name--", self.name)
        body_html = body_html.replace("--property-manager-name--",
                                       self.manager_id.name)
        body_html = body_html.replace("--customer-name--", self.env.user.name)
        body_html = body_html.replace("--customer-email--", self.env.user.email or "")
        body_html = body_html.replace("--customer-mobile--", self.env.user.mobile or "")

        mail_values = {
            "email_to": self.env.user.email,
            "email_from": self.manager_id.email,
            "subject": "Someone Interested in Property",
            "body_html": body_html,
        }
        self.env["mail.mail"].create(mail_values).send()
