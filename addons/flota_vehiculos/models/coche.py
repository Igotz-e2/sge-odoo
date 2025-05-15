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

    @api.model
    def init(self):
        if not self.env['flota_vehiculos.coche'].search_count([]):
            coches = [
                {'codigo': 'A001', 'marca': 'seat', 'modelo': 'Ibiza', 'matricula': '1234ABC', 'disponible': True},
                {'codigo': 'B002', 'marca': 'bmw', 'modelo': 'Serie 3', 'matricula': '5678DEF', 'disponible': True},
                {'codigo': 'C003', 'marca': 'audi', 'modelo': 'A4', 'matricula': '9012GHI', 'disponible': False}
            ]
            for coche in coches:
                self.env['flota_vehiculos.coche'].create(coche)