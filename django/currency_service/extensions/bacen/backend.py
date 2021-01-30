import logging

from ramos.mixins import SingletonCreateMixin

from currency_service.backends.cotation.backend import CotationBackend
from currency_service.backends.cotation.constants import (
    DEFAULT_LOCAL_CURRENCY_ID
)
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

    def get(self, target_currency, source_currency=DEFAULT_LOCAL_CURRENCY_ID):
        bacen_source_currency_id = get_bacen_currency_id(
            currency_id=target_currency
        )

        http_client = BacenHTTPClient()
        try:
            response_target_cotation = http_client.get_cotation(
                bacen_currency_id=bacen_source_currency_id
            )
        except Exception as e:
            logger.error(
                'Error to get bacen cotation with '
                f'currency_id: {target_currency}. Error: {e}'
            )
            raise BacenServerError(e)

        response_source_cotation = None
        if source_currency != DEFAULT_LOCAL_CURRENCY_ID:
            bacen_target_currency_id = get_bacen_currency_id(
                currency_id=source_currency
            )
            try:
                response_source_cotation = http_client.get_cotation(
                    bacen_currency_id=bacen_target_currency_id
                )
            except Exception as e:
                logger.error(
                    'Error to get bacen cotation with different local '
                    f'currency_id. currency_id: {source_currency}. Error: {e}'
                )
                raise BacenServerError(e)

        return build_cotation_by_bacen_response(
            target_currency=target_currency,
            source_currency=source_currency,
            response_target_cotation=response_target_cotation,
            response_source_cotation=response_source_cotation,
        )
