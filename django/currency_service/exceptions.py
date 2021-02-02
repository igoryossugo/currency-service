class APIException(Exception):
    http_status = 500
    error_message = 'Internal Server Error'
    error_code = 'internal_server_error'

    def __init__(self, http_status=None, error_message=None, error_code=None):
        if http_status:
            self.http_status = http_status

        if error_message:
            self.error_message = error_message

        if error_code:
            self.error_code = error_code

    def __str__(self):
        return (
            f'{self.__class__.__name__}: '
            f'{self.http_status} - {self.error_message} - {self.error_code}'
        )

    def as_dict(self):
        return {
            'error_code': self.error_code,
            'error_message': self.error_message,
        }


class BadRequest(APIException):
    http_status = 400
    error_message = 'Bad Request'
    error_code = 'bad_request'
