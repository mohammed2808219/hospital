{
    'name' : 'PK21',
    'version' : '1.1',
    'summary': 'PK21 application software system',
    'sequence': 1,
    'description': """PK21 application for odoo""",
    'category': 'PK21',
    'website': 'https://www.odoohospi.tech',
    'depends' : ['base',
                 'menu'],
    'data': [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "data/conf_data_pk21.xml",
        "views/pk21_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'application': True,
}
