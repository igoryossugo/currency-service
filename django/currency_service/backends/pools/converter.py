from ramos.mixins import DefaultBackendMixin
from ramos.pool import BackendPool


class ConverterBackendPool(DefaultBackendMixin, BackendPool):
    """
    A pool of converter backends, for generic backends.
    For more informations of ramos: https://github.com/luizalabs/ramos
    """
    backend_type = 'converter'
    SETTINGS_KEY = 'DEFAULT_CONVERTER_BACKEND'
