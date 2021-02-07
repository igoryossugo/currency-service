import logging

from ramos.mixins import SingletonCreateMixin

from currency_service.backends.cotation.backend import CotationBackend
from currency_service.currency.constants import DEFAULT_LOCAL_CURRENCY_ID
from currency_service.extensions.bacen.exceptions import BacenServerError
from currency_service.extensions.bacen.helpers import (
    build_cotation_by_bacen_response,
    get_bacen_currency_id
)
from currency_service.extensions.bacen.http_client import BacenHTTPClient

logger = logging.getLogger(__name__)


class BacenCotationBackend(SingletonCreateMixin, CotationBackend):
    id = 'bacen'
    name = 'Banco central do Brasil'

    def _get(self, target_currency, source_currency=DEFAULT_LOCAL_CURRENCY_ID):
        response_target_cotation, response_source_cotation = None, None
        http_client = BacenHTTPClient()

        if target_currency != DEFAULT_LOCAL_CURRENCY_ID:
            response_target_cotation = self._get_bacen_cotation(
                http_client=http_client,
                currency_id=target_currency
            )

        if source_currency != DEFAULT_LOCAL_CURRENCY_ID:
            response_source_cotation = self._get_bacen_cotation(
                http_client=http_client,
                currency_id=target_currency
            )

        return build_cotation_by_bacen_response(
            target_currency=target_currency,
            source_currency=source_currency,
            response_target_cotation=response_target_cotation,
            response_source_cotation=response_source_cotation,
        )

    def _get_bacen_cotation(self, http_client, currency_id):
        bacen_currency_id = get_bacen_currency_id(currency_id=currency_id)
        try:
            return http_client.get_cotation(
                bacen_currency_id=bacen_currency_id
            )
        except Exception as e:
            logger.error(
                'Error to get bacen cotation with '
                f'currency_id: {bacen_currency_id}. Error: {e}'
            )
            raise BacenServerError(e)
