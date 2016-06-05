# -*- coding: utf-8 -*-
##############################################################################
#
#    account_bank_statement_import_fr_cfonb module for Odoo
#    Copyright (C) 2014-2015 Akretion (http://www.akretion.com)
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#    @author Florent de Labarre <florent@iguanayachts.com>
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Import French CFONB Multi Bank Statements',
    'version': '9.0.2.0.0',
    'license': 'AGPL-3',
    'author': "Akretion,Odoo Community Association (OCA), Florent de Labarre",
    'website': 'http://www.akretion.com',
    'summary': 'Import French CFONB multi bank files as Bank Statements in Odoo',
    'depends': ['account_bank_statement_import', 'base'],
    'data': ['account_bank_statement_import_fr_multi_cfonb.xml'],
    'installable': True,
}
