import pytest

from currency_service.backends.cotation.models import Cotation
from currency_service.currency.enums import CurrencyID
from currency_service.extensions.fake.backends.cotation import (
    FakeCotationBackend
)


class TestFakeCotationBackend:

    @pytest.fixture
    def backend(self):
        return FakeCotationBackend()

    def test_get_should_return_a_cotation_object(self, backend):
        cotation = backend.get(target_currency=CurrencyID.USD.value)
        assert isinstance(cotation, Cotation)
        assert cotation.target_currency == CurrencyID.USD.value
