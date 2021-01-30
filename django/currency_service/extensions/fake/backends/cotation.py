from django.conf import settings
from ramos.mixins import SingletonCreateMixin

from currency_service.backends.cotation.backend import CotationBackend
from currency_service.currency.models import Currency


class FakeCotationBackend(SingletonCreateMixin, CotationBackend):
    id = 'fake'
    name = 'Fake'

    def get(self, currency, currency_id):
        return Currency(id=currency_id, value=currency.value)

    def list(self, currency, currency_ids=None):
        currency_ids = currency_ids or settings.DEFAULT_CURRENCY_IDS
        return [
            Currency(id=currency_id, value=currency.value)
            for currency_id in currency_ids
        ]
