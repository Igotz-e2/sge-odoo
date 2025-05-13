from odoo import models, fields, api

class PerritosCalientes(models.Model):
    _name = 'perritos_calientes.perritos_calientes'
    _description = 'Modelo para Perritos Calientes'

    name = fields.Char("Nombre")
    value = fields.Integer("Valor")
    value2 = fields.Float(compute="_value_pc", store=True, string="Valor %")
    description = fields.Text("Descripción")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
