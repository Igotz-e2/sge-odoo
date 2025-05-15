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

    from odoo.exceptions import ValidationError

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _validar_fechas(self):
        for record in self:
            if record.fecha_fin and record.fecha_inicio > record.fecha_fin:
                 raise ValidationError("La fecha fin no puede ser anterior a la fecha inicio")

    @api.constrains('coche_id')
    def _validar_disponibilidad(self):
        for record in self:
            if not record.coche_id.disponible:
                raise ValidationError("El coche seleccionado no está disponible")

    def _cargar_datos_iniciales(self):
        if not self.env['flota_vehiculos.reserva'].search_count([]):
            empleado = self.env['hr.employee'].search([], limit=1)
            coche = self.env['flota_vehiculos.coche'].search([('disponible','=',True)], limit=1)
        
        if coche and empleado:
            self.create({
                'coche_id': coche.id,
                'conductor_id': empleado.id,
                'fecha_inicio': fields.Date.today(),
                'fecha_fin': fields.Date.add(fields.Date.today(), days=7),
                'zona': 'bizkaia',
                'entregado': False
            })

    def marcar_entregado(self):
        for reserva in self:
            reserva.entregado = True
            reserva.coche_id.disponible = True