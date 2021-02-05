from ramos.mixins import DefaultBackendMixin
from ramos.pool import BackendPool


class CatalogBackendPool(DefaultBackendMixin, BackendPool):
    """
    A pool of catalog backends, for generic backends.
    For more informations of ramos: https://github.com/luizalabs/ramos
    """
    backend_type = 'catalog'
    SETTINGS_KEY = 'DEFAULT_CATALOG_BACKEND'
