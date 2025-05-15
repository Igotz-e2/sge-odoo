from odoo import models, fields, api

class Coche(models.Model):
    _name = 'flota_vehiculos.coche'
    _description = 'Vehículo de la empresa'
    
    # Campo name requerido por Odoo
    name = fields.Char(string="Nombre", compute="_compute_name", store=True)
    
    codigo = fields.Char(string='Código', required=True)
    marca = fields.Selection(
        selection=[
            ('seat', 'Seat'),
            ('bmw', 'BMW'),
            ('audi', 'Audi'),
            ('mercedes', 'Mercedes'),
        ],
        string='Marca',
        required=True
    )
    modelo = fields.Char(string='Modelo', required=True)
    matricula = fields.Char(string='Matrícula')
    disponible = fields.Boolean(string='Disponible', default=True)

    @api.depends('codigo', 'modelo')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.codigo} - {record.modelo}"

    def toggle_disponible(self):
        for record in self:
            record.disponible = not record.disponible