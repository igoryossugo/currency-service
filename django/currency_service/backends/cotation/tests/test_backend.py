from decimal import Decimal
from unittest import mock

import pytest

from currency_service.backends.cotation.backend import CotationBackend
from currency_service.backends.cotation.models import Cotation


class DummyCotationBackend(CotationBackend):

    def _get(self, target_currency, source_currency):
        pass


class TestCotationBackend:

    @pytest.fixture
    def backend(self):
        return DummyCotationBackend()

    def test_get_should_return_cotation_from_cache(self, backend):
        with mock.patch.object(backend, '_get') as mocked__get:
            mocked__get.return_value = Cotation(
                value=Decimal('10'),
                source_currency='BRL',
                target_currency='USD'
            )
            backend.get(target_currency='USD', source_currency='BRL')
            backend.get(target_currency='USD', source_currency='BRL')

        mocked__get.assert_called_once_with(
            target_currency='USD',
            source_currency='BRL'
        )

    def test_get_should_not_return_from_cache_with_different_currency_id(
        self,
        backend
    ):
        with mock.patch.object(backend, '_get') as mocked__get:
            mocked__get.return_value = Cotation(
                value=Decimal('10'),
                source_currency='BRL',
                target_currency='USD'
            )
            backend.get(target_currency='USD', source_currency='BRL')
            backend.get(target_currency='USD', source_currency='EUR')

        mocked__get.call_count == 2
