from odoo import models, fields, api

class Reserva(models.Model):
    _name = 'flota_vehiculos.reserva'
    _description = 'Reserva de vehículo'

    coche_id = fields.Many2one(
        'flota_vehiculos.coche', 
        string='Coche', 
        domain="[('disponible', '=', True)]",
        required=True
    )
    conductor_id = fields.Many2one(
        'hr.employee', 
        string='Conductor',
        required=True
    )
    fecha_inicio = fields.Date(string='Fecha inicio', required=True)
    fecha_fin = fields.Date(string='Fecha fin')
    zona = fields.Selection(
        selection=[
            ('euskadi', 'Euskadi'),
            ('araba', 'Araba'),
            ('bizkaia', 'Bizkaia'),
            ('gipuzkoa', 'Gipuzkoa'),
        ],
        string='Zona',
        required=True
    )
    entregado = fields.Boolean(string='Entregado')

    @api.onchange('coche_id')
    def _onchange_coche_id(self):
        if self.coche_id:
            self.coche_id.disponible = False