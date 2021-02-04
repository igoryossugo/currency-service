import pytest

from currency_service.backends.catalog.models import Product
from currency_service.extensions.fake.backends.catalog import (
    FakeCatalogBackend
)


class TestFakeCatalogBackend:

    @pytest.fixture
    def backend(self):
        return FakeCatalogBackend()

    def test_get_should_return_an_product_object(self, backend):
        sku = 'abc12345'
        seller = 'centauro'
        product = backend.get_product(sku=sku, seller=seller)
        assert isinstance(product, Product)
        assert product.sku == sku
        assert product.seller == seller
