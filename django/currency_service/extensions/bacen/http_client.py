import logging
from typing import Dict

from zeep import Client

from django.conf import settings

logger = logging.getLogger(__name__)


class BacenHTTPClient:

    def __init__(self, wsdl_base_url=None):
        wsdl_base_url = wsdl_base_url or settings.BACEN_WSDL_BASE_URL
        self.client = Client(wsdl_base_url)

    def get_cotation(self, bacen_currency_id: int) -> Dict:
        logger.debug(
            f'Calling bacen web service to get {bacen_currency_id} cotation'
        )
        response = self.client.service.getUltimoValorVO(in0=bacen_currency_id)
        logger.debug(
            f'Received {response} from bacen for {bacen_currency_id}'
        )
        return response
