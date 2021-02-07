from abc import abstractmethod

from currency_service.product.models import Product


class CatalogBackend:
    id = None
    name = None

    @abstractmethod
    def get_product(
        self,
        sku: str,
        seller: str
    ) -> Product:  # pragma: no cover
        pass
