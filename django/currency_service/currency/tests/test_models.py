from decimal import Decimal
from unittest import mock

from currency_service.backends.cotation.models import Cotation
from currency_service.currency.enums import CurrencyID
from currency_service.currency.models import Currency


class TestCurrency:

    def test_convert_should_convert_value_and_id(self):
        initial_value = Decimal('100.00')
        currency = Currency(
            id=CurrencyID.BRL.value,
            value=initial_value
        )
        currency.convert(id=CurrencyID.USD.value)

        assert currency.id == CurrencyID.USD.value
        assert currency.value != initial_value

    def test_convert_should_call_cotation_backend(self):
        with mock.patch(
            'currency_service.extensions.fake.backends.cotation.'
            'FakeCotationBackend.get',
            return_value=Cotation(
                value=Decimal('5.72'),
                source_currency=CurrencyID.USD.value,
                target_currency=CurrencyID.USD.value,
            )
        ) as mocked_backend:
            currency = Currency(
                id=CurrencyID.BRL.value,
                value=Decimal('100.00')
            )
            currency.convert(id=CurrencyID.USD.value)

        mocked_backend.assert_called_with(
            target_currency=CurrencyID.USD.value,
            source_currency=CurrencyID.BRL.value
        )

    def test_convert_should_not_call_cotation_backend_with_same_id(self):
        with mock.patch(
            'currency_service.extensions.fake.backends.cotation.'
            'FakeCotationBackend.get',
        ) as mocked_backend:
            currency = Currency(
                id=CurrencyID.USD.value,
                value=Decimal('100.00')
            )
            currency.convert(id=CurrencyID.USD.value)

        assert not mocked_backend.called
