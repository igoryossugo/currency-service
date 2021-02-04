from abc import abstractmethod

from currency_service.backends.catalog.models import Product


class CatalogBackend:
    id = None
    name = None

    @abstractmethod
    def get_product(self, sku: str, seller: str) -> Product:
        pass
