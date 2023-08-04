{
    'name': 'Module Custom Pembelian',
    'version': '1.0.0.0',
    'category' : 'purchase',
    'summary' : 'Modul Custom Pembeliann',
    'description' : """
                    Tes custom module
                    """,
    'website'   : '',
    'author'    : 'wisnu',
    'depends' : ['web','base'],
    'data' : [
        'security/ir.model.access.csv'
        'views/algoritma_pembelian_view.xml'
        'views/algoritma_pembelian_action.xml'
        'views/algoritma_pembelian_menuitem.xml'
    ],
    'installable': True,
    'application' : True,
    'license' : 'OEEL-1',

}