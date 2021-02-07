from decimal import Decimal

from currency_service.product.models import Product


def get_fake_product(sku, seller):
    fake_products = {
        'abdef1234_centauro': Product(
            sku=sku,
            seller=seller,
            price=Decimal('1499.90')
        ),
        'jkqrm3214_centauro': Product(
            sku=sku,
            seller=seller,
            price=Decimal('1499.90')
        ),
        '3214mfam4_nike': Product(
            sku=sku,
            seller=seller,
            price=Decimal('1499.90')
        ),
        '3n5jk223m_lupo': Product(
            sku=sku,
            seller=seller,
            price=Decimal('1499.90')
        ),
    }
    return fake_products[f'{sku}_{seller}']
