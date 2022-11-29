{
    'name' : 'obat',
    'version' : '1.1',
    'summary': 'obat application software system',
    'sequence': 1,
    'description': """obat application for odoo""",
    'category': 'obat',
    'website': 'https://www.odoohospi.tech',
    'depends' : ['base',
                 'menu'],
    'data': [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "views/obat_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'application': True,
}
