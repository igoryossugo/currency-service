from decimal import Decimal

import pytest

from currency_service.currency.enums import CurrencyID
from currency_service.currency.models import Currency
from currency_service.extensions.fake.backends.cotation import (
    FakeCotationBackend
)


class TestFakeCotationBackend:

    @pytest.fixture
    def backend(self):
        return FakeCotationBackend()

    @pytest.fixture
    def currency(self):
        return Currency(id=CurrencyID.BRL.value, value=Decimal('50.00'))

    def test_get_should_return_a_currency_object(self, backend, currency):
        currency_id = CurrencyID.EUR.value
        response = backend.get(currency=currency, currency_id=currency_id)
        assert isinstance(response, Currency)
        assert response.id == currency_id

    def test_list_should_return_a_list_of_currency(self, backend, currency):
        currency_ids = [
            CurrencyID.EUR.value,
            CurrencyID.USD.value
        ]
        response = backend.list(currency=currency, currency_ids=currency_ids)
        assert isinstance(response, list)
        for currency_response in response:
            assert isinstance(currency_response, Currency)
            assert currency_response.id in currency_ids
