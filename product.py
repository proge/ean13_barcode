# -*- coding: utf-8 -*-

from osv import osv, fields
from tools.translate import _


class product_product(osv.osv):
    _inherit = 'product.product'
    _columns = {
        'barcode': fields.char(_('Barcode'), size=13),
        }

product_product()
