import copy
from decimal import Decimal

import pytest

from currency_service.extensions.bacen.constants import BACEN_CURRENCY_IDS
from currency_service.extensions.bacen.exceptions import InvalidBacenCurrencyID
from currency_service.extensions.bacen.helpers import (
    build_cotation_by_bacen_response,
    get_bacen_currency_id
)


class TestGetBacenCurrencyID:

    def test_should_return_bacen_currency_id(self):
        bacen_currency_id = get_bacen_currency_id(currency_id='USD')
        assert bacen_currency_id == BACEN_CURRENCY_IDS['USD']

    def test_should_raise_error_with_invalid_bacen_currency_id(self):
        with pytest.raises(InvalidBacenCurrencyID):
            get_bacen_currency_id(currency_id='ABC')


class TestBuildCotationByBacenResponse:

    def test_should_return_cotation(self, response_bacen_cotation):
        target_currency = 'USD'
        source_currency = 'BRL'
        cotation = build_cotation_by_bacen_response(
            target_currency=target_currency,
            source_currency=source_currency,
            response_target_cotation=response_bacen_cotation
        )
        assert cotation.target_currency == target_currency
        assert cotation.source_currency == source_currency
        assert cotation.value == (
            response_bacen_cotation['ultimoValor']['valor']['_value_1']
        )

    def test_should_return_cotation_with_response_source_cotation(
        self,
        response_bacen_cotation
    ):
        target_currency = 'USD'
        source_currency = 'EUR'

        response_source_bacen_cotation = copy.deepcopy(response_bacen_cotation)
        response_source_bacen_cotation['ultimoValor']['valor']['_value_1'] = (
            Decimal('6.253')
        )

        cotation = build_cotation_by_bacen_response(
            target_currency=target_currency,
            source_currency=source_currency,
            response_target_cotation=response_bacen_cotation,
            response_source_cotation=response_source_bacen_cotation
        )
        assert cotation.target_currency == target_currency
        assert cotation.source_currency == source_currency
        assert cotation.value == (
            response_bacen_cotation['ultimoValor']['valor']['_value_1'] /
            response_source_bacen_cotation['ultimoValor']['valor']['_value_1']
        )
