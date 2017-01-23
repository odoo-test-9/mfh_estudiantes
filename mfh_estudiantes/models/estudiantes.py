# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv

class estudiantes(osv.osv):
	# declaramos el nombre empezando con un prefijo
	_name = 'mfh.estudiantes'
	# Por donde se va a buscar
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	   'apellidos' : fields.char('Apellidos', size=80, required=True, help='Aqui pones el apellido'),
	   'cedula' : fields.integer('Cedula', size=10, required=True, help='Aqui pones la cedula'),
	   'fecha_nacimiento' : fields.date('Fecha de nacimiento', help='Fecha de Nacimiento'),
	   'direccion' : fields.text('Direccion', help='Direccion'),
	   'active' : fields.boolean('Activo', help='Campo activo'),
	}
estudiantes()

