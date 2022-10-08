{
    'name' : 'Hospital Manegement',
    'version' : '1.1',
    'summary': 'hospital application software system',
    'sequence': 1,
    'description': """hospital application for odoo""",
    'category': 'hospital',
    'website': 'https://www.odoohospi.tech',
    'depends' : [
        'sale',
        'mail'
        ],
    'data': [
        "security/ir.model.access.csv",
        "data/data.xml",
        'wizard\create_appointmen_view.xml',
        "views/hospital_view.xml",
        "views/sale_view.xml",
        "views/kids_view.xml",
        "views/gender_view.xml",
        "views/appointmen_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
