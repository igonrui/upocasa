# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class visita(osv.Model):

    _name = 'visita'
    _description = 'Visitas de un cliente a un inmueble'
 
    _columns = {
        'name': fields.integer('Id', size=9, required=True),
        'visit_start': fields.datetime('Inicio', size=60, required=True),
        'visit_end':fields.datetime('Fin',size=60,required=True),
        
        'cliente_dni':fields.many2one('cliente', 'Cliente', required=True),
        'inmueble_id':fields.many2one('inmueble','Inmueble', required=True),
        'agente_dni_visita':fields.many2one('agente','Agente', required=True),
    }
    
    _sql_constraints=[('name_uniq','unique (name)','El identificador de la visita ya existe.')]