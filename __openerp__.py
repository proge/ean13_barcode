# -*- coding: utf-8 -*-

{
    "name": "EAN13 to Barcode",
    "version": "0.1",
    "author": "Proge",
    "category": "Product",
    "website": "http://proge.com.br",
    "description": """
    Module to hide the EAN13 field and let any barcode type to be stored
    """,
    'depends': ['product'],
    'init_xml': [],
    'update_xml': [
        'product_view.xml',
        ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'active': False,
}
