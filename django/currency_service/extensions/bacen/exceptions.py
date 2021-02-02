from currency_service.exceptions import APIException, BadRequest


class BacenServerError(APIException):
    http_status = 500
    error_code = 'bacen_server_error'

    def __init__(self, error):
        self.error_message = f'Unexpected bacen server error: {error}'


class InvalidBacenCurrencyID(BadRequest):
    error_code = 'invalid_bacen_currency_id'

    def __init__(self, currency_id):
        self.error_message = (
            f'Invalid or unregistered bacen currency ID: {currency_id}'
        )
