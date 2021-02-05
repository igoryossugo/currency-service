from unittest import mock

import pytest

from currency_service.backends.cotation.models import Cotation
from currency_service.currency.constants import DEFAULT_LOCAL_CURRENCY_ID
from currency_service.currency.enums import CurrencyID
from currency_service.extensions.bacen.backend import BacenCotationBackend
from currency_service.extensions.bacen.helpers import get_bacen_currency_id


@pytest.fixture
def backend():
    return BacenCotationBackend()


class TestBacenCotationBackend:

    @pytest.fixture
    def mocked_http_client(self, backend, response_bacen_cotation):
        return mock.patch(
            'currency_service.extensions.bacen.backend.BacenHTTPClient.'
            'get_cotation',
            return_value=response_bacen_cotation
        )

    def test_get_should_return_cotation_object(
        self,
        backend,
        mocked_http_client
    ):
        with mocked_http_client:
            cotation = backend._get(target_currency=CurrencyID.USD.value)

        assert isinstance(cotation, Cotation)
        assert cotation.target_currency == CurrencyID.USD.value

    def test_get_should_call_bacen_http_client(
        self,
        backend,
        mocked_http_client
    ):
        with mocked_http_client as mocked_client:
            backend._get(target_currency=CurrencyID.USD.value)

        mocked_client.assert_called_with(
            bacen_currency_id=get_bacen_currency_id(CurrencyID.USD.value)
        )

    def test_get_should_call_bacen_http_client_twice_with_source_currency(
        self,
        backend,
        mocked_http_client
    ):
        with mocked_http_client as mocked_client:
            backend._get(
                target_currency=CurrencyID.USD.value,
                source_currency=CurrencyID.EUR.value
            )

        len(mocked_client.mock_calls) == 2

    def test_get_should_call_get_bacen_currency_id(
        self,
        backend,
        mocked_http_client
    ):
        with mocked_http_client, mock.patch(
            'currency_service.extensions.bacen.backend.get_bacen_currency_id'
        ) as mocked_helper:
            backend._get(target_currency=CurrencyID.USD.value)

        mocked_helper.assert_called_with(currency_id=CurrencyID.USD.value)

    def test_get_should_call_build_cotation_by_bacen_response(
        self,
        backend,
        mocked_http_client,
        response_bacen_cotation
    ):
        with mocked_http_client, mock.patch(
            'currency_service.extensions.bacen.backend.'
            'build_cotation_by_bacen_response'
        ) as mocked_helper:
            backend._get(target_currency=CurrencyID.USD.value)

        mocked_helper.assert_called_with(
            target_currency=CurrencyID.USD.value,
            source_currency=DEFAULT_LOCAL_CURRENCY_ID,
            response_target_cotation=response_bacen_cotation,
            response_source_cotation=None,
        )

    def test_get_should_call_build_cotation_by_bacen_response_with_source_cotation(  # noqa
        self,
        backend,
        mocked_http_client,
        response_bacen_cotation
    ):
        with mocked_http_client, mock.patch(
            'currency_service.extensions.bacen.backend.'
            'build_cotation_by_bacen_response'
        ) as mocked_helper:
            backend._get(
                target_currency=CurrencyID.USD.value,
                source_currency=CurrencyID.EUR.value
            )

        mocked_helper.assert_called_with(
            target_currency=CurrencyID.USD.value,
            source_currency=CurrencyID.EUR.value,
            response_target_cotation=response_bacen_cotation,
            response_source_cotation=response_bacen_cotation,
        )
