# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Estudiantes MFH',
    'version': '1.0',
    'author': 'Marlon Falcon Hernandez',
    'category': 'Tools',
    'summary': 'Ejemplo de un módulo de Odoo',
    'website': 'https://www.marlonfalcon.cl',
    'description': """
Ejemplo de listado de estudiantes
======================
Con este módulo mostraremos como hacer tu primer componente en odoo 9
    """,
    'depends': ['base_setup'],
    'data': [
        'views/estudiantes_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}