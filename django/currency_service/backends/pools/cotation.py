from ramos.mixins import DefaultBackendMixin
from ramos.pool import BackendPool


class CotationBackendPool(DefaultBackendMixin, BackendPool):
    """
    A pool of cotation backends, for generic backends.
    For more informations of ramos: https://github.com/luizalabs/ramos
    """
    backend_type = 'cotation'
    SETTINGS_KEY = 'DEFAULT_COTATION_BACKEND'
