{
    'name' : 'Hospital Manegement',
    'version' : '1.1',
    'summary': 'hospital application software system',
    'sequence': 1,
    'description': """hospital application for odoo""",
    'category': 'hospital',
    'website': 'https://www.odoohospi.tech',
    'depends' : [
        'base',
        'menu',
        'om_kartu_keluarga'
        ],
    'data': [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "data/code_alasan_datang.xml",
        "data/data.xml",
        "views/perawat_triase_view.xml",
        "views/icpc_view.xml",
        "views/icd_view.xml",
        "views/medik_view.xml",
    ],
    'demo': [],
    'qweb': [],
    'application': True,    
}
