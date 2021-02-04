from decimal import Decimal

from ramos.mixins import SingletonCreateMixin

from currency_service.backends.catalog.backend import CatalogBackend
from currency_service.backends.catalog.models import Product


class FakeCatalogBackend(SingletonCreateMixin, CatalogBackend):
    id = 'fake'
    name = 'Fake'

    def get_product(self, sku, seller):
        return Product(
            sku=sku,
            seller=seller,
            price=Decimal('1499.90'),
            old_price=Decimal('1899.90'),
            cash_price=Decimal('1199.90'),
        )
