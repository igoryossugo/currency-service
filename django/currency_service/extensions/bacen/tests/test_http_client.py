from unittest import mock

from currency_service.extensions.bacen.http_client import BacenHTTPClient


class TestBacenHTTPClient:

    def test_get_cotation_should_call_bacen_client(self):
        bacen_currency_id = 1
        http_client = BacenHTTPClient()
        with mock.patch.object(http_client, 'client') as mocked_client:
            http_client.get_cotation(bacen_currency_id)

        mocked_client.service.getUltimoValorVO.assert_called_with(
            in0=bacen_currency_id
        )
