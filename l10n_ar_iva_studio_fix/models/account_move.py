from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    # Nos aseguramos de re-declarar el campo para añadirle
    # la lógica 'compute' y 'store=True'.
    x_studio_vat_date = fields.Date(
        string='Fecha Imputación IVA', # Studio ya le puso este nombre
        compute='_compute_x_studio_vat_date',
        store=True,
        readonly=False, # ¡Clave! Permite edición manual
        copy=False,
        index=True)

    @api.depends('date')
    def _compute_x_studio_vat_date(self):
        """
        Asigna la fecha contable por defecto.
        Si un usuario la cambia manualmente, el 'store=True' y 'readonly=False'
        respetarán ese valor manual.
        """
        for move in self:
            # Solo asigna el default si no hay un valor manual ya seteado
            # o si la fecha contable cambia.
            if not move.x_studio_vat_date or move.date != move.x_studio_vat_date:
                 move.x_studio_vat_date = move.date