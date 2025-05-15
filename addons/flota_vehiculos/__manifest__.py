# -*- coding: utf-8 -*-
{
    'name': 'Flota de Vehículos',
    'summary': 'Gestión de vehículos y reservas para empleados',
    'description': 'Este módulo permite gestionar coches y sus reservas en una empresa.',
    'author': 'Carlos',
    'version': '1.0',
    'depends': ['base', 'hr'],
    'Apps': True,
    'data': [
        'security/ir.model.access.csv',
        'views/coche_views.xml',
        'views/reserva_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}