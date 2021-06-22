##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import fields, models, _


class MessageWizard(models.TransientModel):
    _name = "message.wizard"
    _description = "Message wizard to display warnings, alerts and success messages."

    def get_default(self):
        if self.env.context.get("message", False):
            return self.env.context.get("message")
        return False

    name = fields.Text(
        string="Message",
        readonly=True,
        default=get_default
    )
