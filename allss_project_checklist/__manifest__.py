# -*- coding: utf-8 -*-
{
    'name': 'ALLSS - Checklists',
    'version': '14.0.1.0.0',
    'licence': 'AGPL-3',
    'category': 'Project',
    'author': 'Renata Carrillo (ALLSS Soluções em Sistemas),',
    'summary': 'ALLSS - Checklists',
    'description':'Campos Específicos Checklists - PKI',
    'depends': [
        'project',
        'base',
        'sale_management',
        'sale_project',
        'account',
    ],
    'data': [
        #report
        'reports/report.xml',

        #views
        'views/project_custom_view.xml',

        #security
        # 'security/ir.model.access.csv',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}