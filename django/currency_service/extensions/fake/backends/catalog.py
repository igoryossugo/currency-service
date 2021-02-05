from ramos.mixins import SingletonCreateMixin

from currency_service.backends.catalog.backend import CatalogBackend
from currency_service.backends.catalog.exceptions import ProductNotFound
from currency_service.extensions.fake.factory import get_fake_product


class FakeCatalogBackend(SingletonCreateMixin, CatalogBackend):
    id = 'fake'
    name = 'Fake'

    def get_product(self, sku, seller):
        try:
            return get_fake_product(sku=sku, seller=seller)
        except KeyError:
            raise ProductNotFound(sku=sku, seller=seller)
